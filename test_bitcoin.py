# -*- coding: utf-8 -*-
"""
Google style docstrings.

Created on 15.04.22

@author: Sahin  Ogur
@company: Satoshi Nakamoto GmbH
"""
from unittest import TestCase
from unittest.mock import patch
from bitcoin import Bitcoin
from bitcoin_exceptions import BitCoinException


class TestBitCoin(TestCase):
    """Test Bitcoin  class """

    def test_sha_256_function_called_once_with_args(self):
        transactions = '''2 BTC is sent to Mark from Andrea'''
        expected_hash = 'a4447b14d580d08fcf4dadbf36f56b67a4153e36ffe05430b321e62e3adca1ea'
        block_number = 5
        prefix_zeros = 4
        previous_hash = ""
        nonce = 0
        with patch.object(Bitcoin, 'sha_256_hash_function', returned_value=expected_hash) as sha_256_hash_function:
            Bitcoin().mine_bitcoin(block_number, transactions, previous_hash, prefix_zeros)
        expected_args = str(block_number) + transactions + previous_hash + str(nonce)
        sha_256_hash_function.assert_called_once_with(expected_args)

    def test_sha_256_function_with_empty_string(self):
        response = Bitcoin().sha_256_hash_function("")
        expected_response = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        self.assertEqual(response, expected_response)

    def test_sha_256_function_with_none_value(self):
        with self.assertRaises(BitCoinException) as error_context:
            Bitcoin().sha_256_hash_function(None)
        self.assertEqual(
            error_context.exception.args[0][0],
            'The type of hashed data could not be None, Integer or Float'
        )
        self.assertEqual(error_context.exception.args[0][1], 'bitcoin.py')

    def test_sha_256_function_with_int_value(self):
        with self.assertRaises(BitCoinException) as error_context:
            Bitcoin().sha_256_hash_function(5)
        self.assertEqual(
            error_context.exception.args[0][0],
            'The type of hashed data could not be None, Integer or Float'
        )
        self.assertEqual(error_context.exception.args[0][1], 'bitcoin.py')

    def test_sha_256_function_with_float_value(self):
        with self.assertRaises(BitCoinException) as error_context:
            Bitcoin().sha_256_hash_function(5.2)
        self.assertEqual(
            error_context.exception.args[0][0],
            'The type of hashed data could not be None, Integer or Float'
        )
        self.assertEqual(error_context.exception.args[0][1], 'bitcoin.py')

    def test_mine_bitcoin_function(self):
        transactions = '''2 BTC is sent to Mark from Andrea'''
        expected_response = '0000d5670392e9f4ef9d2d4fc3b95d123e84fdff6ddbf93bd21b111e0cffeb8f'
        block_number = 5
        prefix_zeros = 4
        previous_hash = ""
        response = Bitcoin().mine_bitcoin(block_number, transactions, previous_hash, prefix_zeros)
        self.assertEqual(response, expected_response)

    def test_mine_bitcoin_function_with_none__transaction(self):
        transactions = None
        block_number = 5
        prefix_zeros = 4
        previous_hash = ""
        with self.assertRaises(BitCoinException) as error_context:
            Bitcoin().mine_bitcoin(block_number, transactions, previous_hash, prefix_zeros)
        self.assertEqual(
            error_context.exception.args[0][0],
            'The mining missing params error'
        )
        self.assertEqual(error_context.exception.args[0][1], 'bitcoin.py')

    def test_mine_bitcoin_function_with_none__block_number(self):
        transactions = 'Satoshi Nakamoto'
        block_number = None
        prefix_zeros = 4
        previous_hash = ""
        with self.assertRaises(BitCoinException) as error_context:
            Bitcoin().mine_bitcoin(block_number, transactions, previous_hash, prefix_zeros)
        self.assertEqual(
            error_context.exception.args[0][0],
            'The mining missing params error'
        )
        self.assertEqual(error_context.exception.args[0][1], 'bitcoin.py')

    def test_mine_bitcoin_function_with_empty_string__block_number(self):
        transactions = 'Satoshi Nakamoto'
        block_number = ''
        prefix_zeros = 4
        previous_hash = ""
        with self.assertRaises(BitCoinException) as error_context:
            Bitcoin().mine_bitcoin(block_number, transactions, previous_hash, prefix_zeros)
        self.assertEqual(
            error_context.exception.args[0][0],
            'The mining missing params error'
        )
        self.assertEqual(error_context.exception.args[0][1], 'bitcoin.py')

    def test_mine_bitcoin_function_with_none__previous_hash(self):
        transactions = 'Satoshi Nakamoto'
        block_number = ''
        prefix_zeros = 4
        previous_hash = None
        with self.assertRaises(BitCoinException) as error_context:
            Bitcoin().mine_bitcoin(block_number, transactions, previous_hash, prefix_zeros)
        self.assertEqual(
            error_context.exception.args[0][0],
            'The mining missing params error'
        )
        self.assertEqual(error_context.exception.args[0][1], 'bitcoin.py')

    def test_mine_bitcoin_function_with_none__prefix_zeros(self):
        transactions = 'Satoshi Nakamoto'
        block_number = ''
        prefix_zeros = None
        previous_hash = ""
        with self.assertRaises(BitCoinException) as error_context:
            Bitcoin().mine_bitcoin(block_number, transactions, previous_hash, prefix_zeros)
        self.assertEqual(
            error_context.exception.args[0][0],
            'The mining missing params error'
        )
        self.assertEqual(error_context.exception.args[0][1], 'bitcoin.py')

    def test_mine_bitcoin_function_with__prefix_zeros__value_is_zero(self):
        transactions = 'Satoshi Nakamoto'
        block_number = 4
        prefix_zeros = 0
        previous_hash = ""
        with self.assertRaises(BitCoinException) as error_context:
            Bitcoin().mine_bitcoin(block_number, transactions, previous_hash, prefix_zeros)
        self.assertEqual(
            error_context.exception.args[0][0],
            'The mining missing params error'
        )
        self.assertEqual(error_context.exception.args[0][1], 'bitcoin.py')

    def test_mine_bitcoin_function_with__max_nonce__is_one(self):
        transactions = 'Satoshi Nakamoto'
        block_number = 2
        prefix_zeros = 6
        previous_hash = ""
        with self.assertRaises(BitCoinException) as error_context:
            bitcoin = Bitcoin()
            bitcoin.max_nonce = 1
            bitcoin.mine_bitcoin(block_number, transactions, previous_hash, prefix_zeros)
        self.assertEqual(
            error_context.exception.args[0][0],
            'The mining not worth it'
        )
        self.assertEqual(error_context.exception.args[0][1], 'bitcoin.py')

    def test_calculate_total_time_to_mine_a_bitcoin(self):
        start_time = 2
        end_time = 4
        response = Bitcoin().calculate_total_time(start_time, end_time)
        self.assertEqual(response, 2)

    def test_calculate_total_time_with_none_value(self):
        start_time = None
        end_time = 4
        response = Bitcoin().calculate_total_time(start_time, end_time)
        self.assertIsNone(response)

    def test_calculate_total_time_with_str_value(self):
        start_time = ''
        end_time = 4
        response = Bitcoin().calculate_total_time(start_time, end_time)
        self.assertIsNone(response)



