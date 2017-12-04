import unittest

import Part1


class Part1Test(unittest.TestCase):
    def testSingleRow(self):
        self.assertEqual(Part1.calculateChecksum("5\t1\t9\t5"), 8)

    def testMultiRow(self):
        self.assertEqual(Part1.calculateChecksum("5\t1\t9\t5\n"
                                                 "7\t5\t3"), 12)
