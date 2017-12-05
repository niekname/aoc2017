import unittest

import Part2


class Part2Test(unittest.TestCase):
    def testSingleRow(self):
        self.assertEqual(Part2.calculateChecksum("5\t9\t2\t8"), 4)

    def testMultiRow(self):
        self.assertEqual(Part2.calculateChecksum("5\t9\t2\t8\n"
                                                 "9\t4\t7\t3"), 7)
