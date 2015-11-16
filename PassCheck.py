"""
Password checker for the password with Turkish characters. The function
below checks both length and characters of password. A password with
minimum 8 characters, at least one letter and one digit is accepted as
valid.
"""
import re

def password_checker(password):
    minimum_length = 8
    if len(password) >= minimum_length:
        #Check for Turkish Characters
        password_restrictions = re.compile(r'^(?=.*?[^\W_])(?=.*?\d)',re.IGNORECASE | re.UNICODE)
        if not password_restrictions.match(password) or password.isdigit():
            print "Password is not valid!"
        else:
         print "This is a valid password."
    else:
        print "Password is too short!"


if __name__ == "__main__":
    print "Please enter your password:"
    password = raw_input()
    password_checker(password)
