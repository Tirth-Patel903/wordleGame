import unittest
import test2

class Test_Wordle(unittest.TestCase):
    def test_process(self):
        guess="earth"
        answer="world"
        self.assertEqual(test2.processGuess(guess,answer),False,"test_process Test failed")
    def test_process_same_guess(self):
        guess="earth"
        answer="earth"
        self.assertEqual(test2.processGuess(guess,answer),True,"test_process Test failed")
    def test_process_null_guess(self):
        guess="earth"
        answer=""
        self.assertEqual(test2.processGuess(guess,answer),False,"test_process_null_guess Test Failed")
    def test_process_specialcharacter_guess(self):
        guess="earth"
        answer="*****"
        self.assertEqual(test2.processGuess(guess,answer),False,"test_process_specialcharacter_guess Test Failed")
    def test_verifyGuess_more_length(self):
        guess="earthearth"
        self.assertEqual(test2.verifyGuess(guess),"earth")
    def test_verifyGuess_less_length(self):
        guess="ear"
        self.assertEqual(test2.verifyGuess(guess),"ear")
    def test_verifyGuess_null_string(self):
        self.assertEqual(test2.verifyGuess(""),"")
    def test_verifyGuess_same_string(self):
        guess="earth"
        self.assertEqual(test2.verifyGuess(guess),"earth")
    def test_logicCode(self):
        self.assertEqual(test2.logicCode(),(False,6))
    def test_logicCode(self):
        self.assertEqual(test2.logicCode(),(True,6))
if __name__ == '__main__':
    unittest.main()      
 
