from game import Game
from controls import Controls
from game_screen import GameScreen

game = Game()
game_controls = Controls(game.segments[0])
screen = GameScreen(game_controls.control_func)

game.play(screen.game_screen)
