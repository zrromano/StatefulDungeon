from character import *
from location import *
import time
import random

class GameState:
    player = None
    location = None
    talkingTo = None
    fighting = None
    name = "state"

    def getName(self):
        return self.name

    def changeState(self, state):
        self.__class__ = state

    def changeLocation(self, location):
        self.location = location
    

class Start(GameState):
    name = "start"

    def update(self, command):
        if command == "play":
            print("What do you want to be called?")
            name = input("Please enter a name: ")
            self.player = Hero(name)
            print("")
            print("Welcome to stateful dungeon", name + "! Your adventure is about to begin...")
            time.sleep(0.5)
            input("Press enter to continue...")
            self.changeLocation(TutorialIsland())
            self.changeState(Play)

        elif command == "quit":
            self.name = "quit"

        else:
            print("That command is invalid, please enter a valid command.")

    def menu(self):
        print("Welcome to Stateful dungeon!")
        print("To begin enter \"play\".")
        print("To exit enter \"quit\".")

class Play(GameState):
    name = "play"

    def update(self, command):
        if command == "change location":
            print("")
            print("Where would you like to go?")
            time.sleep(0.5)
            print("Available Locations:")
            time.sleep(0.5)
            locations = self.location.getAdjacentLocationNames()
            for name in locations:
                print(name)
                time.sleep(0.5)
            command = input("Enter one of the names above, or \"stay\" to stay where you are: ")
            if command == "stay":
                return
            newLocation = self.location.getAdjacentLocation(command)
            if newLocation is None:
                print("Invalid location")
                input("Press enter to continue...")
                return
            print("Moving to", command + "...")
            input("Press enter to continue...")
            self.changeLocation(newLocation)

        elif command == "chat":
            npc = self.location.getNPC()
            if npc is not None:
                self.talkingTo = npc
                self.changeState(Chat)
                return
            input("Press enter to continue...")
        
        elif command == "battle":
            monster = self.location.getMonster()
            if monster is not None:
                self.fighting = monster
                self.changeState(Battle)
                return
            input("Press enter to continue...")
        
        elif command == "quit":
            while command != "yes" and command != "no":
                print("")
                print("Are you sure you want to quit?")
                print("Your progress will not be saved.")
                command = input("yes/no: ")
            if command == "yes":
                self.name = "quit"

        else:
            print("That command is invalid, please enter a valid command.")
            input("Press enter to continue...")

    def menu(self):
        print("You are currently at", self.location.getName() + ".")
        print("You can \"change location\", find an npc to \"chat\" with, \"battle\" a nearby monster, or \"quit\".")

class Battle(GameState):
    name = "battle"

    def update(self, command):
        firstMove = random.randint(0,1)
        opponent = self.fighting.decideNextMove()
        if command == "attack":
            if opponent == "attack":
                if firstMove == 0:
                    print(self.player.getName(), "attacked!")
                    if self.fighting.updateHealth(self.player.getAttack()) == False:
                        self.winBattle()
                        return
                    print(self.fighting.getName(), "attacked!")
                    if self.player.updateHealth(self.fighting.getAttack()) == False:
                        self.die()
                        return
                else:
                    print(self.fighting.getName(), "attacked!")
                    if self.player.updateHealth(self.fighting.getAttack()) == False:
                        self.die()
                        return
                    print(self.player.getName(), "attacked!")
                    if self.fighting.updateHealth(self.player.getAttack()) == False:
                        self.winBattle()
                        return

            elif opponent == "defend":
                print(self.player.getName(), "attacked!")
                print("But", self.fighting.getName(), "defended...")
                if self.fighting.updateHealth(int(self.player.getAttack() / 2)) == False:
                    self.winBattle()
                    return

            else:
                if firstMove == 0:
                    print(self.player.getName(), "attacked!")
                    if self.fighting.updateHealth(self.player.getAttack()) == False:
                        self.winBattle()
                        return
                    print(self.fighting.getName(), "attempted to run away...")
                    if random.randint(0, self.fighting.getCurrentHealth()) <= 5:
                        print("and succeeded...")
                        self.runAway()
                        return
                    else:
                        print("and failed!")
                else:
                    print(self.fighting.getName(), "attempted to run away...")
                    if random.randint(0, self.fighting.getCurrentHealth()) <= 5:
                        print("and succeeded...")
                        self.runAway()
                        return
                    else:
                        print("and failed!")
                        print(self.player.getName(), "attacked!")
                        if self.fighting.updateHealth(self.player.getAttack()) == False:
                            self.winBattle()
                            return

        elif command == "defend":
            if opponent == "attack":
                print(self.fighting.getName(), "attacked...")
                print("But", self.player.getName(), "defended!")
                if self.player.updateHealth(int(self.fighting.getAttack() / 2)) == False:
                    self.die()
                    return

            elif opponent == "defend":
                print("Both fighters tried to defend...")

            else:
                print(self.player.getName(), "attempted to defend...")
                print(self.fighting.getName(), "attempted to run away...")
                if random.randint(0, self.fighting.getCurrentHealth()) <= 5:
                    print("and succeeded...")
                    self.runAway()
                    return
                else:
                    print("and failed!")

        elif command == "retreat":
            if opponent == "attack":
                if firstMove == 0:
                    print(self.player.getName(), "attempted to run away...")
                    if random.randint(0, self.player.getCurrentHealth()) <= 5 + self.player.getLevel():
                        print("and succeeded!")
                        self.runAway()
                        return
                    else:
                        print("and failed...")
                        print(self.fighting.getName(), "attacked!")
                        if self.player.updateHealth(self.fighting.getAttack()) == False:
                            self.die()
                            return
                else:
                    print(self.fighting.getName(), "attacked!")
                    if self.player.updateHealth(self.fighting.getAttack()) == False:
                        self.die()
                        return
                    print(self.player.getName(), "attempted to run away...")
                    if random.randint(0, self.player.getCurrentHealth()) <= 5 + self.player.getLevel():
                        print("and succeeded!")
                        self.runAway()
                        return
                    else:
                        print("and failed...")

            elif opponent == "defend":
                print(self.fighting.getName(), "attempted to defend...")
                print(self.player.getName(), "attempted to run away...")
                if random.randint(0, self.player.getCurrentHealth()) <= 5 + self.player.getLevel():
                    print("and succeeded!")
                    self.runAway()
                    return
                else:
                    print("and failed...")

            else:
                if firstMove == 0:
                    print(self.player.getName(), "attempted to run away...")
                    if random.randint(0, self.player.getCurrentHealth()) <= 5 + self.player.getLevel():
                        print("and succeeded!")
                        self.runAway()
                        return
                    else:
                        print("and failed...")
                        print(self.fighting.getName(), "attempted to run away...")
                        if random.randint(0, self.fighting.getCurrentHealth()) <= 5:
                            print("and succeeded...")
                            self.runAway()
                            return
                        else:
                            print("and failed!")
                else:
                    print(self.fighting.getName(), "attempted to run away...")
                    if random.randint(0, self.fighting.getCurrentHealth()) <= 5:
                        print("and succeeded...")
                        self.runAway()
                        return
                    else:
                        print("and failed!")
                        print(self.player.getName(), "attempted to run away...")
                        if random.randint(0, self.player.getCurrentHealth()) <= 5 + self.player.getLevel():
                            print("and succeeded!")
                            self.runAway()
                            return
                        else:
                            print("and failed...")
        else:
            print("That command is invalid, please enter a valid command.")
        input("Press enter to continue...")

    def menu(self):
        print(self.player.getName(), "--")
        print("Level:", self.player.getLevel())
        print("Health:", self.player.getCurrentHealth(), "/", self.player.getMaxHealth())
        print(self.fighting.getName(), "--")
        print("Health:", self.fighting.getCurrentHealth(), "/", self.fighting.getMaxHealth())
        print("--")
        print("Actions: \"attack\", \"defend\", \"retreat\"")

    def runAway(self):
        self.location.addMonster(self.fighting)
        self.fighting = None
        self.changeState(Play)
        time.sleep(1.0)
        input("Press enter to continue...")

    def winBattle(self):
        print(self.player.getName(), "won the fight!")
        self.player.updateExp(self.fighting.getMaxHealth() * 2)
        self.fighting = None
        self.changeState(Play)
        time.sleep(1.0)
        input("Press enter to continue...")

    def die(self):
        self.name = "quit"
        print("Game over...")
        time.sleep(1.0)
        input("Press enter to exit...")


class Chat(GameState):
    name = "chat"

    def update(self, command):
        if command == "continue":
            print("")
            time.sleep(0.5)
            line = self.talkingTo.getNextLine()
            if line is not None:
                print(self.talkingTo.getName(), "says to", self.player.getName() + ":")
                while line is not None:
                    time.sleep(0.5)
                    print(line)
                    line = self.talkingTo.getNextLine()
            else:
                print(self.talkingTo.getName(), "has nothing more to say.")
            self.talkingTo = None
            time.sleep(1.0)
            input("Press enter to continue...")
            self.changeState(Play)

        elif command == "leave":
            self.changeState(Play)
        
        else:
            print("That command is invalid, please enter a valid command.")
                

    def menu(self):
        print(self.player.getName(), "found", self.talkingTo.getName(), "to chat with.")
        print("Enter \"continue\" to start a conversation or you can \"leave\".")