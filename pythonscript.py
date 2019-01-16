"""
THE FOLLOWING IS FROM AN ASSIGNMENT FROM THE FALL PYTHON COURSE:
Write a program that asks the user for their PIN number.
The valid PIN number is "1234".
The user has 3 attempts to enter the correct pin until they
are locked out of their account.
If the correct value is entered, a message is printed and
the program ends.
"""


def main():
    """
    Receive user input for pin number that must must "1234"
    """
    import sys

    for pin in range(0, 3):
        pin = input('Please enter your PIN: ')
        if pin == "1234":
            print("Your balance is 0...yikes :|. Goodbye!")
            sys.exit()
        else:
            print("INVALID PIN")

    print("You have tried too many times.")

# Do not edit below
if __name__ == "__main__":
    main()
