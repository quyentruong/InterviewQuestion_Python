from Solution import replace_space
import unittest


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(replace_space("  Mr Bean 2"), "Mr%20Bean%202")
        self.assertEqual(replace_space("  Mr  Super man"), "Mr%20%20Super%20man")


if __name__ == '__main__':
    unittest.main()
