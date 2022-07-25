import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    def testEmpty(self):
        input = ""
        self.assertFalse(check_pwd(input))

    def testLen7(self):
        input = "1111144"
        self.assertFalse(check_pwd(input))

    def testNoLower(self):
        input = "111117777"
        self.assertFalse(check_pwd(input))

    def testNoUpper(self):
        input = "747477h7"
        self.assertFalse(check_pwd(input))

    def testNoDigit(self):
        input = "Uhhhhdgd"
        self.assertFalse(check_pwd(input))

if __name__ == "__main__":
    unittest.main(verbosity=2)
