def decompose_calculus_line(line: str):
    match line.split(" "):
        case [left_operand, "+", right_operand]:
            print("add")
        case [left_operand, "-", right_operand]:
            print("sub")
        case [left_operand, "*", right_operand]:
            print("mul")
        case [left_operand, "/", right_operand]:
            print("div")
        case _:
            raise Exception(f"Not parseable line -- {line}")


if __name__ == "__main__":
    print("Hello World")
