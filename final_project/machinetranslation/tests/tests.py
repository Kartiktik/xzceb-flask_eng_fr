import unittest
from translator import english_to_french,french_to_english

class Test_english_to_french(unittest.TestCase):
    def test1(self):
        self.assertIsNone(english_to_french(None))
        self.assertIsNone(english_to_french(1234))
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertNotEquals(english_to_french("Bonjour"),"Hello")
        
class Test_french_to_english(unittest.TestCase):
    def test1(self):
        self.assertIsNone(french_to_english(None))
        self.assertIsNone(french_to_english(1234))
        self.assertNotEquals(french_to_english("Hello"),"Bonjour")
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        
unittest.main()
