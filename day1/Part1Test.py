import unittest
import Part1


class Day1Test(unittest.TestCase):
    def testNoneMatching(self):
        self.assertEqual(Part1.solveCaptcha("1"), 0)
        self.assertEqual(Part1.solveCaptcha("16"), 0)
        self.assertEqual(Part1.solveCaptcha("987654321"), 0)

    def testAllMatching(self):
        self.assertEqual(Part1.solveCaptcha("11"), 2)
        self.assertEqual(Part1.solveCaptcha("1111"), 4)
        self.assertEqual(Part1.solveCaptcha("333"), 9)

    def testOnlyFirstAndLastMatch(self):
        self.assertEqual(Part1.solveCaptcha("11"), 2)
        self.assertEqual(Part1.solveCaptcha("91212129"), 9)
