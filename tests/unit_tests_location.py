import unittest
from velivelo.location import horsForfait, Verdict

class TestHorsForfait(unittest.TestCase):
    def testcas1(self):
        self.assertEqual(horsForfait(60, 90), Verdict.SANS_DEPASSEMENT)

    def testcas2(self):
        self.assertEqual(horsForfait(60, 30), Verdict.AVEC_DEPASSEMENT)

    def testcas3(self):
        self.assertEqual(horsForfait(241, 380), Verdict.AMENDE)
    def testcas4(self):
        with self.assertRaises(ValueError):
            horsForfait(0, 30)

if __name__ == '__main__':
    unittest.main()
