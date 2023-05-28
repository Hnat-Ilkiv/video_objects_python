"""
Author: Hnat Ilkiv IR-15
Date: May 20, 2023
"""

from models.video import Video
from models.film import Film
from models.clip import Clip


class VideoManager:
    """
    Class manage Video's classes.

    Attributes
    ----------
    _video_list: int

    Method
    ------
    add_video(video) -> None:
    find_video_by_year(year: int) -> list[Video]:
    find_Video_by_current_rating(rating: int) -> list[Video]:
    """

    def __init__(self, video_list: list[Video] = []) -> None:
        self._video_list = video_list

    def add_video(self, new_video: Video) -> None:
        """
        Add video object to videos list.

        Parameters
        ----------
        new_video: Video

        Returns
        -------
        None
        """
        self._video_list.append(new_video)

    def find_video_by_year(self, year: int) -> list[Video]:
        """
        Find video by year in video list.

        Parameters
        ----------
        year: int

        Returns
        -------
        find_video_list: list[Video]
        """
        return [new_video for new_video in self._video_list if new_video._year == year]

    def find_video_by_current_rating(self, rating: int) -> list[Video]:
        """
        Find video by year in video list.

        Parameters
        ----------
        rating: int

        Returns
        -------
        find_video_list: list[Video]
        """
        return [video for video in self._video_list if int(video.get_current_rating()) == rating]


if __name__ == "__main__":
    manager = VideoManager()
    manager.add_video(Film())
    manager.add_video(
        Film(file_name="File", video_name="Film", director="Director", year=2000, rating=100, marks=10)
    )
    manager.add_video(Clip())
    manager.add_video(Clip("File", "Clip", "Director", 2000, "Singer", 100, 50))

    for video in manager._video_list:
        print(video)

    for video in manager.find_video_by_year(2000):
        print(video)