age=50

if age>=18:
    print("You can vote")
else:
    print("You're too young to vote")


grade=50

if grade>=50:
    print("Passed")
else:
    print("Failed")

print("Welcome to mobile money services")

balance=5000
pinCode="1234"

print("MTN mobile money")
print("1. Send Money")
print("2. Buy Airtime")
print("3. Check Balance")



option=input("Select an option ")

if option=="1":
    phone=input("Enter receipient number ")
    amount=float(input("Enter the amount to send "))
    pin=input("Enter your 4 digit pincode ")
    if pin!=pinCode:
        print("Invalid pin")
    else:
        if amount>balance:
            print("Insufficient balance")
        elif amount<=0:
            print("Enter amount above zero ")
        else:
            balance=balance-amount
            print("Transaction Sucessful")
            print(f"You've sent {amount} to {phone} ")
            print(f"Your balance left is {balance} ")

elif option=="2":
    print("1. Self")
    print("2. Others")

    choice=input("Select an option ")
    if choice=="1":
        amount=float(input("Enter amount to buy "))
        pin=input("Enter your 4 digit pin ")

        if pin!=pinCode:
            print("Invalid pin")
        elif amount>balance:
            print("Insufficient balance")
        elif amount<=0:
            print("Enter amount above zero ")
        else:
             balance=balance-amount
             print("Transaction Sucessful")
             print(f"You've bought an airtime of {amount} ")
             print(f"Your balance left is {balance} ")
    else:
        phone=input("Enter the number to send ")
        amount=float(input("Enter the amount to buy "))
        pin=input("Enter your 4 digit pin ")

        if pin!=pinCode:
            print("Invalid pin")
        elif amount>balance:
            print("Insufficient balance")
        elif amount<=0:
            print("Enter amount above zero")
        else:
            balance=balance-amount
            print("Transaction Sucessful")
            print(f"You've  successfully purcahase an amount of {amount} airtime to {phone} ")
            print(f"Your balance left is {balance} ")
else:
    if option=="3":
        pin=input("Enter your pin ")
        if pin!=pinCode:
            print("Invalid pin")
        else:
            print(f"Your balance is {balance}")
    else:
        print("Invalid option")
        

