"""
Author: Vaughn Al-Duane Pinnock
Task: class Director
"""

from game.terminal_service import TerminalService
from game.word import Word
from game.parachutist import Parachutist

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
        self._is_playing = True
        self._parachutist = Parachutist()
        self._word = Word()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self.lives = 5
        self._is_playing = True
        while self._is_playing:
            self._do_updates()
            self._do_outputs()
            self._get_inputs()
            self.lives -= 1
            if self.lives == 0:
                self._is_playing = False
            self._is_playing = True

    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        guess = self._terminal_service.read_text("\nEnter your guess[a - z]: ")
        self._word.check_guess(guess)
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        self._word.check_for_win()
        self._parachutist.parachute_gone()

    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        self._parachutist.draw_parachutist()
        self._word.show()