class ATM:
    def __init__(self, balance, bank_charge, amount_to_withdraw, amount):
        self.balance = balance
        self.bank_charge = bank_charge
        self.amount_to_withdraw = amount_to_withdraw
        self.amount = amount

    def calculate(self):
        if amount <= balance:
            print("Releasing cash. Kindly collect!")
            current_balance = float(balance) - float(amount)
            print("Your balance is now: {} upon this withdrawal and bank charge deduction".format(current_balance))
        else:
            print("You need to maintain sufficient balance for the deduction of the bank charges")
            print("Your current balance is: {}".format(balance))


if __name__ == '__main__':
    balance = 10000
    bank_charge = 0.50
    amount_to_withdraw = int(input("Enter the amount you want to withdraw: "))
    if amount_to_withdraw % 5 == 0:
        amount = float(amount_to_withdraw) + float(bank_charge)
        atm_obj = ATM(balance, bank_charge, amount_to_withdraw, amount)
        atm_obj.calculate()
    else:
        print("""This ATM can dispense denomination in multiple of 5 only. 
Please try again based on this displayed information""")
