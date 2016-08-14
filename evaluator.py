#!/usr/bin/python

#Author Marcin Cherek
#Language: Python 3.4
#Version 1.0
#License: MIT

"""
Designed to check the strength of a password
"""

import re
import tag
import pattern
import logging

logging.basicConfig()
logger= logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def hasSpecialChars(passW,pat):
    """
    This method counts how many special chars
    there in the current password
    """
    ret=0
    for i in pat.specialCh_list:
        if( i in passW):
            ret+=1
    return ret

def hasCapitalLetters(passW):
    """
    checks if password has Capital Letters
    """
    count = 0
    for i in passW:
        if(i.isupper()):
            count+=1
    return count
    
def hasNumber(passW):
    """
    Checks if password has Numbers
    """
    count=0
    for i in ["0","1","2","3","4","5","6","7","8","9"]:
        if(i in passW):
            count+=1
    return count

def hasSpecialSymbols(passW):
    """
    Checks if the password has special characters
    """
    if(re.match(r'^_-:,;<>+"*ç%&/()=?"',passW)):
        return True
    return False

def hasConnection(passW,tags):
    """
    Checks if the password has no connectio
    To the informations about the person
    Returns the strength of the Connection 0-10
    """
    connection=0
    for i in tags:
        if(i.name.lower() in passW.lower()):
            connection += i.priority/2
    return connection

def checkForRepeatingPatterns(passW):
    """
    Checks if the passWord has repeating patterns
    """
    r = re.compile(r"(.+?)(?=\1)")
    return len(r.findall(passW))

def confirmedPattern(passW,pat):
    """
    Checks if the password has the right pattern
    """
    if(len(passW)<pat.min_length or len(passW)>pat.max_length):#Check length
        return False
    if(pat.numbers):
        if(hasNumber(passW)==0):
            return False
    if(pat.capital):
        if(hasCapitalLetters(passW)==0):
            return False
    if(pat.special_characters):
        if(hasSpecialChars(passW,pat)==0):
            return False
    return True
    
def evaluate(passW,tags):
    """
    returns a integer from 0 to 10
    Specifies the strength of a password
    """
    points = len(passW)/10
    if(hasCapitalLetters(passW)):points+=hasCapitalLetters(passW)
    if(hasNumber(passW)):points+=hasNumber(passW)
    if(hasSpecialSymbols(passW)):points+=1
    points-=hasConnection(passW,tags)
    points-=checkForRepeatingPatterns(passW)/2
    return points

#
if __name__== "__main__":
    """if main"""
    passW = input("password:")
    tags = []
    while(True):
        i = input("Tag>")
        if(i!=""):
            tags.append(tag.Tag(str(i.split(',')[0]).strip(),int(i.split(",")[1])))
        else:
            break
    print("strength:",evaluate(passW,tags))
