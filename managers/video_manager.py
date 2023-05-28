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

    Methods
    -------
    add_video(video) -> None
    find_video_by_year(year: int) -> list[Video]
    find_Video_by_current_rating(rating: int) -> list[Video]
    generate_list_current_rating(self) -> list[float]

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

    def generate_list_current_rating(self) -> list[float]:
        """
        With list comprehension, you create a list of the results of executing an arbitrary method from an abstract class for all objects in the manager's list. For example, there is an abstract method do_something(). You need to create a list in which each item is the result of calling do_something() for the corresponding item in the list from the manager.

        Parameters
        ---------
        None

        Returns
        -------
        list_current_rating: list[float]
        """
        return [video.get_current_rating() for video in self]

    def generate_list_indexes_and_elements(self) -> list[{int, Video}]:
        """
        Using the enumerate function, returns a glue from an object and its ordinal number in the list.

        Parameters
        ----------
        None

        Returns
        -------
        list_indexes_and_elements: list[{int, Video}]
        """
        return [[index, video] for index, video in enumerate(self._video_list, start=1)]

    def generate_tuple_object_and_current_rating(self) -> tuple[(Video, float)]:
        """
        Using the zip function, it returns a zip from the object and the result of the generate_list_current_rating(self) method.

        Parameters
        ----------
        None

        Returns
        -------
        list_object_and_current_rating: tuple[(Video, float)]
        """
        return tuple(zip(self._video_list, self.generate_list_current_rating()))

    def generate_dict_all_any(self, value: int) -> dict[str: str]:
        all_year = all(video._year >= value for video in self._video_list)
        any_year = any(video._year >= value for video in self._video_list)
        return {"all": {all_year}, "any": {any_year}}

    def __len__(self):
        return len(self._video_list)

    def __getitem__(self, index):
        return self._video_list[index]

    def __iter__(self):
        for item in self._video_list:
            yield item


if __name__ == "__main__":
    manager = VideoManager()
    manager.add_video(Film())
    manager.add_video(Film(file_name="File", video_name="Film", director="Director", year=2000, rating=100, marks=10))
    manager.add_video(Clip())
    manager.add_video(Clip("File", "Clip", "Director", 2000, "Singer", 100, 50))
