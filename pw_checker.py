#Password Strength Checker

# Takes in a password that the user gives and based on the length, 
# complexity, and given characters (Case sensitive) or symbols
# returns how strong or weak your password is against malicious attempts
# to access the website or information stored behind said password


#TODO Comment this professionally please...



import string
import getpass

#Defines the structure of what we look for in a passwor to determine its strength.
class aPassword:
    def __init__(self, length, hasSymbols, allNumbers, caseSensitive):
        self.allNumbers = allNumbers
        self.hasSymbols = hasSymbols
        self.caseSensitive  = caseSensitive
        self.length = length

#Defining Global Variables that are used in multiple instances
password = aPassword(0, False, False, False)
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=", "_", "+", "<" , ">", ",", ".", "/", "?", "'", ":", ";", "`", "~", "\""]
nums_in_pw = 0

#
def password_strength_checker():
    passwordRequest = getpass.getpass("Enter password to check its strength: ")
    password.hasSymbols = does_pw_have_symbols(passwordRequest)
    password.caseSensitive = is_pw_case_sensitive(passwordRequest)
    password.length = len(passwordRequest)
    password.allNumbers = is_pw_only_nums(passwordRequest)
    if in_Top_10mill_Easy_Pw_Pwnd(passwordRequest) is True:
        print("This password is in the top 100k most used passwords, do not use this password!")
    else:
        check_pw_complexity(passwordRequest)


#Lets users know how long it could take a user to hack/break into their password.
def want_more_specifics_timewise_on_brekabilitiy(timeToBreak) -> None:
    #dish out based on score, # only, lowercase only, upper and lower, num upper and lower, num, symbol, upper and lower
    # and length of password to give them a more accurate example of the strength (or weakness) of their password
    if timeToBreak == "Instantly" :
        print("Your password will be broken instantly.")
    else:
        print(f"It should take a hacker {timeToBreak} to break your password.")


#Checks if the password contains only numbers making it the least secure type of password
def is_pw_only_nums(password) -> bool:
    for char in password:
        if char.isdigit() and char.isnumeric():
            global nums_in_pw
            nums_in_pw+=1

    #if only numbers its here!
    # if length of pw = # of ints in pw TRUE else FALSE
    if len(password) == nums_in_pw:
        return True
    else:
        return False
        
#Checks if the password contains uppercase and lowercase letters
def is_pw_case_sensitive(pw) -> bool:
    upper = 0
    lower = 0
    for char in pw:
        if char.isupper():
            upper+=1
        elif char.islower():
            lower+=1

    if upper>1 and lower>1:
        return True
    else: 
        return False
    

#Checks if there are only lowercase characters in the password.
def is_pw_only_lower(pw) -> bool:
    lower_in_pw = 0
    for char in pw:
        for sym in symbols:
            if char.islower():
                lower_in_pw+=1
    if len(pw) == lower_in_pw:
        return True
    else:
        return False


def does_pw_have_symbols(pw) -> bool:
    num_of_symbols = 0
    for char in pw:
        for char2 in symbols:
            if char == char2:
                num_of_symbols+=1
    if num_of_symbols > 1:
        return True
    else:
        return False
    #if yes & case sensitive & nums-symbol plus to difficulty- 
    #if no and is case sensitive and !onlyNums use case+num part of chart

def in_Top_10mill_Easy_Pw_Pwnd(pw) -> bool:
    fileObj = r"C:\Users\laure\Downloads\100k-most-used-passwords-NCSC.txt"
    with open(fileObj, "r") as file:
        for line in file:
            commonlyUsedPw = line.strip()
            if commonlyUsedPw == pw:
                 return True
    return False


def check_pw_complexity(pw):
    if password.hasSymbols is True:
        want_more_specifics_timewise_on_brekabilitiy(get_Time_Case_for_Num_BothCase_Symbols(pw))
    else:
        if password.caseSensitive is True:
            if nums_in_pw > 0:
                want_more_specifics_timewise_on_brekabilitiy(get_Time_Case_for_num_BothCase(pw))
            elif nums_in_pw == 0:
                want_more_specifics_timewise_on_brekabilitiy(get_Time_Case_for_BothCase(pw))
        else:
            if password.allNumbers is False:
                want_more_specifics_timewise_on_brekabilitiy(get_Time_Case_for_lowerCase(pw))        
        if password.allNumbers is True and password.hasSymbols is False:
                want_more_specifics_timewise_on_brekabilitiy(get_Time_Case_for_num(pw))


def get_Time_Case_for_Num_BothCase_Symbols(pw) -> string:
    match len(pw):
        case 1 | 2 | 3 | 4:
            return "Instantly"
            #end purple
        case 5:
            return "4 hours"
        case 6:
            return "2 weeks"
            #end red
        case 7:
            return "2 years"
        case 8:
            return "164 years"
        case 9:
            return "11k years"
            #end orange
        case 10:
            return "803k years"
        case 11:
            return "56 million years"
        case 12:
            return "3 billion years"
            #end yellow
        case 13:
            return "275 billion years"
        case 14:
            return "19 trillion years"
        case 15:
            return "1 quadrillion years"
        case 16:
            return "94 quadrillian years"
        case 17:
            return "6 quintillion years"
        case 18:
            return "463 quintillion years"
        case _:
            return "longer than 463 quintillion years"


def get_Time_Case_for_num_BothCase(pw) -> string:
    match len(pw):
        case 1 | 2 | 3 | 4:
            return "Instantly"
            #end purple
        case 5:
            return "2 hours"
        case 6:
            return "6 days"
        case 7:
            return "1 years"
            #end red
        case 8:
            return "62 years"
        case 9:
            return "3k years"
            #end orange
        case 10:
            return "238k years"
        case 11:
            return "14 million years"
        case 12:
            return "917 million years"
            #end yellow
        case 13:
            return "56 billion years"
        case 14:
            return "3 trillion years"
        case 15:
            return "218 trillion years"
        case 16:
            return "13 quadrillion years"
        case 17:
            return "840 quadrillion years"
        case 18:
            return "52 quintillion years"
        case _:
            return "longer than 52 quintillion years"


def get_Time_Case_for_BothCase(pw) -> string:
    match len(pw):
        case 1 | 2 | 3 | 4:
            return "Instantly"
        #end purple
        case 5:
            return "57 minutes"
        case 6:
            return "2 days"
        case 7:
            return "4 months"
            #end red
        case 8:
            return "15 years"
        case 9:
            return "791 years"
        case 10:
            return "41k years"
            #end orange
        case 11:
            return "2 million years"
        case 12:
            return "111 million years"
        case 13:
            return "5 billion years"
            #end yellow
        case 14:
            return "300 brillion years"
        case 15:
            return "15 trillion years"
        case 16:
            return "812 trillion years"
        case 17:
            return "42 quadrillion years"
        case 18:
            return "2 quintillion years"
        case _:
            return "longer than 2 quintillion years"


##TODO Symbols are being considered as lowercase...
def get_Time_Case_for_lowerCase(pw) -> string:
    match len(pw):
        case 1 | 2 | 3 | 4 | 5:
            return "Instantly"
            #end purple
        case 6:
            return "46 minutes"
        case 7:
            return "20 hours"
        case 8:
            return "3 weeks"
            #end red
        case 9:
            return "2 years"
        case 10:
            return "40 years"
        case 11:
            return "1k years"
        case 12:
            return "27k years"
            #end orange
        case 13:
            return "705k years"
        case 14:
            return "18 million years"
        case 15:
            return "477 million years"
            #end yellow
        case 16:
            return "12 billion years"
        case 17:
            return "322 billion years"
        case 18:
            return "8 trillion years"
        case _:
            return "longer than 8 trillion years"


def get_Time_Case_for_num(pw) -> string:
    match len(pw):
        case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8:
            return "Instantly"
            #end purple
        case 9:
            return "2 hours"
        case 10:
            return "1 day"
        case 11:
            return "1 weeks"
        case 12:
            return "3 months"
            #end red
        case 13:
            return "3 years"
        case 14:
            return "28 years"
        case 15:
            return "284 years"
        case 16:
            return "2k years"
        case 17:
            return "28k years"
            #end orange
        case 18:
            return "284k years"
        case _:
            return "Longer than 284k years"



def main():
    password_strength_checker()


if __name__ == '__main__':
    main()
