import unittest
import chatbotClasses as cb
from chatbotClasses import Response as rp

class TestBot(unittest.TestCase):
    def test_validate(self):
        self.assertEqual(cb.ReadInput.read("damn"), "Invalid Input")

    def test_HOW_I_AM_response(self):
        self.assertIn(cb.ReadInput.read("how are you?").removeprefix(cb.ReadInput.USERNAME + ": "),rp.HOW_I_AM)
        self.assertNotIn(cb.ReadInput.read("I climb v2, how about you?").removeprefix(cb.ReadInput.USERNAME + ": "),rp.HOW_I_AM)

if __name__=="__main__":
    unittest.main()