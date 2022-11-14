import unittest
import chatbotClasses as cb
from chatbotClasses import Response as rp

class TestBot(unittest.TestCase):
    def test_validate(self):
        self.assertEqual(cb.ReadInput.read("damn"), "Invalid Input")

    def test_HOW_I_AM_response(self):
        self.assertIn(cb.ReadInput.read("how are you?").removeprefix(cb.ReadInput.USERNAME + ": "),rp.HOW_I_AM)
        self.assertNotIn(cb.ReadInput.read("I climb v2, how about you?").removeprefix(cb.ReadInput.USERNAME + ": "),rp.HOW_I_AM)

    def test_probability(self):
        self.assertEqual(cb.InputAnalysis.probability(["what", "kind", "of", "shoes", "do", "you", "wear"],recognizedWords=["what", "kind", "type", "of", "shoes", "do", "you", "have", "wear"],requiredWords=["shoes"]),int(7/9*100))

if __name__=="__main__":
    unittest.main()