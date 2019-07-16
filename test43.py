import unittest
from test42 import *

class TestInternetBankk(unittest.TestCase):
    def setUp(self):
        self.terminal = InternetBank()
        self.terminal.enter_pin_code(333)

#    def test_top_up_account(self):
#        my_money = self.terminal.top_up_money(5000)
#        self.assertEqual(my_money, 10000)


#    def test_top_up_account_not(self):
#        my_money = self.terminal.top_up_money(5000)
#        self.assertNotEqual(my_money, 10000)


#    def test_enter_pin_code (self):
#        incorrect_attempt = self.terminal.enter_pin_code(222)
#        self.assertEqual(self.terminal.attempts, 2)

    def test_enter_pin_code_2 (self):
        incorrect_attempt = self.terminal.enter_pin_code(222)
        incorrect_attempt2 = self.terminal.enter_pin_code(222)
        self.assertEqual(self.terminal.attempts, 1)

     def test_enter_pin_code_3 (self):
         incorrect_attempt = self.terminal.enter_pin_code(222)
         incorrect_attempt2 = self.terminal.enter_pin_code(222)
         incorrect_attempt3 = self.terminal.enter_pin_code(222)
         self.assertEqual(self.terminal.attempts, 0)



#    def test_enter_pin_code_not(self):
#        my_pin_code = self.terminal.enter_pin_code(222)
#        self.assertNotEqual(my_pin_code, 333)
