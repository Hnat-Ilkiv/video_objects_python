class IncorrectRatingValueExeption(Exception):
    def __init__(self, log_message="Incorrect rating value"):
        self.log_message = log_message

class NoSuchModeException(Exception):
    def __init__(self, log_message="Incorrect rating value"):
        self.log_message = log_message