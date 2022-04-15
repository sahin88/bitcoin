# -*- coding: utf-8 -*-
"""
Google style docstrings.

Created on 15.04.22

@author: Sahin Ogur
@company: Satoschi Nakamoto GmbH
"""

import time
from hashlib import sha256
from bitcoin_error import MINING_NOT_WORTH_ERROR, TYPE_ERROR, MINING_MISSING_PARAMS_ERROR
from bitcoin_exceptions import BitCoinException
from bitcoin_logger import BitCoinLogger


class Bitcoin:
    """Creating blockchain"""

    def __init__(self):
        self.max_nonce = 100**5

    def sha_256_hash_function(self, text):
        """
        Hash the text

        Args:
            text(str): Text to be encrypted or hashed

        Raises:
            BitcoinException: If the  text args is None

        Returns:
            Hashed data

        """
        if text is None or isinstance(text, int) or isinstance(text, float):
            raise BitCoinException(TYPE_ERROR)

        return sha256(text.encode('ascii')).hexdigest()

    def mine_bitcoin(self, _block_number, _transactions, _previous_hash, _prefix_zeros):
        """
        Mine Bitcoin

        Args:
            _block_number(int): Block number
            _transactions(str): Transactions
            _previous_hash(str): Previous Hash
            _prefix_zeros(int): Number of the zeros the hashed text  should startswith

        Returns:
            Hashed data, If the number of trials is under the threshold.

        Raises:
            BitcoinException:if the number of trials is over threshold(max_nonce) or missing params

        """
        if not _block_number or _transactions is None or _previous_hash is None or not _prefix_zeros:
            raise BitCoinException(MINING_MISSING_PARAMS_ERROR)

        start_time = time.time()
        BitCoinLogger().info(
            "Mining is started with block number of {}, previous_hash of  ".format(
                _block_number, _previous_hash
            )
        )
        expected_prefix_str = '0' * _prefix_zeros
        for nonce in range(self.max_nonce):
            text_to_be_hashed = str(_block_number) + _transactions + _previous_hash + str(nonce)
            hashed_data = self.sha_256_hash_function(text_to_be_hashed)
            if hashed_data.startswith(expected_prefix_str):
                end_time = time.time()
                BitCoinLogger().info(
                    "Mining is completed successfully in {} seconds with the hash of {}".format(
                        self.calculate_total_time(start_time, end_time),
                        hashed_data
                    )
                )
                return hashed_data

        raise BitCoinException(MINING_NOT_WORTH_ERROR)

    def calculate_total_time(self, start_time, end_time):
        """
        Calculate time to mine the bitcoin

        Args:
            start_time(float): Unix time, at which calculation is started
            end_time(float): Unix time, at which calculation is ended

          Returns:
              float. Time difference in seconds.

          """
        if not isinstance(start_time, str) and not isinstance(end_time, str) \
                and start_time is not None and end_time is not None:
            return end_time - start_time


if __name__ == '__main__':
    transactions = ''' 
    2 BTC is sent to Mark from Andrea
    '''
    previous_hash = 'a4447b14d580d08fcf4dadbf36f56b67a4153e36ffe05430b321e62e3adca1ea'
    block_number = 5
    prefix_zeros = 6

    print(Bitcoin().mine_bitcoin(block_number, transactions, previous_hash, prefix_zeros))
