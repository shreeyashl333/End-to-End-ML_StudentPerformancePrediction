import sys
import logging
from types import TracebackType
from typing import Optional, Tuple, Type

from src.logger import logging   # your custom logger


def error_message_detail(
    error: Exception,
    error_detail: Tuple[Optional[Type[BaseException]], Optional[BaseException], Optional[TracebackType]]
) -> str:
    """
    Returns a formatted error message with filename, line number, and error details.
    """
    _, _, exc_tb = error_detail
    file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown"
    line_no = exc_tb.tb_lineno if exc_tb else "Unknown"

    return (
        f"Error occurred in script [{file_name}] "
        f"at line [{line_no}] "
        f"with error: [{str(error)}]"
    )


class CustomException(Exception):
    """
    Custom exception class that captures detailed traceback info
    and logs the error automatically.
    """

    def __init__(
        self,
        error: Exception,
        error_detail: Tuple[Optional[Type[BaseException]], Optional[BaseException], Optional[TracebackType]]
    ):
        super().__init__(str(error))  # base exception keeps error string
        self.error_message = error_message_detail(error, error_detail)

        # log the error automatically
        logging.error(self.error_message)

    def __str__(self):
        return self.error_message
