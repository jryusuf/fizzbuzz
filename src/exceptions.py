import logging


class InvalidRangeException(ValueError):
    """
    Custom exception for invalid range specifications (1-100, start <= end).
    Logs an ERROR message automatically when raised.
    """

    def __init__(self, message: str | None = None):
        default_msg = "Invalid range specified (e.g., outside 1-100 or start > end)."
        final_message = message or default_msg

        logger = logging.getLogger(self.__class__.__module__)
        logger.error(f"{self.__class__.__name__}: {final_message}")

        super().__init__(final_message)


class InvalidInputTypeException(TypeError):
    """
    Custom exception for incorrect input types (e.g., non-integer start/end).
    Logs an ERROR message automatically when raised.
    """

    def __init__(self, message: str | None = None):
        default_msg = "Invalid input type provided (e.g., expected an integer)."
        final_message = message or default_msg

        logger = logging.getLogger(self.__class__.__module__)
        logger.error(f"{self.__class__.__name__}: {final_message}")

        super().__init__(final_message)
