import unittest
import test2

class Test_Wordle(unittest.TestCase):

    # function which check word is matched or not
    def test_process(self):
        guess="earth"
        answer="world"
        self.assertEqual(test2.processGuess(guess,answer),False,"test_process Test failed")

    #testing function for same guess
    def test_process_same_guess(self):
        guess="earth"
        answer="earth"
        self.assertEqual(test2.processGuess(guess,answer),True,"test_process Test failed")

    #testing function for null values entered
    def test_process_null_guess(self):
        guess="earth"
        answer=""
        self.assertEqual(test2.processGuess(guess,answer),False,"test_process_null_guess Test Failed")

    #testing for special characters entered
    def test_process_specialcharacter_guess(self):
        guess="earth"
        answer="*****"
        self.assertEqual(test2.processGuess(guess,answer),False,"test_process_specialcharacter_guess Test Failed")

    #testing for guess verifying if is more than 5
    def test_verifyGuess_more_length(self):
        guess="earthearth"
        self.assertEqual(test2.verifyGuess(guess),"earth")

    #testing for guess verifying if is less than 5
    def test_verifyGuess_less_length(self):
        guess="ear"
        self.assertEqual(test2.verifyGuess(guess),"ear")

    #testing for checking null values
    def test_verifyGuess_null_string(self):
        self.assertEqual(test2.verifyGuess(""),"")

    #testing for same num of characters
    def test_verifyGuess_same_string(self):
        guess="earth"
        self.assertEqual(test2.verifyGuess(guess),"earth")

    #In this test only one test will be errorfree both at same time only 1 ran successfully another will give error
    #testing for no guess for all chances and false guess
    def test_logicCode(self):
        self.assertEqual(test2.logicCode(),(False,6))

    #testing for True guess for chances true guesses
    def test_logicCode(self):
        self.assertEqual(test2.logicCode(),(True,6))

if __name__ == '__main__':
    unittest.main()      
 
