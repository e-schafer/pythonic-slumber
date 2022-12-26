import itertools
from glob import glob
from operand import MyNumber, MyTime, Operand, OperandFactory


def compute_file():
    path = """E:\\pythonic-slumber\\calculus\\resources"""
    files_list = glob(path + "\\*.txt")
    for file_path in files_list:
        with open(file_path, "r") as file:
            print(f"Reading file -- {file_path}")
            for line in file.readlines():
                print(f"""    {line[0:-1]} -- {decompose_calculus_line(line)}""")


def decompose_calculus_line(line: str):
    match line.strip("\n").split(" "):
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
            result = left_operand() + righ_operand()
        case "-":
            result = left_operand() - righ_operand()
        case "*":
            result = left_operand() * righ_operand()
        case "/":
            result = left_operand() / righ_operand()
        case _:
            raise Exception
    if isinstance(left_operand, MyTime) or isinstance(righ_operand, MyTime):
        return str(MyTime(time_seconds=result))
    else:
        return str(MyNumber(num_float=result))


if __name__ == "__main__":
    print("Hello World")
    compute_file()
