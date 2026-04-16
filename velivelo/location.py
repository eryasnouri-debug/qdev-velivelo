import unittest
from velivelo.location import horsForfait

class TestHorsForfait(unittest.TestCase):
    def testhorsforfaitcas1(self):
        self.assertEqual(horsForfait(60, 90), "SansDépassement")

    def testhorsforfaitcas2(self):
        self.assertEqual(horsForfait(60, 30), "AvecDépassement")
