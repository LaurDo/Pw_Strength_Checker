#Password Strength Checker

# Takes in a password that the user gives and based on the length, 
# complexity, and given characters (Case sensitive) or symbols
# returns how strong or weak your password is against malicious attempts
# to access the website or information stored behind said password

import string
import getpass
import array

strengthOfPw = 0
numsInPW = 0
hasSymbols = False
password = ""
symbols = array.array('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', '<' , '>', ',', '.', '/', '?', '', ':', ';', '`', '~', '\'' )

def password_strength_checker():
    passwordRequest = getpass.getpass("Enter password to check its strength: ")
    password = passwordRequest

    
def strong_pw():
    #
    print("Your password is strong enough to out live you.")



def weak_pw():
    #pws 6 chars and below regardless of complexity
    #nums only 12 or less (14 or less)
    #lowercase letters 8 or less (10 or less)
    #upper and lowercase letters & numbers 7 or less (8 or less)
    # both cases, nums, and symbols 6 or less (7 or less)
    # adding in anything less than a human lifespan.
        #these are in parenthesis above
    print("Your password is not safe. Recommendation, change it asap.")


def moderate_pw():
    #Orange to yellow

    print("Your password should be safe (according to Hive Systems brute for password time table) if you change it at least once every 2 years.")

def horrible_pw():
    #In top 100 common passwords
    print("If a hacker wanted your password, its posted in the top 100 most used (and easy to break) passwords. Change now.")


def want_more_specifics_timewise_on_brekabilitiy():
    #dish out based on score, # only, lowercase only, upper and lower, num upper and lower, num, symbol, upper and lower
    # and length of password to give them a more accurate example of the strength (or weakness) of their password
    years_to_break = 0

    if years_to_break == 0 :
        print("Your password will be broken instantly.")
    elif years_to_break == 1:
        print("Your password will break in a year.")
    else:
        print(f"It should take a hacker {years_to_break} year(s) to break your password.")



def is_pw_only_nums():
    nums_in_pw = 0
    for ints in password:
        nums_in_pw+=1

    #if only numbers its here!
    # if length of pw = # of ints in pw TRUE else FALSE
    if password == nums_in_pw:
        return True
    else:
        return False
        

def is_pw_case_sensitive():
    upper = 0
    lower = 0
    #does the pw have more than one case?
    #use isupper() and islower()
    for char in password:
        if char.isupper():
            upper+=1
        elif char.islower():
            lower+=1

    if upper>1 and lower >1:
        return True
    else: 
        return False



def does_pw_have_symbols():
    num_of_symbols = 0
    for char in password:
        for char2 in symbols:
            if char == char2:
                num_of_symbols+=1
    if num_of_symbols > 1:
        return True
    else:
        return False
    #if yes & case sensitive & nums-symbol plus to difficulty- 
    #if no and is case sensitive and !onlyNums use case+num part of chart
