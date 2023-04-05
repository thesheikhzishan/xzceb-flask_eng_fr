import unittest  
  
# First we import the class which we want to test.  
import translator
  
class TestLanguage(unittest.TestCase): 

    def test_englishToFrench(self):
        self.assertEqual(translator.english_to_french('Hello'), "Bonjour")
        self.assertNotEqual(translator.english_to_french('Yes'), "Non")

    def test_frenchToEnglish(self):
        self.assertEqual(translator.french_to_english('Bonjour'), "Hello")
        self.assertNotEqual(translator.french_to_english('Non'), "Yes")

if __name__ == '__main__':
    unittest.main()