from ast import parse
import unittest
from calculus.myparser import MyParser


parser = MyParser()


class MyParser_parse_my_string(unittest.TestCase):
    def test_nominal_case(self):
        input = "Number(999999999999) - Number(232)"
        to_test = parser.parser_my_string(record_line=input)
        assert to_test[0] == "Number(999999999999)"
        assert to_test[1] == "-"
        assert to_test[2] == "Number(232)"

    @unittest.expectedFailure
    def test_missing_operator(self):
        input = "Number(999999999999) Number(232)"
        to_test = parser.parser_my_string(record_line=input)


class MyParser_check_operator(unittest.TestCase):
    def test_nominal_case(self):
        input = "+"
        to_test = parser.check_operator(input)
        assert to_test is True

    def test_wrong_operator(self):
        input = "A"
        to_test = parser.check_operator(input)
        assert to_test is False


if __name__ == "__main__":
    unittest.main()
