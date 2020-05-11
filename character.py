import random

class Character:
    name = ""
    attack = 0
    defense = 0
    maxhealth = 0
    currenthealth = 0

    def getName(self):
        return self.name
        
    def getCurrentHealth(self):
        return self.currenthealth

    def getMaxHealth(self):
        return self.maxhealth
    
    def getAttack(self):
        return self.attack

    def getDefense(self):
        return self.defense

    def updateHealth(self, value):
        if value > 0:
            mod = random.randint(80, 120)
            value *= mod / (mod + self.defense)
            value = int(value)
            if self.currenthealth - value <= 0:
                self.currenthealth = 0
                print(self.name, "took", value, "damage!")
                print(self.name, "died...")
                return False
            else:
                self.currenthealth -= value
                print(self.name, "took", value, "damage!")
                return True

        elif value < 0:
            if self.currenthealth - value > self.maxhealth:
                value = (self.maxhealth - self.currenthealth)
                self.currenthealth = self.maxhealth
                print(self.name, "healed", value, "hit points.", self.name, "is at full health!")
                return True
            else:
                value = -value
                self.currenthealth += value
                print(self.name, "healed", value, "hit points.")
                return True

class Hero(Character):
    level = 0
    exp = 0
    expToLevel = 0

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.expToLevel = 100
        self.attack = 15
        self.defense = 15
        self.maxhealth = 100
        self.currenthealth = 100

    def getLevel(self):
        return self.level

    def getExp(self):
        return self.exp

    def getExpToLevel(self):
        return self.expToLevel

    def updateExp(self, value):
        if value != 0:
            self.exp += value
            print(self.name, "gained", value, "experience points!")
        if(self.exp >= self.expToLevel):
            self.levelUp()

    def levelUp(self):
        self.level += 1
        print(self.name, "leveled up!")
        print (self.name, "is now level", str(self.level) + "!") 
        self.exp -= self.expToLevel
        self.expToLevel *= 1.5
        choice = None
        while choice != "attack" and choice != "defense" and choice != "health":
            print("Which stat do you want to focus on?")
            choice = input("attack / defense / health: ")
            if choice != "attack" and choice != "defense" and choice != "health":
                print("Please choose \"attack\" or \"defense\" or \"health\"...")
        if choice == "attack":
            self.attack *= 1.5
            self.attack = int(self.attack)
            print(self.name + "'s attack has raised to", str(self.attack) + "!")
            self.defense *= 1.3
            self.defense = int(self.defense)
            print(self.name + "'s defense has raised to", str(self.defense) + "!")
            self.maxhealth *= 1.3
            self.maxhealth = int(self.maxhealth)
            self.currenthealth = self.maxhealth
            print(self.name + "'s max health has raised to", self.maxhealth, "and their health has been fully restored!")
        if choice == "defense":
            self.attack *= 1.3
            self.attack = int(self.attack)
            print(self.name + "'s attack has raised to", str(self.attack) + "!")
            self.defense *= 1.5
            self.defense = int(self.defense)
            print(self.name + "'s defense has raised to", str(self.defense) + "!")
            self.maxhealth *= 1.3
            self.maxhealth = int(self.maxhealth)
            self.currenthealth = self.maxhealth
            print(self.name + "'s max health has raised to", self.maxhealth, "and their health has been fully restored!")
        if choice == "health":
            self.attack *= 1.3
            self.attack = int(self.attack)
            print(self.name + "'s attack has raised to", str(self.attack) + "!")
            self.defense *= 1.3
            self.defense = int(self.defense)
            print(self.name + "'s defense has raised to", str(self.defense) + "!")
            self.maxhealth *= 1.5
            self.maxhealth = int(self.maxhealth)
            self.currenthealth = self.maxhealth
            print(self.name + "'s max health has raised to", self.maxhealth, "and their health has been fully restored!")
        if(self.exp >= self.expToLevel):
            self.levelUp()


class Monster(Character):
    def __init__(self, name, attack, defense, maxHealth):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.maxhealth = maxHealth
        self.currenthealth = maxHealth

    def decideNextMove(self):
        factor = random.randint(0, self.currenthealth + self.attack + self.defense)
        if factor == 0:
            return "retreat"
        elif factor <= self.currenthealth + self.attack:
            return "attack"
        else:
            return "defend"

class NPC(Character):
    attack = None
    defense = None
    maHealth = None
    currenthealth = None
    dialogue = []
    currentLine = 0

    def __init__(self, name, dialogue):
        self.name = name
        self.dialogue = dialogue

    def getNextLine(self):
        if len(self.dialogue) <= self.currentLine:
            return None

        else:
            self.currentLine += 1
            return self.dialogue[self.currentLine - 1]

    
