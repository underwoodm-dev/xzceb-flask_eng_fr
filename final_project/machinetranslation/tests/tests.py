"""
    Unit Tests for the translator service.
"""
import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """
    Tranlator tests.
    """
    def test_english_to_french_null(self):
        """
        Null test E2F
        """
        self.assertNotEqual(english_to_french(''), None)
    def test_english_to_french_equal(self):
        """
        Equals test E2F
        """
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def test_french_to_english_null(self):
        """
        Null test F2E
        """
        self.assertNotEqual(french_to_english(''), None)
    def test_french_to_english_equal(self):
        """
        Equals test F2E
        """
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()
