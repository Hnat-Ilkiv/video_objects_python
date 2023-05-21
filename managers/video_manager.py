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
    """
    def __init__(self, video_list: list[Video] = []) -> None:
        self._video_list = video_list

    def add_video(self, video) -> None:
        self._video_list.append(video)

    def find_video_by_year(self, year: int) -> list[Video]:
        return [video for video in self._video_list if video._year == year]

    def find_video_by_current_rating(self, rating: int) -> list[Video]:
        return [video for video in self._video_list if int(video.get_current_rating()) == rating]

if __name__ == "__main__":
    manager = VideoManager()
    manager.add_video(Film())
    manager.add_video(Film("File" "Film", "Director", 2000, 100, 10))
    manager.add_video(Clip())
    manager.add_video(Clip("File", "Clip", "Director", 2000, "Singer",  100, 50))

    for video in manager._video_list:
        print(video)

    for video in manager.find_video_by_year(2000):
        print(video)