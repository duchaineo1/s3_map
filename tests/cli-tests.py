import unittest
from unittest.mock import patch
import argparse
import sys


from s3_map.main import parser


class TestArgParser(unittest.TestCase):
    def test_bucket_argument(self):
        test_args = parser.parse_args(["-b", "test-bucket"])
        self.assertEqual(test_args.bucket, "test-bucket")

        test_args = parser.parse_args(["--bucket", "test-bucket"])
        self.assertEqual(test_args.bucket, "test-bucket")

    def test_region_argument(self):
        test_args = parser.parse_args([])
        self.assertFalse(test_args.region)

        test_args = parser.parse_args(["-r"])
        self.assertTrue(test_args.region)

        test_args = parser.parse_args(["--region"])
        self.assertTrue(test_args.region)

    def test_unit_argument(self):
        test_args = parser.parse_args([])
        self.assertEqual(test_args.unit, "b")

        test_args = parser.parse_args(["-u", "mb"])
        self.assertEqual(test_args.unit, "mb")

        test_args = parser.parse_args(["--unit", "gb"])
        self.assertEqual(test_args.unit, "gb")

        with self.assertRaises(SystemExit):
            parser.parse_args(["-u", "invalid"])

    def test_storageclass_argument(self):
        test_args = parser.parse_args([])
        self.assertIsNone(test_args.storageclass)

        test_args = parser.parse_args(["-s", "STANDARD"])
        self.assertEqual(test_args.storageclass, "STANDARD")

        test_args = parser.parse_args(["--storageclass", "STANDARD_IA"])
        self.assertEqual(test_args.storageclass, "STANDARD_IA")

        with self.assertRaises(SystemExit):
            parser.parse_args(["-s", "INVALID"])

    def test_combined_arguments(self):
        test_args = parser.parse_args(
            ["-b", "test-bucket", "-r", "-u", "gb", "-s", "STANDARD"]
        )
        self.assertEqual(test_args.bucket, "test-bucket")
        self.assertTrue(test_args.region)
        self.assertEqual(test_args.unit, "gb")
        self.assertEqual(test_args.storageclass, "STANDARD")


if __name__ == "__main__":
    unittest.main()
