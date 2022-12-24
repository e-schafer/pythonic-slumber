import unittest
from calculus.operand import OperandFactory


class OperandFactoryTest(unittest.TestCase):
    def test_build_MyNumber_1(self):
        obj = OperandFactory.build("Number(1)")
        self.assertEquals(obj.value_as_number, 1)

    def test_build_MyNumber_2(self):
        obj = OperandFactory.build("Number(3.14)")
        self.assertEquals(obj.value_as_number, 3.14)

    def test_build_MyNumber_3(self):
        obj = OperandFactory.build("Number(-654.86)")
        self.assertEquals(obj.value_as_number, -654.86)

    def test_build_MyTime_1(self):
        obj = OperandFactory.build("Time(1h)")
        self.assertEquals(obj.value_as_number, 3600)

    def test_build_MyTime_2(self):
        obj = OperandFactory.build("Time(1m20s)")
        self.assertEquals(obj.value_as_number, 80)

    def test_build_MyTime_3(self):
        obj = OperandFactory.build("Time(2m100s)")
        self.assertEquals(obj.value_as_number, 220)
