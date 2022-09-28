import random 


print("Welcome to your password generator")


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*?"
numbers = input("How many passwords would you like to generate?: ")
numbers = int(numbers)
length = input("How long would the length of the password be?: ")
length = int(length)


print("\nHere is the amount of password generated.")

for pwd in range(numbers):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)