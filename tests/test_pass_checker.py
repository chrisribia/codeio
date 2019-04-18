import unittest
from unittest.mock import patch
from pass_checker.pass_checker import validate_password


class TestValidPassword(unittest.TestCase):

    @patch('pass_checker.pass_checker.get_password', return_value='Chris')
    def test_password_minimum_length(self, input):
        self.assertEqual(
            validate_password(), "INVALID: Password should have minumum of 6 characters and maximum of 12 characters")

    @patch('pass_checker.pass_checker.get_password', return_value='Chris2547@')
    def test_password_maximum_length(self, input):
        self.assertEqual(
            validate_password(), "INVALID: Password should have minumum of 6 characters and maximum of 12 characters")

    @patch('pass_checker.pass_checker.get_password', return_value='CHRIS254@')
    def test_password_lowercase_character(self, input):
        self.assertEqual(
            validate_password(), "INVALID: Password should contain at least a lowercase character")

    @patch('pass_checker.pass_checker.get_password', return_value='CHRISiel@')
    def test_password_should_contain_number(self, input):
        self.assertEqual(
            validate_password(), "INVALID: Password should contain at least a number")

    @patch('pass_checker.pass_checker.get_password', return_value='chris1@')
    def test_password_should_contain_uppercase_character(self, input):
        self.assertEqual(
            validate_password(), "INVALID: Password should contain at least a capital character")

    @patch('pass_checker.pass_checker.get_password', return_value='Chrisl112')
    def test_password_should_contain_special_character(self, input):
        self.assertEqual(
            validate_password(), "INVALID: Password should contain at least a special character")

    @patch('pass_checker.pass_checker.get_password', return_value='Chrs254@#')
    def test_valid_password(self, input):
        self.assertEqual(
            validate_password(), "Your password is VALID")
