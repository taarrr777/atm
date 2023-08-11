import time


# import getpass
class Bank:
    def __init__(self, pwd):
        self.password = pwd

    BankMoney = [20000, 10000, 5000, 1000]
    BankMoneyCount = [30, 50, 70, 100]

    BankValue = 0
    for i in range(len(BankMoney)):
        BankValue += BankMoney[i] * BankMoneyCount[i]

    def ChangePassword(self):

        print("You must change Your Default Password")
        time.sleep(2)

        newPassword = input("Insert New Password: ")
        self.password = newPassword
        print("Password changed Successfully")

    def LogIn(self):
        cardNumber = input("Insert Card Number: ")
        print("Scaning Card...")
        time.sleep(3)
        if len(cardNumber) != 16:
            print("Card Number Invalid")
            quit()
        else:
            # cardPass = getpass.getpass(prompt="Insert Password: ", stream=None)
            cardPass = int(input("Insert Password: "))

            if cardPass == self.password:
                print("Connection...")
                time.sleep(2)
                return 1
        return 0

    def CashOut(self):

        process = self.LogIn()

        UserCash = int(input('Cash: '))
        if process == 1:
            while UserCash >= 1000:
                for i in range(len(self.BankMoney)):
                    if self.BankValue <= UserCash and len(self.BankMoneyCount) == 0:
                        print("Not Enough Money")
                        break
                    elif UserCash == 0 and self.BankValue >= 0:
                        print("Success")
                        break
                    elif UserCash >= self.BankMoney[i]:
                        UserCash -= self.BankMoney[i]
                        self.BankMoneyCount[i] -= 1

                    if self.BankMoneyCount[i] == 0:
                        self.BankMoney.remove(self.BankMoneyCount[i])
                        self.BankMoneyCount.remove(self.BankMoneyCount[i])
            print(self.BankMoneyCount)
        else:
            print("Operation Failed")
        print("Mnac ", UserCash)