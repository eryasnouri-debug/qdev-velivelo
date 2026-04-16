import unittest
from velivelo.location import horsForfait

class TestHorsForfait(unittest.TestCase):
    def testhorsforfaitcas1(self):
        self.assertEqual(horsForfait(60, 90), "SansDepassement")

    def testhorsforfaitcas2(self):
        self.assertEqual(horsForfait(60, 30), "AvecDepassement")

    def testhorsforfaitcas3(self):
        self.assertEqual(horsForfait(241, 380), "Amende")

    def testhorsforfaitcas4(self):
        with self.assertRaises(ValueError):
            horsForfait(0, 30)
