"""
Author: Fred Okorio
Task: parachutist class
"""


from game.terminal_service import TerminalService

class Parachutist:

  def __init__(self):
    self.terminalService = TerminalService()
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
    self._parachutist.pop(0)

  def has_parachute(self):
    """This method verifies if the player stills has the parachute"""
    return len(self.has_parachute) >= 6

  def parachute_gone(self):
    """This method ends the game if the player
       no parachute frame to keep playing
     """
    self._parachutist[0] = "x"