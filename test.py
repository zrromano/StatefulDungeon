from game import Game
from character import *
from unittest import mock
from unittest import TestCase
from unittest import main
import gamestate

class TestGame(TestCase):
    @mock.patch('gamestate.input', create=True)
    def testPlay(self, mocked_input):
        print("------------------")
        print("Testing game start")
        print("------------------")
        mocked_input.side_effect = ['Jeff','']
        game = Game()
        print("--Starting game--")
        game.update("play")
        self.assertEqual(game.getState(), "play")
        print("")
        print("")

    @mock.patch('gamestate.input', create=True)
    def testChat(self, mocked_input):
        print("------------------")
        print("Testing chat state")
        print("------------------")
        mocked_input.side_effect = ['Jeff','','','Tutorial Dungeon','']
        game = Game()
        print("--Starting game--")
        game.update("play")
        print("--Attempting to chat--")
        game.update("chat")
        self.assertEqual(game.getState(), "chat")
        game.update("continue")
        print("--Changing locations--")
        game.update("change location")
        print("--Attempting to chat--")
        game.update('chat')
        self.assertEqual(game.getState(), "chat")
        print("")
        print("")
    
    @mock.patch('gamestate.input', create=True)
    def testBattle(self, mocked_input):
        print("--------------------")
        print("Testing battle state")
        print("--------------------")
        mocked_input.side_effect = ['Jeff','','','Tutorial Dungeon','']
        game = Game()
        print("--Starting game--")
        game.update("play")
        print("--Attempting to battle--")
        game.update("battle")
        self.assertEqual(game.getState(), "play")
        print("--Changing location--")
        game.update("change location")
        print("--Attempting to battle--")
        game.update('battle')
        self.assertEqual(game.getState(), "battle")
        print("")
        print("")

    def testDamage(self):
        print("--------------------")
        print("Testing health update")
        print("--------------------")
        character = Hero("Jeff")
        print("--Attempting to damage nonfatally--")
        self.assertEqual(character.updateHealth(10), True)
        print("--Attempting to heal partially--")
        self.assertEqual(character.updateHealth(-1), True)
        print("--Attempting to heal fully--")
        self.assertEqual(character.updateHealth(-100), True)
        print("--Attempting to damage fatally--")
        self.assertEqual(character.updateHealth(300), False)
        print("")
        print("")

    @mock.patch('character.input', create=True)
    def testExp(self, mocked_input):
        print("------------------------------------")
        print("Testing experience gain and level up")
        print("------------------------------------")
        mocked_input.side_effect = ['attack', 'attack', 'attack']
        character = Hero("Jeff")
        print("--Attempting to gain exp--")
        character.updateExp(1)
        self.assertEqual(character.getLevel(), 1)
        print("--Attempting to level up--")
        character.updateExp(100)
        self.assertEqual(character.getLevel(), 2)
        self.assertEqual(character.getAttack(), 22)
        self.assertEqual(character.getDefense(), 19)
        self.assertEqual(character.getMaxHealth(), 130)
        print("--Attempting to level up twice--")
        character.updateExp(400)
        self.assertEqual(character.getLevel(), 4)
        print("")
        print("")

    def testMonsterAI(self):
        print("-----------------------")
        print("Testing that monster AI")
        print("-----------------------")
        monster = Monster("Jeff", 0, 0, 0)
        result = monster.decideNextMove()
        print(result)
        correct = result == "attack" or result == "defend" or result == "retreat"
        self.assertEqual(correct, True)
        print("")
        print("")


if __name__ == '__main__':
    main()