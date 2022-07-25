import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    def testEmpty(self):
        input = ""
        self.assertFalse(check_pwd(input))

  
if __name__ == "__main__":
    unittest.main(verbosity=2)
