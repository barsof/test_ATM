import unittest
from test42 import *

class TestInternetBank(unittest.TestCase):
    def setUp(self):
        self.terminal = InternetBank()
        self.terminal.enter_pin_code(333)

#    def test_top_up_account(self):
#        my_money = self.terminal.top_up_money(5000)
#        self.assertEqual(my_money, 10000)

    # def test_top_up_account_0(self):
    #      my_money = self.terminal.top_up_money(0)
    #      self.assertEqual(my_money, 5000)




#    def test_top_up_account_mines_5000(self):
#         my_money = self.terminal.top_up_money(-5000)
#         self.assertEqual(my_money, 0)

    #
    # def test_top_up_account_mines_1(self):
    #      my_money = self.terminal.top_up_money('d')
    #      self.assertEqual(my_money, 5000)


    # def test_minus_sum(self):
    #     #this test should be down //Ahmed
    #     minus_sum = self.terminal.top_up_money(0)
    #     self.assertEqual(minus_sum, 5000)




#    def test_top_up_account_not(self):
#        my_money = self.terminal.top_up_money(5000)
#        self.assertNotEqual(my_money, 10000)

#    def test_correct_pin_code(self):
#        self.assertTrue(self.terminal.enter_pin_code(333))


#    def test_enter_pin_code (self):
#        incorrect_attempt = self.terminal.enter_pin_code(222)
#        self.assertEqual(self.terminal.attempts, 2)

#    def test_enter_pin_code_2 (self):
#        incorrect_attempt = self.terminal.enter_pin_code(222)
#        incorrect_attempt2 = self.terminal.enter_pin_code(222)
#        self.assertEqual(self.terminal.attempts, 1)

#    def test_enter_pin_code_3 (self):
#         incorrect_attempt = self.terminal.enter_pin_code(222)
#         incorrect_attempt2 = self.terminal.enter_pin_code(222)
#         incorrect_attempt3 = self.terminal.enter_pin_code(222)
#         self.assertEqual(self.terminal.attempts, 0)
#         self.assertTrue(self.terminal.user_can_get_money)

    # def test_balance_cash_back_money_5000(self):
    #     is_cash = self.terminal.cash_back_money(5000)
    #     self.assertEqual(self.terminal.balance, 0)

    # def test_balance_cash_back_money_5001(self):
    #     is_cash = self.terminal.cash_back_money(5001)
    #     self.assertEqual(self.terminal.balance, 5000)

#should be down
    # def test_balance_cash_back_money_4999(self):
    #     is_cash = self.terminal.cash_back_money(4999)
    #     self.assertEqual(self.terminal.balance, 1)



    # def test_balance_cash_back_money__1(self):
    #     is_cash = self.terminal.cash_back_money(-1)
    #     self.assertEqual(self.terminal.balance, 5001)

    # should be down
    # def test_balance_cash_back_money__1(self):
    #     is_cash = self.terminal.cash_back_money(-2)
    #     self.assertEqual(self.terminal.balance, 5002)

#should be no give cash
    # def test_balance_cash_back_money__1(self):
    #     is_cash = self.terminal.cash_back_money(0)
    #     self.assertEqual(self.terminal.balance, 5000)


    # def test_cash_back_money_4000(self):
    #     is_cash = self.terminal.cash_back_money(4000)
    #     self.assertEqual(is_cash, 4000)

    # def test_cash_back_money_5001(self):
    #     is_cash = self.terminal.cash_back_money(5001)
    #     self.assertEqual(is_cash, 5001)

    # #test  account status positive
    # def test_check_acc_status(self):
    #     yes_check = self.terminal.check_acc_status(True)
    #     self.assertEqual(yes_check,5000)

    # test  account status negative
    # def test_check_acc_status_neg(self):
    #     yes_check = self.terminal.check_acc_status(False)
    #     self.assertNotEqual(yes_check,5000)


    #test  account status positive ahmed
    def test_check_acc_status(self):
        enter_pin = self.terminal.enter_pin_code(333)
        self.assertTrue(self.terminal.check_acc_status())
        self.assertEqual(self.terminal.balance, 5000)

    def test_check_acc_status_neg(self):
        enter_pin = self.terminal.enter_pin_code(11)
        self.assertRaises(Exception)


#    def test_enter_pin_code_not(self):
#        my_pin_code = self.terminal.enter_pin_code(222)
#        self.assertNotEqual(my_pin_code, 333)


