#A function are reusable block of code that perform a specific task.

#def greet(name):
#     print("Hello!", name)

#greet("Joe State")
#greet("James")

#def add(a,b):
 #   return a + b

#result = add(3,6)
#print(result)

#MoMo services
balance=5000
pin_code="1234"

def send_Money(balance):
    phone = input("Enter recipient phone number: ")
    try:
        amount = float(input("Enter amount to send: "))
    except ValueError:
        print("Invalid amount")
        return balance

    pin = input("Enter your 4-digit pincode: ")
    if pin != pin_code:
        print("Invalid pincode")
        return balance
    if amount<=0:
        print("You can only send amount greater than zero")
        return balance
    if amount > balance:
        print("Insufficient balance")
        print("Please top up your momo balance")
        return balance

    balance=balance-amount
    print("Transaction successful")
    print(f"You've sent Ghc {amount} to {phone}. Your current balance is {balance}")
    return balance


def buy_Airtime(balance):
    print("Buy airtime for family and friends")
    print("1. Self")
    print("2. Others")
    select = input("Select one of the options above: ")

    if select == "2":
        phone = input("Enter recipient phone number: ")

    try:
        amount = float(input("Enter amount to purchase: "))
    except ValueError:
        print("Invalid amount")
        return balance

    pin = input("Please enter your pincode to validate the transaction: ")
    if pin != pin_code:
        print("Invalid pin, please try again")
        return balance

    if amount<=0:
        print("Airtime amount must be greater than zero")
        print(f"Your remaining balance is {balance}")
        return balance
    
    if amount > balance:
        print("Insufficient balance in your account , please top up your momo balance")
        print(f"You've have Ghc {amount} in your account")
        return balance

    balance= balance-amount
    if select=="1":
        print(f"You've purchased Ghc {amount} of airtime for self")
        print(f"Your current balance is {balance}")

    elif select == "2":
        print(f"You have successfully purchased airtime of Ghc {amount} to {phone}. Your current balance is {balance}")
    return balance


def check_balance(balance):
    pin=input("Please enter your pincode to access your balance: ")
    if pin==pin_code:
        print(f"Your balance is Ghc {balance}")
    else:
        print("Invalid pin code")
        return balance
    return balance


print("WELCOME TO MOBILE MONEY SERVICES")
print("-----------------------------------")
print("1. Send Money")
print("2. Buy Airtime")
print("3. Check Balance")

options=input("Please select one of the option above: ")

if options=="1":
    sendMoney=send_Money(balance)
elif options=="2":
    buyAirtime=buy_Airtime(balance)
elif options=="3":
    checkBalance=check_balance(balance)
else: 
    print("Invalid option")

