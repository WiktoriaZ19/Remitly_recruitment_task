import unittest
from check_json import check_json_data

class TestCheckJsonData(unittest.TestCase):
    def test_invalid_json_format(self):
        file_path = "invalid_json_format.txt"
        with self.assertRaises(ValueError):
            check_json_data(file_path)

    def test_no_single_asterisk(self):
        file_path = "no_single_asterisk.json"
        self.assertTrue(check_json_data(file_path))

    def test_single_asterisk(self):
        file_path = "single_asterisk.json"
        self.assertFalse(check_json_data(file_path))

    def test_missing_resource(self):
        file_path = "no_resource.json"
        with self.assertRaises(ValueError):
            check_json_data(file_path)

    def test_missing_policy_name(self):
        file_path = "no_policy_name.json"
        with self.assertRaises(ValueError):
            check_json_data(file_path)

    def test_missing_policy_document(self):
        file_path = "no_policy_document.json"
        with self.assertRaises(ValueError):
            check_json_data(file_path)

    def test_invalid_resource_format(self):
        file_path = "invalid_resource_format.json"
        with self.assertRaises(ValueError):
            check_json_data(file_path)

    def test_invalid_statement_format(self):
        file_path = "invalid_statement_format.json"
        with self.assertRaises(ValueError):
            check_json_data(file_path)

if __name__ == '__main__':
    unittest.main()
