import logging
from functools import wraps
from exceptions.exceptions import NoSuchModeException

def logged(exception, mode="console"):

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except exception as ex:
                if mode == "console":
                    logging.error(ex.log_message)
                elif mode == "file":
                    logging.basicConfig(filename='log.txt',
                                        filemode="a", # w - overwrite | a - add
                                        level=logging.ERROR)
                    logging.error(ex.log_message)
                else:
                    raise NoSuchModeException() from ex
        return wrapper
    return decorator