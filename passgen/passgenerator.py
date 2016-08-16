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
from passgen import importer
import string
import random
from passgen import evaluator
from random import randint
import sys


def genPossibleChars(pers,pat):
    """
    Considers the pattern and fills
    The ret array with the possible chars
    """
    possible_chars = ""
    possible_chars+=string.ascii_lowercase
    if(pat.capital != pattern.pattern_Status.forbidden):
        possible_chars+=string.ascii_uppercase
    if(pat.numbers != pattern.pattern_Status.forbidden):
        possible_chars+=string.digits
    if(pat.special_characters != pattern.pattern_Status.forbidden):
        possible_chars+="".join(pat.specialCh_list)
    '''
    for i in pers.tags:
        if(i.isdigit()):
            possible_chars.remove(i)
    '''
    return possible_chars

def randomized_selection(chars,pat):
    """
    Selects randomized the chars for the password
    It breaks at the moment, when the password has
    the right pattern
    """
    passW = ""
    for c in range(pat.max_length):
        passW += chars[randint(0,len(chars)-1)]
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
    password = randomized_selection(chars,pat)
    print("Password>",password)

def Gmain(argv):
    '''
    Entry Point passgenerator
    '''
    if(len(argv)<=1):
        genPass(importer.InputPers(),importer.InputPat())
    else:
        None
    
    

if __name__== "__main__":
    Gmain(sys.argv)
