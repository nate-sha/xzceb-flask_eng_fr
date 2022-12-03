import unittest
from machinetranslation import translator


class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        # Test for null input
        self.assertEqual(translator.english_to_french(""), "")
        # Test translating a simple phrase from English to French
        self.assertEqual(translator.english_to_french("Hello"), "Bonjour")

    def test_french_to_english(self):
        # Test for null input
        self.assertEqual(translator.french_to_english(""), "")
        # Test translating a simple phrase from French to English
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello")


if __name__ == "__main__":
    unittest.main()
