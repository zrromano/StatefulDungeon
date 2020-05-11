from character import Monster
import random

class MonsterFactory:
    monsterNames = [
        "Goblin",
        "Scorpion",
        "Orc"
    ]

    bossNames = [
        "Minotaur",
        "Dragon Hatchling",
        "Chungus"
    ]
    def createMonster(self, level):
        base = level * 10
        return Monster(
            self.monsterNames[random.randint(0, len(self.monsterNames) - 1)],
            random.randint(base * 0.8, base * 1.2),
            random.randint(base * 0.8, base * 1.2),
            random.randint(base * 3, base * 5)
            )

    def createBoss(self, level):
        base = level * 10
        return Monster(
            self.bossNames[random.randint(0, len(self.bossNames) - 1)],
            random.randint(base, base * 1.6),
            random.randint(base, base * 1.6),
            random.randint(base * 5, base * 7)
            )