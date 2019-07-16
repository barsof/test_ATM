from exception import *

class InternetBank(object):
    balance = 5000
    pin_code = 333
    attempts = 3
    user_can_get_money = False

    def top_up_money(self, my_money):
        return self.balance + my_money


    def enter_pin_code(self,pin_code):
        correct_pin_code = 333
        if pin_code != correct_pin_code:
            self.attempts -= 1
            print 'jojo'
            return False
        if self.attempts == 0:
            print 'haha'
            raise AttempOver

        if pin_code == correct_pin_code:
            self.user_can_get_money = True
            print 'gg'
            return True

    def cash_back_money(self,back_money):
        if self.user_can_get_money :
            if back_money <= self.balance:
                print 'U can take', back_money, 'money'
                self.balance = self.balance - back_money
                return back_money
            else:
                return 'U have not enough money'


    # def check_acc_status (self, want_check):
    #     if self.user_can_get_money:
    #         if want_check==True:
    #             return self.balance

    def check_acc_status (self):
        if self.user_can_get_money:
                return self.balance
        else:
            raise EnterPin


##tt = InternetBank()

# tt.enter_pin_code(333)
# tt.cash_back_money(4999)
# print tt.cash_back_money(2000)


