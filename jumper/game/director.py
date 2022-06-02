"""
Author: Vaughn Al-Duane Pinnock
Task: class Director
"""

from game.terminal_service import TerminalService
from game.word import Word
from game.parachutist import Parachutist
from game.draw import Draw

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        parachutist (Parachutist): The game's parachutist.
        is_playing (boolean): Whether or not to keep playing.
        word (Word): The game's word.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._draw = Draw()
        self._is_playing = True
        self._parachutist = Parachutist()
        self._word = Word()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self.wrong = 0
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            self.wrong += 1

    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        guess = self._terminal_service.read_text("\nEnter your guess[a - z]: ")
        self._word.check_guess(guess)
        
    def _do_updates(self):
        """Keeps track of game progress.

        Args:
            self (Director): An instance of Director.
        """
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        self._word.show()
        text = self._word.check_for_win()
        self._terminal_service.write_text(text)
        if self._word.win():
            self._is_playing = False
        elif self._word.loose():
            self._is_playing = False
        elif self._word.loose2():
            self._is_playing = False
        
            # self._is_playing = False
        # elif self._parachutist.loose():
        #     self._is_playing = False