#!/usr/bin/python

#Author Marcin Cherek
#Language: Python 3.4
#Version 1.0
#License: MIT

"""
Designed to check the strength of a password
"""

import re
from passgen import tag
from passgen import pattern
from passgen import person
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
            print("[Found Connection]>",i.name.lower())
            connection += i.priority/2
    return connection

def checkForRepeatingPatterns(passW):
    """
    Checks if the passWord has repeating patterns
    """
    r = re.compile(r"(.+?)(?=\1)")
    return len(r.findall(passW))

def isStatusChecked(status,iN):
    if(status == pattern.pattern_Status.forbidden):
        if(iN>0):return False
    if(status==pattern.pattern_Status.musthave):
        if(iN==0):return False
    return True

def confirmedPattern(passW,pat):
    """
    Checks if the password has the right pattern
    """
    if(len(passW)<pat.min_length or len(passW)>pat.max_length):
        return False
    if(isStatusChecked(pat.numbers,hasNumber(passW))==False):
        return False
    if(isStatusChecked(pat.capital,hasCapitalLetters(passW))==False):
        return False
    if(isStatusChecked(pat.special_characters,hasSpecialChars(passW,pat))==False):
        return False
    return True
    
def evaluate(passW,tags):
    """
    returns a integer from 0 to 10
    Specifies the strength of a password
    """
    points = len(passW)/3
    h_C = hasCapitalLetters(passW)
    h_N = hasNumber(passW)
    h_S = hasSpecialSymbols(passW)
    conn = hasConnection(passW,tags)
    print("length>",len(passW))
    points+=h_C
    print("Capital Letters>",h_C)
    points+=h_N
    print("Numbers>",h_N)
    points+=h_S
    print("Special Symbols>",h_S)
    points-=conn
    print("Connection>",conn)
    #points-=checkForRepeatingPatterns(passW)/2
    return abs(int(points))

def Emain(argv):
    passW = input("password:")
    tags = []
    while(True):
        i = input("Tag>")
        if(i!=""):
            tags.append(tag.Tag(str(i.split(',')[0]).strip(),int(i.split(",")[1])))
        else:
            break
    print("strength(Scala 1-10)>",evaluate(passW,tags))
#
if __name__== "__main__":
    #Entry Point
    """if main"""
    Emain(sys.argv)
