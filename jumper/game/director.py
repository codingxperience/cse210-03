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
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            self._is_playing = False

    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        pass
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        pass
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        self._parachutist.draw_parachutist()
        self._word.draw_word_guess()