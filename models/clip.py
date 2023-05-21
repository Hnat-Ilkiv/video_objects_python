"""
Author: Hnat Ilkiv IR-15
Date: May 13, 2023
"""

from models.video import Video

class Clip(Video):
    """
    A class that describes a clip.

    Attributes
    ----------
    _singer : str
    _views : int
    _likes : int

    Methods
    -------
    get_current_rating()
    """

    RATING_COEFFICIENT = 10

    def __init__(self, file_name=None, video_name=None, director=None,
                 year=0, singer=None, views=0, likes=0):
        super().__init__(file_name, video_name, director, year)
        self._singer = singer
        self._views = views
        self._likes = likes

    def __repr__(self):
        pass

    def __str__(self):
        return f"{super().__str__()} {self._singer} {self.get_current_rating()}"

    def get_current_rating(self) -> float:
        """
        Method give current rating.

        Parameters
        ----------
        None

        Returns
        -------
        current_rating : float
        """
        return (
            self._likes / self._views * Clip.RATING_COEFFICIENT
            if self._views != 0
            else 0
        )



if __name__ == '__main__':
    clips = [
        Clip(),
        Clip("File", "Clip", "Director", 2000, "Singer",  100, 50)
    ]

    for clip in clips:
        print(clip)
