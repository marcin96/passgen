#!/usr/bin/python

#Author Marcin Cherek
#Language: Python 3.4
#Version 1.0
#License: MIT

"""Generates a password considering all the informations
about a person
for best security
"""

from passgen import person
from passgen import pattern
from passgen import tag
import string
import random
from passgen import evaluator
import sys


def genPossibleChars(pers,pat):
    """
    Considers the pattern and fills
    The ret array with the possible chars
    """
    possible_chars = []
    possible_chars.append(string.ascii_lowercase)
    if(sec.Capital != pattern.pattern_Status.forbidden):
        possible_chars.append(ascii_uppercase)
    if(sec.Number != pattern.pattern_Status.forbidden):
        possible_chars.append(string.digits)
    if(sec.special_character != pattern.pattern_Status.forbidden):
        None #ToDo
    for i in pers.tags:
        if(i.isdigit()):
            possible_chars.remove(i)
    return random.shuffle(possible_chars)

def randomized_selection(chars,pat):
    """
    Selects randomized the chars for the password
    It breaks at the moment, when the password has
    the right pattern
    """
    pattern_confirmed=False
    passW=""
    while(pattern_confirmed!=True):
        if(evaluaor.confirmedPattern(passW,pat)):
           pattern_confirmed =True
           break
    return passW


def genPass(pers,pat):
    """
    #Generation method
    #Considers all Tags about a person
    #And the pattern
    #And the security
    #Pers->Person
    #pat ->Pattern
    #sec ->security
    """
    chars = genPossibleChars(pers,pat)
    password = randomized_selection(chars,pat.max_length)

def Gmain(argv):
    None
    
    

if __name__== "__main__":
    Gmain(sys.argv)
