import sys

from myparser import MyParser


if __name__ == "__main__":
    print("Hello World")
    test = "Number(999999999999) Number(232)"
    print(MyParser().parser_my_string(test))
