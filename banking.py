import pandas as pd

df=pd.read_csv("accounts.csv")

class Bank:
    def __init__(self,name):
        self.name = name
        self.balance = df.loc[df['account_holder'] == self.name,'balance'].squeeze()
    
    def deposit(self, amount):
        self.balance += amount
        df.loc[df['account_holder']==self.name,"balance"]=self.balance
        
        df.to_csv("accounts.csv",index=False)
        
        content = f"{amount} deposited. New balance is {self.balance}"
        return content

    def withdraw(self,amount):
        self.balance-=amount
        df.loc[df['account_holder']==self.name,'balance']=self.balance
        
        df.to_csv("accounts.csv",index=False)
        
        content = f"{amount} Withdrawn. New balance is {self.balance}"
        return content

class BankSystem:
    def __init__(self, name, account_balance):
        self.name = name
        self.balance = account_balance

    def viewBalance(self):
        
        current_balance=df.loc[df['account_holder']==self.name,"balance"].squeeze()
        
        content = f"Account Holder: {self.name}, Balance: {current_balance}"
        return content

    def createAccount(self, name, balance):
        new_row={'account_holder':self.name,'balance':self.balance}
        new_df=pd.DataFrame([new_row])
        
        updated_df=pd.concat([df,new_df],ignore_index=True)
        
        updated_df.to_csv("accounts.csv",index=False)
        
        content = f"Account created for {name} with balance: {balance}"
        return content
    
    
system = BankSystem('arpit',0)

print('1. Create Account')
print('2. Deposit money')
print('3. View Balance')
print('4. Withdraw Money')
print('5. Exit')

print(df)

while True:
    choice = int(input("Enter choice: "))
    if choice == 1:
        name = input("Enter your name: ")
        deposit = int(input("Enter the initial amount to deposit: "))
        system = BankSystem(name,deposit)

        print(system.createAccount(name, deposit))

    elif choice == 2:
        name=input("Enter your name:")
        amount = int(input("Enter the amount to deposit: "))
        bank = Bank(name)
        print(bank.deposit(amount))

    elif choice == 3:
        name=input('Enter name:')
        print(system.viewBalance())

    elif choice==4:
        name=input("Enter a name:")
        bank1=Bank(name)
        amount = int(input("Enter the amount to withdraw: "))
        print(bank1.withdraw(amount))

    elif choice == 5:
        print('Thank you for using this program!')
        break

