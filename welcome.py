from get_name import *
from validate_age import *
from survey import *

print("="*50)
print("\tWelcome to voting system check")
print("="*50)
print("\n")

name = get_name()
print(f"Hello {name}!\n")

age = int(input("Enter your age: "))
validate_age(age)

participate = input("Would you like to participate in our survey (Y/N): ")

if participate == "Y":
    survey()
    
print("\nThank you!")