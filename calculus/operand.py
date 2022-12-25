from abc import ABC
from os import times_result
import re
from datetime import timedelta


class Operand(ABC):
    def __init__(self, myvalue: float):
        self.value_as_number: float = myvalue


class MyTime(Operand):
    def __init__(self, timestr: str = "", time_seconds: float = 0):
        if timestr != "":
            super().__init__(self.strtime_to_seconds(timestr))
        else:
            super().__init__(time_seconds)

    def strtime_to_seconds(self, val: str) -> int:
        re_pattern = re.compile(
            """((?P<hours>\\d*)h)?((?P<minutes>\\d*)m)?((?P<seconds>\\d*)s)?"""
        )
        match re_pattern.search(val):
            case None:
                raise Exception(f"Time value not parseable -- value={val}")
            case m:
                return (
                    int(m.group("hours") if m.group("hours") else "0") * 3600
                    + int(m.group("minutes") if m.group("minutes") else "0") * 60
                    + int(m.group("seconds") if m.group("seconds") else "0")
                )

    def __repr__(self) -> str:
        return f"Time({timedelta(seconds=self.value_as_number)})"


class MyNumber(Operand):
    def __init__(self, num_str: str = "", num_float: float = 0) -> None:
        if num_str != "":
            super().__init__(float(num_str))
        else:
            super().__init__(num_float)

    def __repr__(self) -> str:
        return f"Number({self.value_as_number})"


class OperandFactory:
    @staticmethod
    def build(ope: str) -> Operand:
        match ope.strip(")").split("("):
            case ["Number", myvalue]:
                return MyNumber(myvalue)
            case ["Time", myvalue]:
                return MyTime(myvalue)
            case _:
                raise Exception(f"Unknown operand type -- type={ope}")
