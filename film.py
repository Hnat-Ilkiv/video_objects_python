class Film:
    """
        My first class
    """

    MIN_MARK_NUMBER = 1
    MAX_MARK_NUMBER = 10
    __instance = None

    def __init__(self, title=None, director=None, year=None, rating=0, marks=0):
        self.__title = title
        self.__director = director
        self.__year = year
        self.__rating = rating
        self.__marks = marks

    def __str__(self):
        return f"Film [Title: {self.__title}, Director: {self.__director}, Year: {self.__year}, Rating: {self.__rating}, Marks: {self.__marks}]"

    @staticmethod
    def get_instance():
        if Film.__instance == None:
            Film.__instance = Film()
        return Film.__instance

    def rate(self, mark):
        if mark <= MIN_MARK_NUMBER:
            self.__rating += MIN_MARK_NUMBER
        elif mark >= MAX_MARK_NUMBER:
            self.__rating += MAX_MARK_NUMBER
        else:
            self.__rating += mark
        self.__marks += 1

    def get_current_rating(self):
       return self.__rating / self.__marks if self.__marks != 0 else 0 

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, director):
        self.__director = director

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating):
        self.__rating = rating

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, marks):
        self.__marks = marks



if __name__ == '__main__':
    films = [
        Film(),
        Film("Film", "Director", 2000, 100, 10),
        Film.get_instance(),
        Film.get_instance()
    ]

for film in films:
    print(film)
