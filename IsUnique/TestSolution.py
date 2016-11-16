from Solution import check
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_1(self):
        self.assertEqual(check("no idea"), True)
        self.assertEqual(check("no one"), False)

    def test_2(self):
        self.assertEqual(check("hapy new"), True)
        self.assertEqual(check("hapy  new"), False)


if __name__ == '__main__':
    unittest.main()
