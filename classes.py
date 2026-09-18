class Car:
    def __init__(self, color, model, brand):
        self.color = color
        self.model = model
        self.brand = brand

car1=Car("white","x-class","Toyota")

    


class Laptop:
    def __init__(self, processor, device_name, ram, storage):
        self.processor = processor
        self.device_name = device_name
        self.ram = ram
        self.storage = storage

laptop1=Laptop("Intel Core i5", "Work laptop", 8, 512)
laptop2=Laptop("AMD Ryzen 7", "Personal laptop", 16, 1024)

print(laptop1.processor)
print(laptop2.ram)



class MTNMOMO:
    def __init__(self, name, phone, balance, pincode):
        self.name = name
        self.phone = phone
        self.balance = balance
        self.pincode = pincode

   
    def send_Money(self):
        phone = input("Enter recipient phone number: ")
        if len(phone)<10 or len(phone)>10:
            print("Invalid number")
            return
        try:
            amount = float(input("Enter amount to send: "))
        except ValueError:
            print("Invalid amount")
            return 

        pin = input("Enter your 4-digit pincode: ")
        if pin != self.pincode:
            print("Invalid pincode")
            return 
        if amount<=0:
            print("You can only send amount greater than zero")
            return 
        if amount >self.balance:
            print("Insufficient balance")
            print("Please top up your momo balance")
            return 

        self.balance -= amount
        print("Transaction successful")
        print(f"You've sent Ghc {amount} to {phone}. Your current balance is {self.balance}")
        return 


    def buy_Airtime(self):
        print("Buy airtime for family and friends")
        print("1. Self")
        print("2. Others")
        select = input("Select one of the options above: ")

        if select != "1" and select != "2":
            print("Invalid option")
            return
        phone = input("Enter recipient phone number: ")
        if len(phone)<10 or len(phone)>10:
            print("Invalid number")
            return

        try:
            amount = float(input("Enter amount to purchase: "))
        except ValueError:
            print("Invalid amount")
            return 

        pin = input("Please enter your pincode to validate the transaction: ")
        if pin != self.pincode:
            print("Invalid pin, please try again")
            return 

        if amount<=0:
            print("Airtime amount must be greater than zero")
            print(f"Your remaining balance is {self.balance}")
            return 
    
        if amount > self.balance:
            print("Insufficient balance in your account , please top up your momo balance")
            print(f"You've have Ghc {amount} in your account")
            return

        self.balance -= amount
        if select=="1":
            print(f"You've purchased Ghc {amount} of airtime for self")
            print(f"Your current balance is {self.balance}")

        else:
            print(f"You have successfully purchased airtime of Ghc {amount} to {phone}. Your current balance is {self.balance}")
            return 


    def check_balance(self):
        pin=input("Please enter your pincode to access your balance: ")
        if pin == self.pincode:
            print(f"Your balance is Ghc {self.balance}")
        else:
            print("Invalid pin code")
            return 
    
MyAccount = MTNMOMO(name="", phone="", balance=500, pincode="1234")

while True:
    print("WELCOME TO MTN MOMO")
    print("1. Send Money")
    print("2. Buy Airtime")
    print("3. Check Balance")
    print("4. Exit")

    options = input("Please select one of the options above: ")

    if options == "1":
        MyAccount.send_Money()
    elif options == "2":
        MyAccount.buy_Airtime()
    elif options == "3":
        MyAccount.check_balance()
    elif options == "4":
        print("Thank yoou for using MTN MOMO")
        break
    else:
        print("Invalid option")



