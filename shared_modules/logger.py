import functools
from enum import Enum


class log_level(Enum):
    all = 1
    trace = 2
    debug = 3
    info = 4
    warning = 5
    error = 6


class Logger:
    def __init__(self, level: log_level = log_level.all) -> None:
        self.level = level

    # Used to log entrance and exits of functions
    def log_trace(self, message: str) -> None:
        self.__log(log_level.trace, "TRACE: " + message)

    # Used to log normal program execution
    def log_debug(self, message: str) -> None:
        self.__log(log_level.trace, "DEBUG: " + message)

    # Used to log non-happy path/optional scenarios
    def log_info(self, message: str) -> None:
        self.__log(log_level.trace, "INFO:  " + message)

    # Used to log non desirable situations that either do not cause execution failure or were handled
    def log_warning(self, message: str) -> None:
        self.__log(log_level.trace, "WARN:  " + message)

    # Used to log any error that causes execution fail
    def log_error(self, message: str) -> None:
        self.__log(log_level.trace, "ERR:   " + message)

    def __log(self, level: log_level, message: str) -> None:
        if level.value >= self.level.value:
            print(message)


# Sets the logger level for everything
logger = Logger(log_level.all)


def get_logger() -> Logger:
    return logger


def trace_logging():
    def print_objects(args) -> str:
        result = ""
        for each in args:
            result += print_object(each) + ", "
        return result

    def print_object(obj) -> str:
        try:
            result = "{ "
            for key, value in vars(obj).items():
                result += key + ":" + value
            result += "}"
            return result
        except TypeError:
            return str(obj)

    def error_log(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            get_logger().log_trace("Entering function '" + func.__name__ + "' with " + print_objects(args))
            result = func(*args, **kwargs)
            get_logger().log_trace("Exiting function  '" + func.__name__ + "' with " + print_object(result))
            return result

        return wrapper

    return error_log


