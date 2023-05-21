"""
Author: Hnat Ilkiv IR-15
Date: May 20, 2023
"""

from abc import ABC, abstractmethod

class Video(ABC):
    """
    This is an abstract Video class. It stores basic information about
    video files and provides an abstract method that determines the
    current rating.

    Attributes
    ----------
    _file_name : str
    _videl_name : str
    _director : str
    _year : int

    Method
    ------
    get_current_rating()
    """

    def __init__(self, file_name: str, video_title: str,
                 director: str, year: int) -> None:
        self._file_name = file_name
        self._video_title = video_title
        self._director = director
        self._year = year

    def __str__(self):
        return f"{self._video_title} {self._director} {self._year}"

    @abstractmethod
    def get_current_rating(self) -> float:
        """
        This is an abstract method that returns the current movie
        rating and calculates its dependencies on how the descendants
        determine it.

        Parameters
        ----------
        None

        Returns
        -------
        current_rating : float
        """
