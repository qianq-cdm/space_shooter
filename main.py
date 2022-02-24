# Importer arcade
import arcade
from module.my_game import MyGame

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Space Shooter"


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
