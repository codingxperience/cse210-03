"""
Author: Fred Okorio
Task: draw class
"""

class Draw:
  """
  The draw class piece handles the visuals of the game to indicate if the 
  player guessed the char letter correctly or wrongly  
  """
  def draw__(self):
    """
    This method has the if conditions for the correctly guessed word.
    if the player guesses wrong a line cut pattern is invoked 
    """
    if self.wrong == 1:
      print()
      print(" ____ ")
      print("/____\ ")
      print("\    / ")
      print(" \  / ")
      print("   o   ")
      print("  /|\ ")
      print("  / \ ")
      print("^^^^^^^")
      print()
    elif self.wrong == 2:
      print()
      print(" ")
      print("/____\ ")
      print("\    / ")
      print(" \  / ")
      print("   o   ")
      print("  /|\ ")
      print("  / \ ")
      print("^^^^^^^")
      print()
    elif self.wrong == 3:
      print()
      print("\    / ")
      print(" \  / ")
      print("   o   ")
      print("  /|\ ")
      print("  / \ ")
      print("^^^^^^^")
      print()
    elif self.wrong == 4:
      print()
      print(" \  / ")
      print("   o   ")
      print("  /|\ ")
      print("  / \ ")
      print("^^^^^^^")
      print()
    elif self.wrong == 5:
      print()
      print("   x   ")
      print("  /|\ ")
      print("  / \ ")
      print("^^^^^^^")
      print()
    else:
      print("Invalid input")
    
