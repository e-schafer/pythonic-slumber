"""
Myparser
"""

import re


class MyParser:
    def parser_my_string(self, record_line: str):
        try:
            operand1, operator, operand2 = record_line.split(" ")
            return operand1, operator, operand2
        except Exception as e:
            raise e

    def check_operator(self, op: str):
        return op in ("+", "-", "/", "*")

    def check_operand(self, ope: str):
        try:
            datatype, datavalue = ope.strip(")").split("(")
            return datatype, datavalue
        except Exception as e:
            raise e
