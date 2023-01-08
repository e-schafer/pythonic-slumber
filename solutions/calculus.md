# Calculus -- examinator guide

## filerunner.py
we mainly check if the candidat know how to read a file in python.

## operand.py
We will no try to see if the candidat have all the basics of OOP, but we check if he knows some stuff on python model object.
 
### MyTime.strtime_to_seconds()

### OperandFactory.build()

#### niv1
``` python
@staticmethod
def build(ope: str) -> Operand:
    """ use if/else """
    list = ope.strip(")").split("(")
    if list.__len__ != 2:
        raise Exception(f"Unparseable operand -- type='{ope}'")
    if list[0] == "Number":
        return MyNumber(list[1])
    elif list[0] == "Time":
        return MyNumber(list[1])
    else:
        raise Exception(f"Unknown operand type -- type='{list[0]}'")
```

#### niv2
```python
@staticmethod
def build(ope: str) -> Operand:
    """ use pattern matching """
    match ope.strip(")").split("("):
        case ["Number", myvalue]:
            return MyNumber(myvalue)
        case ["Time", myvalue]:
            return MyTime(myvalue)
        case [_ as typ, myvalue]:
            raise Exception(f"Unknown operand type -- type='{typ}'")
        case _:
            raise Exception(f"Unparseable operand -- type='{ope}'")
```