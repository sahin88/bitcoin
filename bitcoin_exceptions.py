# -*- coding: utf-8 -*-
"""
Google style docstrings.

Created on 15.04.22

@author: Sahin  Ogur
@company: Satoschi Nakamoto GmbH
"""

from bitcoin_logger import BitCoinLogger


class BitCoinException(BaseException):
    """Bitcoin Custom Exception"""

    def __init__(self, message):
        self.err_msg = message[0]
        self.err_domain = message[1]

    def __str__(self):
        BitCoinLogger().error(self.err_msg)
        return f"{self.err_msg} is occured at {self.err_domain}"
