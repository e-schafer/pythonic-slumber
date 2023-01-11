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
        """
        pass

    # Create a function for formating the data type in string 'Time(12h34m06s)'


class MyNumber(Operand):
    def __init__(self, num_str: str = "", num_float: float = 0) -> None:
        if num_str != "":
            super().__init__(float(num_str))
        else:
            super().__init__(num_float)

    # Create a function for formating the data type in string 'Number(12.9)'


class OperandFactory:
    @staticmethod
    def build(ope: str) -> Operand:
        """Build an operand from a string."""
        pass
