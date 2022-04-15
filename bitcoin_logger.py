# -*- coding: utf-8 -*-
"""
Google style docstrings.

Created on 15.04.22

@author: Sahin Ogur
@company: Satoschi Nakamoto GmbH
"""
import logging
from bitcoin_logger_config import FILE_NAME


class BitCoinLogger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(
            filename=FILE_NAME,
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

    def warning(self, message):
        """
        Write warn message to log file

        Args:
           message(str): Warning message

        Returns:
            Warning logger

        """
        return self.logger.warning(message)

    def debug(self, message):
        """
        Write debug message to log file

        Args:
           message(str): Debug message

        Returns:
            Debug logger

        """
        return self.logger.debug(message)

    def info(self, message):
        """
        Write info message to log file

        Args:
           message(str): Info message

        Returns:
            Info logger

        """
        return self.logger.info(message)

    def error(self, message):
        """
        Write error message to log file

        Args:
           message(str): Error message

        Returns:
            Error logger

        """
        return self.logger.error(message)
