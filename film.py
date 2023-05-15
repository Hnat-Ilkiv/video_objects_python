"""
Author: Hnat Ilkiv IR-15
Date: May 13, 2023
"""
class Film:
    """
    The class representes a film.

    Attributes
    ----------
    title : str
        The change retains the name of the film.
    director : str
        The change retains the director's name.
    year : int
        The change preserves the year of the movie's release.
    rating : int
        The change saves the sum of all estimates.
    marks : int
        The change preserves the number of grades given.

    Methods
    -------
    get_instance()
        The method returns an instance of the Film object.
    rate(mark)
        The method adds a score to the rating and increases the number
        of scores.
    get_current_rating()
        The method calculates and returns the current movie rating.
    """

    MIN_MARK_NUMBER = 1
    MAX_MARK_NUMBER = 10
    __instance = None



    @classmethod
    def get_instance(cls):
        """
        The method returns an instance of the Film object.

        Parameters
        ----------
        None

        Returns
        -------
        obj_film : Film
            The shift is an object of the Film class.
        """
        if cls.__instance is None:
            cls.__instance = Film()
        return cls.__instance

    def rate(self, mark):
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
            self.rating += Film.MIN_MARK_NUMBER
        elif mark >= Film.MAX_MARK_NUMBER:
            self.rating += Film.MAX_MARK_NUMBER
        else:
            self.rating += mark
        self.marks += 1

    def get_current_rating(self):
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
        return self.rating / self.marks if self.marks != 0 else 0

    def __init__(self, title=None, director=None,
                 year=None, rating=0, marks=0):
        self.title = title
        self.director = director
        self.year = year
        self.rating = rating
        self.marks = marks


    def __repr__(self):
        return (
            f"{self.__class__.__name__} = ["
            f"Title: {self.title}, "
            f"Director: {self.director}, "
            f"Year: {self.year}, "
            f"Rating: {self.rating}, "
            f"Marks: {self.rating}]"
        )

    def __str__(self):
        return f"{self.title}, {self.director}, {self.year}"



if __name__ == '__main__':
    films = [
        Film(),
        Film("Film", "Director", 2000, 100, 10),
        Film.get_instance(),
        Film.get_instance()
    ]

    for film in films:
        print(film)
