# Creating a simple Telegram login page 
print("Telegram Login")
country = input("Enter the name of your country: ")
phone = input("Enter your phone number: ")
print("We've sent a verification code to your phone number.")
verificationCode = int(input("Enter your verification code: "))
loginSuccessful = bool(verificationCode)




