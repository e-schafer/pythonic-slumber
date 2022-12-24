from abc import ABC
import re


class Operand(ABC):
    def __init__(self, myvalue: float):
        self.value_as_number: float = myvalue


class MyTime(Operand):
    def __init__(self, timestr: str):
        super().__init__(self.strtime_to_seconds(timestr))

    @staticmethod
    def strtime_to_seconds(val: str) -> int:
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


class MyNumber(Operand):
    def __init__(self, num: str) -> None:
        super().__init__(float(num))


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
