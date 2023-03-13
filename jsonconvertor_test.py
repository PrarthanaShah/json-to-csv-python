import unittest
import os
from jsonconverter import *

class MyTestCase(unittest.TestCase):
    def test_convert_json_to_csv_empty_string(self):
        json = {}
        csv = convert_json_to_csv(json)
        self.assertEqual(csv, "")

    def test_convert_json_to_csv_one_column(self):
        json = [{"a":1}, {"a":2}]
        csv= convert_json_to_csv(json)
        self.assertEqual(csv,"a\n1\n2\n")

    def test_convert_json_to_csv_multiple_columns(self):
        json=[{'a':2,'b':4}]
        csv = convert_json_to_csv(json)
        self.assertEqual(csv,"a,b\n2,4\n")

    def test_convert_json_to_csv_missing_columns(self):
        json=[{'a':2,'b':4}, { 'a': 3}]
        csv = convert_json_to_csv(json)
        self.assertEqual(csv,"a,b\n2,4\n3, \n")


if __name__ == '__main__':
    unittest.main()
