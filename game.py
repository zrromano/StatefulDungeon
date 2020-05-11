from gamestate import *

class Game:
    state = None
    def __init__(self):
        self.state = Start()

    def getState(self):
        return self.state.getName()

    def displayMenu(self):
        self.state.menu()

    def update(self, command):
        self.state.update(command)
        
if __name__ == '__main__':
    game = Game()
    while(game.getState() != "quit"):
        print("")
        game.displayMenu()
        command = input("Enter a command: ")
        print("")
        game.update(command)
    print("Thank you for playing!")


