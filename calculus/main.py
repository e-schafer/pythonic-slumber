import re
from re import Match


def decompose_calculus_line(line: str):
    match line.split(" "):
        case [operand1, "+", operand2]:
            print("add")
        case [operand1, "-", operand2]:
            print("sub")
        case [operand1, "*", operand2]:
            print("mul")
        case [operand1, "/", operand2]:
            print("div")
        case _:
            raise Exception(f"Not parseable line -- {line}")


def decompose_operand(ope: str):
    match ope.strip(")").split("("):
        case ["Number", myvalue]:
            print(f"NUMBER ==> {myvalue}")
        case ["Time", myvalue]:
            print(f"TIME ==> {myvalue}")
        case [x, myvalue]:
            raise Exception(f"Unknown operand type -- type={x}")


def strtime_to_seconds(val: str):
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


if __name__ == "__main__":
    print("Hello World")
    print(strtime_to_seconds("1h"))
