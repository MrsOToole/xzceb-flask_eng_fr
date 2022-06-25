import unittest

from translator import englishToFrench
from translator import frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1e(self):
        self.assertNotEqual(englishToFrench("None"), '')
    def test2e(self):
        self.assertNotEqual(englishToFrench('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    def test1f(self):
        self.assertNotEqual(frenchToEnglish("None"), 'Nul')
    def test2f(self):
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Hello')   

unittest.main()