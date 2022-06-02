"""
Author: Fred Okorio
Task: parachutist class
"""


from re import X
from game.terminal_service import TerminalService
# from game.word import Word

class Parachutist:

  def __init__(self):
    self.terminalService = TerminalService()
    # self._word = Word()
    self._parachutist = [
      " ____ ",
      "/____\ ",
      "\    / ",
      " \  / ",
      "   o   ",
      "  /|\ ",
      "  / \ ",
      "",
      "^^^^^^^"
    ]

  def draw_parachutist(self):
    """Iterates through the lines in a list above to 
       create the jumper. This class will need the terminalService
       class(Import terminalService)
    """
    for piece in self._parachutist:
      self.terminalService.write_text(piece)

  def remove_parachute_piece(self):
    """This function cuts a line on the player's parachute 
       if thethe guess is wrong.
    """
    # guess = self._word.get_word()
    # if guess not in self._word.get_word():
    self._parachutist.pop(0)

  def has_parachute(self):
    """This method verifies if the player stills has the parachute"""
    return len(self.has_parachute) >= 6

  def parachute_gone(self):
    """This method ends the game if the player
       no parachute frame to keep playing
     """
    if len(self._parachutist) == 5:
      self._parachutist[0] = "   x"
  