import unittest
from calculus.operand import MyTime, MyNumber
from calculus.filerunner import Filerunner


class FilerunnerTest(unittest.TestCase):
    def test_compute_add_1(self):
        self.assertEqual(
            Filerunner.compute(MyTime("1m20s"), MyTime("1m20s"), "+"),
            MyTime(timestr="00h02m40s"),
        )

    def test_compute_add_2(self):
        self.assertEqual(
            Filerunner.compute(MyNumber("10"), MyNumber("15"), "+"),
            MyNumber(num_float=25.0),
        )

    def test_compute_add_3(self):
        self.assertEqual(
            Filerunner.compute(MyNumber("5"), MyTime("1m20s"), "+"),
            MyTime(timestr="00h01m25s"),
        )

    def test_compute_add_4(self):
        self.assertEqual(
            Filerunner.compute(MyTime("1m20s"), MyNumber("10"), "+"),
            MyTime(timestr="00h01m30s"),
        )

    def test_compute_sub_1(self):
        self.assertEqual(
            Filerunner.compute(MyTime("1m20s"), MyTime("1m"), "-"),
            MyTime(timestr="00h00m20s"),
        )

    def test_compute_sub_2(self):
        self.assertEqual(
            Filerunner.compute(MyNumber("10"), MyNumber("15"), "-"),
            MyNumber(num_float=-5.0),
        )

    @unittest.expectedFailure
    def test_compute_sub_3(self):
        self.assertEqual(
            Filerunner.compute(MyNumber("5"), MyTime("1m20s"), "-"),
            MyTime(timestr="23h58m45s"),
        )

    def test_compute_sub_4(self):
        self.assertEqual(
            Filerunner.compute(MyTime("1m20s"), MyNumber("10"), "-"),
            MyTime(timestr="00h01m10s"),
        )


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(FilerunnerTest())
