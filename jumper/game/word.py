"""
Author: Mmusi Hubona
Task: Class
"""

from game.terminal_service import TerminalService
# from game.parachutist import Parachutist
import random


class Word:
    """Generates guess word and keeps track of user guesses"""
    def __init__(self):
        self.terminalService = TerminalService()
        # self._chute = Parachutist()
        words = ["moon","earth","abyss","bread","knife","butter","atom", "mass"]
        self._word = random.choice(words)
        self._display = ["_" for letter in self._word]
        self.guesses = 5

    def set_display(self, value):
        """Set display value"""
        self._display = value
        
    def get_word(self):
        """Gets the quessed word"""
        return self._word

    def get_display(self):
        """Gets the display"""
        return self._display

    def show(self):
        """Display secret word in hidden format e.g _ _ _ """
        display = " ".join(self.get_display())
        self.terminalService.write_text(display)

    def get_word_index(self, guess):
        """Get the position of the guessed word within the letter"""
        locations = []
        for index, char in enumerate(list(self.get_word())):
            if char == guess:
                locations.append(index)
        return locations

    def update(self, idx, letter):
        """ places the guessed letter e.g _ _ e _ p"""
        for number in idx:
            self._display[number] = letter

    def check_guess(self, guess):
        """Checks whether the guessed letter is present in the secret word"""
        if guess in self.get_word():
            idx = self.get_word_index(guess)
            self.update(idx, guess)

    def check_for_win(self):
        """Checks if all the hidden letters have been matched"""
        display = "".join(self._display)
        word = self.get_word()
        if display == word:
            return True
