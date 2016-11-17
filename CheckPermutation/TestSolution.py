# Quyen Truong
# 11/16/2016

from Solution import check
import unittest


class MyTestCase(unittest.TestCase):
    def test_same_length(self):
        self.assertEqual(check("dog", "god"), True)
        self.assertEqual(check("Happy", "appHy"), True)

    def test_different_length(self):
        self.assertEqual(check("Dokoko", "kokokodo"), False)
        self.assertEqual(check("Hajimemas", "Hamejimask"), False)

    def test_case_sensitive(self):
        self.assertEqual(check("NEWYEAR", "newyear"), False)
        self.assertEqual(check("HOLIDAY", "dayholi"), False)


if __name__ == '__main__':
    unittest.main()
