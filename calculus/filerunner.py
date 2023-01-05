from calculus.operand import MyNumber, MyTime, Operand, OperandFactory


class Filerunner:
    @staticmethod
    def compute_file(file_path: str):
        """
        ----------------------------------
        niv1: read file without handling exception
        niv2: read file with handling error
        niv3: read file with 'with' instruction
        +1niv: if locate the line in error.
        """
        with open(file_path, "r") as file:
            print(f"Reading file -- {file_path}")
            for index, line in enumerate(file.readlines()):
                # remove EOL caracter.
                try:
                    print(
                        f"""    {line[0:-1]} ==> {Filerunner.decompose_calculus_line(line[0:-1])}"""
                    )
                except Exception as e:
                    print(f"    Error line {index+1}: {e}")

    @staticmethod
    def decompose_calculus_line(line: str):
        """
        ---------------------------------------
        niv1: split on space + if/else
        niv2: regex + if/else
        +1niv: if use pattern matching on result
        """
        # keep strip('\n') to be sure.
        match line.strip("\n").split(" "):
            case [left_operand, ("+" | "-" | "*" | "/") as ope, right_operand]:
                return Filerunner.compute(
                    left_operand=OperandFactory.build(left_operand),
                    righ_operand=OperandFactory.build(right_operand),
                    operator=ope,
                )
            case _:
                raise Exception(f"Not parseable line -- line='{line}'")

    @staticmethod
    def compute(left_operand: Operand, righ_operand: Operand, operator: str):
        """

        -----------------------------------------------
        niv1: use if/else for checking the operator
        niv2: use pattern matching
        +1niv : if check error and use the correct data type on return (time or number)

        """
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
