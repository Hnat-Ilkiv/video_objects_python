"""
Author: Hnat Ilkiv IR-15
Date: May 13, 2023
"""

from models.video import Video

class Film(Video):
    """
    The class representes a film.

    Attributes
    ----------
    rating : int
        The change saves the sum of all estimates.
    marks : int
        The change preserves the number of grades given.

    Methods
    -------
    rate(mark)
        The method adds a score to the rating and increases the number
        of scores.
    get_current_rating()
        The method calculates and returns the current movie rating.
    """

    MIN_MARK_NUMBER = 1
    MAX_MARK_NUMBER = 10
    __instance = None

    def rate(self, mark : int) -> None:
        """
        The method adds a score to the rating and increases the number
        of scores.

        Parameters
        ----------
        mark : int
            The change preserves the number of grades given.

        Returns
        -------
        None
        """
        if mark <= Film.MIN_MARK_NUMBER:
            self._rating += Film.MIN_MARK_NUMBER
        elif mark >= Film.MAX_MARK_NUMBER:
            self._rating += Film.MAX_MARK_NUMBER
        else:
            self._rating += mark
        self._marks += 1

    def get_current_rating(self) -> float:
        """
        The method calculates and returns the current movie rating.

        Parameters
        ----------
        None

        Returns
        -------
        current_rating : float
            The change is a current assessment of the film.
        """
        return self._rating / self._marks if self._marks != 0 else 0

    def __init__(self, file_name: str = None, video_name: str = None,
                 director: str = None, year: int = 1900, rating: int = 0,
                 marks: int = 0):
        super().__init__(file_name, video_name, director, year)
        self._rating = rating
        self._marks = marks


    def __repr__(self):
        pass

    def __str__(self):
        return f"{super().__str__()} {self.get_current_rating()}"


if __name__ == '__main__':
    films = [
        Film(),
        Film("File" "Film", "Director", 2000, 100, 10)
    ]

    for film in films:
        print(film)
