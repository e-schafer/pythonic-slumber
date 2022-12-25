from time import time

from operand import MyNumber, MyTime, Operand, OperandFactory


def decompose_calculus_line(line: str):
    match line.split(" "):
        case [left_operand, ("+" | "-" | "*" | "/") as ope, right_operand]:
            return compute(
                left_operand=OperandFactory.build(left_operand),
                righ_operand=OperandFactory.build(right_operand),
                operator=ope,
            )
        case _:
            raise Exception(f"Not parseable line -- {line}")


def compute(left_operand: Operand, righ_operand: Operand, operator: str):
    result = None
    match operator:
        case "+":
            result = left_operand.value_as_number + righ_operand.value_as_number
        case "-":
            result = left_operand.value_as_number - righ_operand.value_as_number
        case "*":
            result = left_operand.value_as_number * righ_operand.value_as_number
        case "/":
            result = left_operand.value_as_number / righ_operand.value_as_number
        case _:
            raise Exception

    if isinstance(left_operand, MyTime) or isinstance(righ_operand, MyTime):
        return str(MyTime(time_seconds=result))
    else:
        return str(MyNumber(num_float=result))


if __name__ == "__main__":
    print("Hello World")
    val = "Number(43) - Number(1)"
    print(f"{val} -- {decompose_calculus_line(val)}")
    val = "Number(121) / Number(23.9)"
    print(f"{val} -- {decompose_calculus_line(val)}")
    val = "Time(4h50m) - Time(30m)"
    print(f"{val} -- {decompose_calculus_line(val)}")
