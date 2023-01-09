from abc import ABC
import re
import time


class Operand(ABC):
    def __init__(self, myvalue: float):
        self.value_as_number: float = myvalue

    def __call__(self) -> float:
        return self.value_as_number

    def __eq__(self, other) -> bool:
        return self.value_as_number == other.value_as_number


class MyTime(Operand):
    def __init__(self, timestr: str = "", time_seconds: float = 0):
        if timestr != "":
            super().__init__(self.strtime_to_seconds(timestr))
        elif time_seconds >= 0:
            super().__init__(time_seconds)
        else:
            raise Exception(
                f"Invalid argument -- timestr='{timestr}', time_seconds='{time_seconds}'"
            )

    def strtime_to_seconds(self, val: str) -> int:
        """Parse string of time to seconds.
        We need to build our own as the format doesn't comply the norm iso8061.

        val -- time string like '12h123m366s'
        --------------------------------------------
        niv1 : use split on h,m,s and use if elif else to detect each element
        niv2 : use regex to detect elements
        niv3 : use regex and pattern matching
        """
        #
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
        return (
            f"""Time({time.strftime("%Hh%Mm%Ss", time.gmtime(self.value_as_number))})"""
        )


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
        """
        -----------------------
        niv1 : use if/else
        niv2 : use pattern matching
        """
        re_pattern = re.compile("""(?P<type>\\w*)\\((?P<value>.*)\\)""")
        match re_pattern.search(ope):
            case None:
                raise Exception(f"""Unparseable operand -- type='{ope}'""")
            case m:
                match m.groupdict():
                    case {"type": "Number", "value": _ as myvalue}:
                        return MyNumber(myvalue)
                    case {"type": "Time", "value": _ as myvalue}:
                        return MyTime(myvalue)
                    case {"type": _ as typ}:
                        raise Exception(f"""Unknown operand type -- type='{typ}'""")
                    case _:
                        raise Exception(f"""Unparseable operand -- type='{ope}'""")
