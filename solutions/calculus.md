# Calculus -- examinator guide

## filerunner.py
We mainly check if the candidat know how to find and read a files in python.

### Filerunner.find_files_and_compute
### niv1
The easiest way to find files in a folder is to use the `os.listdir` function. But this function only return files in the current folder. So we must use a recursive function to find files in subfolders.

``` python
@staticmethod
def find_files_and_compute(root_folder_path: str):
    """try to build a recursive function with os.path"""
	files = os.listdir(folder)
	# Python simple foreach syntax.
	for file in files:
		currentFile = path.join(folder, file)
		if (path.isdir(currentFile) and currentFile.endswith(".txt")):
			folderLookup(currentFile)
		else:
			processFile(currentFile)
```

### niv2-3
The `glob` module is the best way to find files in a folder.
The `recursive` parameter is the key to find files in subfolders.

``` python
@staticmethod
def find_files_and_compute(root_folder_path: str):
    """use glob in recursive mode."""
    [
        Filerunner.compute_file(file)
        for file in glob(root_folder_path + "\\*.txt", recursive=True)
    ]

```

---
---
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
---

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

#### niv3
``` python
def build(ope: str) -> Operand:
    """use pattern matching and regex"""
    re_pattern = re.compile("""(?P<type>\\w*)\\((?P<value>.*)\\)""")
    match re_pattern.search(ope):
        case None:
            raise Exception(f"""Unparseable operand -- type='{ope}'""")
        case m:
            match m.groupdict():
                case {"type": "Number", "value": _ as myvalue}:
                    return MyNumber(myvalue)
                case {"type": "Time", "value": _ as myvalue}:
                    return MyTime(myvalue)
                case {"type": _ as typ}:
                    raise Exception(f"""Unknown operand type -- type='{typ}'""")
                case _:
                    raise Exception(f"""Unparseable operand -- type='{ope}'""")
```