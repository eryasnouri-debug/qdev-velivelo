import unittest
from velivelo.client import pseudoClientConforme

class TestPseudoClientConforme(unittest.TestCase):
    def testcas1valide(self):
        self.assertTrue(pseudoClientConforme("Rob96"))
    def testcas2tropcourt(self):
        self.assertFalse(pseudoClientConforme("Ro"))
    def testcas3troplong(self):   
        self.assertFalse(pseudoClientConforme("Rob96666666"))
    def testcas4pas_demajuscule(self):
        self.assertFalse(pseudoClientConforme("rob96"))
    def testcas5caracterespecial(self):
        self.assertFalse(pseudoClientConforme("Rob96%"))
    def testcas6vide(self):
        with self.assertRaises(ValueError):
            pseudoClientConforme("")
if __name__ == '__main__':
    unittest.main()
