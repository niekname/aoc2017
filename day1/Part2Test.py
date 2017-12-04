import unittest

import Part2


class Part2Test(unittest.TestCase):
    def testNoneMatching(self):
        self.assertEqual(Part2.solveCaptcha("12"), 0)
        self.assertEqual(Part2.solveCaptcha("1221"), 0)

    def testAllMatching(self):
        self.assertEqual(Part2.solveCaptcha("11"), 2)
        self.assertEqual(Part2.solveCaptcha("1111"), 4)
        self.assertEqual(Part2.solveCaptcha("1212"), 6)
        self.assertEqual(Part2.solveCaptcha("123123"), 12)
        self.assertEqual(Part2.solveCaptcha("222222"), 12)

    def testTheMomentOfTruth(self):
        self.assertEqual(Part2.solveCaptcha("123425"), 4)
        self.assertEqual(Part2.solveCaptcha("12131415"), 4)
