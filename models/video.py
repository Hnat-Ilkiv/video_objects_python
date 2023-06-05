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

    def __repr__(self):
        return f"file_name={self._file_name} video_title={self._video_title} director={self._director} year={self._year}"

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

    def get_attributes_by_type(self,data_type: type) -> dict:
        """
        Using dict comprehension and the __dict__ magic method, it
        returns a dictionary with all the keys and values of the
        object's attributes. Also, keys and values need to be returned
        only for a certain type of value data (the type is passed as
        an argument). For example, if a method takes an int type, then
        you should return all attributes that have values of the int 
        data type. This method will be in an abstract class (but will
        not be abstract).

        Parameters
        ----------
        data_type: type

        Returns
        -------
        attributes_by_type: dict
        """
        if data_type is None:
            return self.__dict__
        return {
            key: value
            for key, value in self.__dict__.items()
            if isinstance(value, data_type)
        }
