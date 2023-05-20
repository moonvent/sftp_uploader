"""
    Create a logger for package
"""


from abc import ABC
import logging

from sftp_uploader.constants.applications.logs import LOGGING_FORMAT


logging.basicConfig(level=logging.INFO,
                    format=LOGGING_FORMAT)


class CustomLogger(ABC):
    """
        Custom class for logging in other classes
        
        Attributes:
            logger (logging.Logger): object logger
    """
    logger: logging.Logger = None

    def __init__(self, 
                 logger_name: str) -> None:
        self.logger = logging.getLogger(logger_name)
        
