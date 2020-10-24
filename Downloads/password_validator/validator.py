"""
##########################################################################
	Name: Avs Revanth
	Student_id: 1684293
	CMPUT 274 Fall 2020
	Weekly Exercise = 1
	Exercise: Password validator and Password generater
##########################################################################
"""
# To generate a random number imported randint method form random
from random import randint

# Password validater arguments password and return value Secure or Insecure or Invalid
def validate(password):
	# Initize all local variables for this function
    count_invalid = 0
    count_upper = 0
    count_lower = 0
    count_digit = 0
    count_spechar = 0
    # List of forbidden characters
    forbidden_characters = [" ", "@", "#"]
    # List fo special characters
    special_characters = ["!" ,"-" ,"$" ,"%" ,"&" ,"'" ,"(" ,")" ,"*" ,"+" ,"." ,"/" ,":" , ";", "<", "=", ">", "?", "_", "<", "[", "]", "^", "`", "{", "|", "}", "~"]
    size = len(password)
    # for loop to check for forbidden characters in password
    for char in password:
        if char in forbidden_characters:
            count_invalid += 1
    # if condition to check if its a Invalid password
    if size < 8 or count_invalid > 0:
    	# Returns if it's Invalid and function call will end here
        return("Invalid")
    # Checking if its a secure password only if its not Invalid password
    elif size >= 8:
    	# for loop to check all cases of secure password conditions
        for char in password:
            if char.isupper():
                count_upper += 1
            if char.islower():
                count_lower += 1
            if char.isdigit():
                count_digit += 1
            if char in special_characters:
                count_spechar += 1
        # Checking if the password met all requriments of secure password
        if count_upper > 0 and count_lower > 0 and count_digit > 0 and count_spechar > 0:
            # Returns if it's a secure and function call will end here
            return("Secure")
        # Checking if the password is a Insecure password only when if it's not a secure password
        elif size >= 8 and count_invalid == 0:
        	# Returns if it's a Insecure and function call will end here
            return("Insecure")

# Password generater arguments length of password and return generated password 
def generate(n):
    if n<8:
    	# The function call will end here if the entered length password is less than 8 
    	return("Wrong input enter number >= 8")
    # List of special characters
    special_characters = ["!","-","$","%","&","'","(",")","*","+",".","/",":",";","<","=",">","?","_","<","[","]","^","`","{","|","}","~"]
    # List of digits
    digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # initializing the While condition
    condition_state = True
    count_value = 0
    count_upper = 0
    count_lower = 0
    count_digit = 0
    count_spechar = 0
    password = ""
    rand_num = 0
    rand_num1 = 0
    # Checking again if the length is >= 8
    if n >= 8:
    	# While loop to generate password since password length is unknown
        while condition_state:
            if n > count_value:
                password += chr(randint(65,90))
                count_value += 1
            if n > count_value:
                password += chr(randint(97,122))
                count_value += 1
            if n > count_value:
                rand_num1 = randint(0,9)
                password += digit[rand_num1]
                count_value += 1
            if n > count_value:
                rand_num = randint(0,27)
                password += special_characters[rand_num]
                count_value += 1
            if n == count_value:
                condition_state = False
        # for loop to check all cases of secure password conditions
        for char in password:
            if char.isupper():
                count_upper += 1
            if char.islower():
                count_lower += 1
            if char.isdigit():
                count_digit += 1
            if char in special_characters:
                count_spechar += 1
        # Checking if the password met all requriments of secure password
        if count_upper > 0 and count_lower > 0 and count_digit > 0 and count_spechar > 0:
            return(password)

if __name__ == "__main__":
    print(validate(input("Enter: ")))
    print(generate(int(input("Enter: "))))