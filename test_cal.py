import unittest
import cal


class TestCal(unittest.TestCase):
    def test_add(self):
        print("test add function")
        self.assertEqual(cal.add(15,20),35)


    def test_subtract(self):
        print("test substract function")
        self.assertEqual(cal.subtract(15,10),1)

if __name__ == "__main__":
    unittest.main()