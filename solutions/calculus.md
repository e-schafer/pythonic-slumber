# Calculus -- examinator guide

## filerunner.py
We mainly check if the candidat know how to read a files in python.

## operand.py
We will no try to see if the candidat have all the basics of OOP, but we check if he knows some stuff on python model object.
 
### printing result and operand
When printing the result in the terminal there are two possible solutions
#### niv1
Basically the printable result is done like this. Each time you add a new type you must update this piece of code.
``` python
#class Filerunner in filerunner.py
result = compute(....) # compute return an Operand subclass
if isinstance(operand1, MyTime) or isinstance(operand2, MyTime) :
    print(f"Time({result})")
else 
    print(f"Number({result})")     
```

#### niv2-3
`__repr__` is overriden in order to have the desired printable result. This way, the class handle his own representation.
``` python
#class MyTime in operand.py
def __repr__(self) -> str:
    return (
        f"""Time({time.strftime("%Hh%Mm%Ss", time.gmtime(self.value_as_number))})"""
    )

# class Filerunner.py in filerunner.py
print(compute(...)) # compute return an Operand subclass
```



### MyTime.strtime_to_seconds()

#### niv1
``` python
//TODO
```

#### niv3
``` python
def strtime_to_seconds(self, val: str) -> int:
    """use regex and pattern matching."""

    # This regex use 'named group' inside 'potential group'
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

```


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