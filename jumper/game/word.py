"""
Author: Mmusi Hubona
Task: Class
"""

from game.terminal_service import TerminalService
from game.parachutist import Parachutist
import random


class Word:
    """Generates guess word and keeps track of user guesses"""
    def __init__(self):
        self.terminalService = TerminalService()
        self._chute = Parachutist()
        words = ["moon","earth","abyss","bread","knife","butter","atom", "mass"]
        self._word = random.choice(words)
        self._display = ["_" for letter in self._word]
        self.wrong = 0
        self.correct = 0

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
        self._chute.parachute_gone()
        self._chute.draw_parachutist()
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
            self.correct += 1
        else:
            self._chute.remove_parachute_piece()
            self.wrong += 1

    def check_for_win(self):
        """Checks if all the hidden letters have been matched"""
        text = ""
        if self.correct == len(self.get_word()):
            text = "**You have won**"

        elif self.wrong == 4:
            text = "You have lost, your parachute is gone!!"
        
        elif len(self._chute._parachutist) == 5:
            text = "You have lost, your parachute is gone!!"
        return text

    def win(self):
        return (self.correct == len(self.get_word()))
    def loose(self):
        return (self.wrong == 4)
    def loose2(self):
        return (len(self._chute._parachutist) == 5)

