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

        print("Do you want to change your password?")
        time.sleep(1)
        validation = input("y/n: ")
        if validation == "y":
            newPassword = int(input("Insert New Password: "))
            self.password = newPassword
            print("Password changed Successfully")
        elif validation == "n":
            print("The operation was cancelled")
        else:
            print("Incorrect data")
        return self.password

    def LogIn(self):
        cardNumber = input("Insert Card Number: ")
        print("Scaning Card...")
        time.sleep(2)
        if len(cardNumber) != 16:
            print("Card Number Invalid")
            quit()
        else:
            # cardPass = getpass.getpass(prompt="Insert Password: ", stream=None)
            cardPass = int(input("Insert Password: "))

            if cardPass == self.password:
                print("Connection...")
                time.sleep(1)
                return 1
        return 0

    def CashOut(self):
        process = self.LogIn()

        if process == 1:
            UserCash = int(input('Cash: '))
            if UserCash > self.BankValue:
                print("Not Enough Money")
                time.sleep(1)
                exit(1)
            if UserCash % 1000 != 0:
                print("ATM cannot give coins")
                print("Exit Process...")
                time.sleep(1)
                exit(1)

            while UserCash >= 1000:
                for i in range(len(self.BankMoney)):
                    while UserCash >= self.BankMoney[i]:
                        if UserCash == 0 and self.BankValue >= 0:
                            print("Success")
                            break
                        elif UserCash >= self.BankMoney[i]:
                            UserCash -= self.BankMoney[i]
                            self.BankMoneyCount[i] -= 1

                    if self.BankMoneyCount[i] <= 0:
                        self.BankMoney.remove(self.BankMoney[i])
                        self.BankMoneyCount.remove(self.BankMoneyCount[i])
            print(self.BankMoneyCount)
        else:
            print("Incorrect data")
            print("Operation Failed")
            exit(1)
        print("Success ")
