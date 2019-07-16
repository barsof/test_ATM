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
            self.user_can_get_money = False
            print 'jojo'
            return False
        if self.attempts == 0:
            self.user_can_get_money = False
            print 'haha'
            return False
        if pin_code == correct_pin_code:
            self.user_can_get_money = True
            print 'gg'
            return True





tt = InternetBank()

tt.enter_pin_code(33)
