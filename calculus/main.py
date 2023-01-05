from calculus.filerunner import Filerunner
from glob import glob


print("hello calculus")
path = """.\\calculus\\resources"""
files_list = glob(path + "\\*.txt")
for file in files_list:
    Filerunner.compute_file(file)
