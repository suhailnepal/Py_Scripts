# Description: This is a note on how to use regular expressions in python. 

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
        if text[3] != '-':
            return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
        if text[7] != '-':
            return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True
print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))

## Better way of doing it (import re)

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

## If you want to add groups with the above, you could do

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo.group(1)
mo.group(2)
mo.group() ## If you want to get the whole thing

## Another example of doing this could be

pattern = r"\bexample\b"
matches = re.findall(pattern, text)
matches = re.findall(pattern, text)
print(matches)

# 1. Import the regex module with import re.
# 2. Create a Regex object with the re.compile() function. (Remember to use a 
# raw string.)
# 3. Pass the string you want to search into the Regex object’s search() method. 
# This returns a Match object.
# 4. Call the Match object’s group() method to return a string of the actual 
# matched text.

# Using pipe to match one of several patterns
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batman lost a wheel')
mo.group()
mo.group(1) ## This will return the first group which is man

# Optional Matching with the Question Mark, this is used when you want to match only optional groups

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()


mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()

# In the above, the regex matches both Batman and Batwoman

# The findall() Method
# Findall will return a set of string of set matches

import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# Output for the above will be [('415', '555', '9999'), ('212', '555', '0000')]

# Character Classes

""" /d: Any numeric digit from 0 to 9.
/D: Any character that is not a numeric digit from 0 to 9.
/w: Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
/W: Any character that is not a letter, numeric digit, or the underscore character.
/s: Any space, tab, or newline character. (Think of this as matching “space” characters.)
/S: Any character that is not a space, tab, or newline. """

# The charet and dollar sign
# The caret sign can be used to match a pattern at the beginning of a string.
# The dollar sign can be used to match a pattern at the end of a string.

beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello world!')
beginsWithHello.search('He said hello.') == None

endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 42')
endsWithNumber.search('Your number is forty two.') == None

# Case Insensitive Matching

robocop = re.compile(r'robocop', re.I)