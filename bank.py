class Bank:

    def __init__(self):
        self.accounts = []

    def __str__(self):
        return str([str(acnt) for acnt in self.accounts])


class Account:
    def __init__(self, name, accnt_no, passwd, balance):
        self.name = name
        self.accnt_no = accnt_no
        self.passwd = passwd
        self.balance = balance

    def __str__(self):
        return "name : " + self.name + " " + "accnt no : " + self.accnt_no + " " + "passwd : " + self.passwd + " Balance :"+ str(self.balance)


bank = Bank()


def data():
    a = input("to create an account pls typ yes \n already have a account pls typ no")
    if a == "yes":
        acno = input("Account number:")
        acname = input("Account holder name")
        passwd = input("Enter password")
        balance=int(input("Enter depositing money:"))
        account = Account(acname, acno, passwd,balance)
        bank.accounts.append(account)
        data()
    if a == "no":
        d = int(input("To deposit money press:1  To withdraw money press:2  To transfer money press:3 "))
        if d==1:
            acno = input("account number:")
            for account in bank.accounts:
                if account.accnt_no == acno:
                    money=int(input("money to be deposited"))
                    account.balance=account.balance+money
                    print(bank)
        if d==2:
            acno = input("account number:")
            flag=false
            for account in bank.accounts:
                if account.accnt_no == acno:
                    money = int(input("money to withdraw:"))
                    if money > account.balance:
                        print("Insufficient balance" )
                    else:
                        account.balance = account.balance - money
                    print(bank)
        if d==3:
            acno = input("your account number:")
            acno1 = input(" account number you want to sent money:")
            for account1 in bank.accounts:
                if account1.accnt_no==acno:
                    for account2 in bank.accounts:
                        if account2.accnt_no==acno1:
                            money=int(input("enter money:"))
                            account1.balance=account1.balance-money
                            account2.balance = account2.balance + money
            print(bank)
data()
