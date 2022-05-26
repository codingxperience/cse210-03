"""
Author: Mmusi Hubona

Task: class Word
"""

from game.terminal_service import TerminalService
import random

class Word:
    """This class is responsible for generating a word which the player 
    must then guess 
    """
    def __init__(self):
        self.terminalService = TerminalService()
        self._words = ["moon","earth","abyss","bread","knife","butter","atom"]
        self._word = random.choice(self._words)
        self._guess_word = ["_"] * len(self._word)

    def secret_word(self):
        """This method gets the randomly generated word."""
        return self._word

    def guess_word(self):
        """This method gets the number of characters for the hidden word"""
        return self._guess_word
    
    def draw_word_guess(self):
        """This methods outputs hidden word to the terminal, by iterating 
        through the hidden word and printing a "_" for each letter.
        
        e.g atom = _ _ _ _
        """
        for i in self._guess_word:
            self.terminalService.write_text_same_line(i + " ")