from abc import ABC
from datetime import datetime

class Operand(ABC):
    def __init__(self) -> None:
        self.value_as_int = 0  


class MyTime(Operand):
    def __init__(self, time:str) -> None:
        time_in_second = datetime.fromisoformat
        super().__init__()

class MyNumber(Operand):
    def __init__(self) -> None:
        super().__init__()

class OperandFactory():
    @staticmethod
    def build(datatype:str, datavalue:str):
        pass
