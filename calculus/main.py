def decompose_calculus_line(line: str):
    match line.split(" "):
        case [operator1, "+", operator2]:
            print("add")
        case [operator1, "-", operator2]:
            print("sub")
        case [operator1, "*", operator2]:
            print("mul")
        case [operator1, "/", operator2]:
            print("div")
        case _:
            print("error")


def decompose_operand(ope: str):
    match ope.strip(")").split("("):
        case ["Number", myvalue]:
            print(f"NUMBER ==> {myvalue}")
        case ["Time", myvalue]:
            print(f"TIME ==> {myvalue}")


if __name__ == "__main__":
    print("Hello World")
    decompose_operand("Time(121)")
