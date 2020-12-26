import unittest

import pytest

from aoc2020.day_2.day_two import validate_password_database

sample_pasword_database = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""


class TestPasswordDatabase(unittest.TestCase):

    def test_validate_password_database(self):
        res = validate_password_database(sample_pasword_database, toboggan_style=False)
        expected = [
            {'lower_limit': '1', 'upper_limit': '3', 'letter': 'a', 'password': 'abcde'},
            {'lower_limit': '2', 'upper_limit': '9', 'letter': 'c', 'password': 'ccccccccc'},
        ]
        self.assertListEqual(expected, res)
        res = validate_password_database(sample_pasword_database, toboggan_style=True)
        expected = [
            {'lower_limit': '1', 'upper_limit': '3', 'letter': 'a', 'password': 'abcde'},
        ]
        self.assertListEqual(expected, res)


if __name__ == '__main__':
    print("Day 2")
    pytest.main()
