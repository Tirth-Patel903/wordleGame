import unittest
from wordle import WordleGame

class Test_Wordle(unittest.TestCase):

    # function which check word is matched or not
    def test_process(self):
        guess="earth"
        answer="world"
        self.assertEqual(WordleGame.processGuess(self,guess,answer),False,"test_process Test failed")

    #testing function for same guess
    def test_process_same_guess(self):
        guess="earth"
        answer="earth"
        self.assertEqual(WordleGame.processGuess(self,guess,answer),True,"test_process Test failed")

    #testing function for null values entered
    def test_process_null_guess(self):
        guess="earth"
        answer=""
        self.assertEqual(WordleGame.processGuess(self,guess,answer),False,"test_process_null_guess Test Failed")

    #testing for special characters entered
    def test_process_specialcharacter_guess(self):
        guess="earth"
        answer="*****"
        self.assertEqual(WordleGame.processGuess(self,guess,answer),False,"test_process_specialcharacter_guess Test Failed")

    #testing for guess verifying if is more than 5
    def test_verifyGuess_more_length(self):
        guess="earthearth"
        self.assertEqual(WordleGame.verifyGuess(self,guess),"earth","Test failed for length is more than 5.")

    #testing for guess verifying if is less than 5
    def test_verifyGuess_less_length(self):
        guess="ear"
        self.assertEqual(WordleGame.verifyGuess(self,guess),"ear","Test Failed for lenght is less than 5.")

    #testing for checking null values
    def test_verifyGuess_null_string(self):
        self.assertEqual(WordleGame.verifyGuess(self,""),"","Test Failed for same length.")

    #testing for same num of characters
    def test_verifyGuess_same_string(self):
        guess="earth"
        self.assertEqual(WordleGame.verifyGuess(self,guess),"earth","Test Failed for same num of characters")

    #In this test only one test will be errorfree both at same time only 1 ran successfully another will give error
    #testing for no guess for all chances and false guess
    def test_logicCode(self):
        self.assertEqual(WordleGame.logicCode(self),(False,6),"Test failed for wrong guess")

    #testing for True guess for chances true guesses
    def test_logicCode(self):
        self.assertEqual(WordleGame.logicCode(self),(True,6),"Test failed for right guess")

if __name__ == '__main__':
    unittest.main() 
