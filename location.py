from monsterfactory import MonsterFactory
from character import NPC
import random

class Location:
    name = ""
    adjacentLocations = []
    npcs = []
    monsters = []
    boss = None

    def getName(self):
        return self.name

    def getNPC(self):
        if len(self.npcs) > 0:
            return self.npcs[random.randint(0, len(self.npcs) - 1)]
        else:
            print("There are no NPCs in this location.")
            return None

    def getMonster(self):
        if len(self.monsters) > 0:
            return self.monsters.pop()
        elif self.boss is not None:
            print("With all other monsters dead, the area boss appeared!")
            boss = self.boss
            self.boss = None
            return boss
        else:
            print("There are no monsters in this location.")
            return None

    def addMonster(self, monster):
        self.monsters.append(monster)
        random.shuffle(self.monsters)
        
    def getAdjacentLocationNames(self):
        names = []
        for location in self.adjacentLocations:
            names.append(location.getName())
        return names

    def getAdjacentLocation(self, name):
        for location in self.adjacentLocations:
            if name == location.getName():
                return location
        return None
        

class TutorialIsland(Location):
    npcs = []
    def __init__(self):
        self.name = "Tutorial Island"
        self.npcs = [NPC("Old Man", [
            "Hello adventurer, welcome to Tutorial Island!",
            "This game is only a proof of concept, so there's not much content.",
            "Try changing location to Tutorial Dungeon and I'll tell you about fighting."
        ])]
        tutorialDungeon = RandomDungeon("Tutorial Dungeon", self, 1,[NPC("Old Man", [
            "Hello again, welcome to the Tutorial Dungeon!",
            "Here there will be a few monsters for you to fight by selecting \"battle\".",
            "Once you've beaten all the regular monsters, a powerful boss monster will appear!",
            "Why don't you try it out?"
        ])

        ])
        self.adjacentLocations = [tutorialDungeon]

class RandomDungeon(Location):
    monsters = []
    npcs = []
    boss = None
    def __init__(self, name, prevLocation, level, npcs = []):
        self.name = name
        self.adjacentLocations = [prevLocation]
        monstercount = random.randint(1, 5)
        monsterFactory = MonsterFactory()
        for loop in range(monstercount):
            self.monsters.append(monsterFactory.createMonster(level))
        self.boss = monsterFactory.createBoss(level)
        self.npcs = npcs