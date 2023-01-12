from glob import glob
from os import path

from calculus.operand import MyNumber, MyTime, Operand, OperandFactory


class Filerunner:
    @staticmethod
    def find_files_and_compute(root_folder_path: str):
        """The point here is to have the list of files"""
        # TODO
        pass

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
            print(f"--------------------------\nReading file -- {file_path}")
            for index, line in enumerate(file.readlines()):
                # remove EOL caracter.
                try:
                    print(
                        f"""    {index+1}:OK    {line[0:-1]} = {Filerunner.decompose_calculus_line(line[0:-1])}"""
                    )
                except Exception as e:
                    print(f"    {index+1}:Error {line[0:-1]}:  {e}")

    @staticmethod
    def decompose_calculus_line(line: str):
        """Decompose your string in operands and operator
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
            case [_, _ as ope, _]:
                raise Exception(f"Unknown operator -- operator='{ope}'")
            case _:
                raise Exception(f"Not parseable line -- line='{line}'")

    @staticmethod
    def compute(left_operand: Operand, righ_operand: Operand, operator: str):
        """Do the magic =D"""
        # TODO
        pass


if __name__ == "__main__":
    print("hello calculus\n--------------------------")
    path = """.\\calculus\\**"""
    Filerunner.find_files_and_compute(path)
