#!/usr/bin/python

#Author Marcin Cherek
#Language: Python 3.4
#Version 1.0
#License: MIT

import sys
import os
import logging

#Project Imports
from passgen import evaluator
from passgen import listgen
from passgen import passgenerator
from passgen import tag
from passgen import pattern
from passgen import person

logging.basicConfig()
logger= logging.getLogger(__name__)
logger.setLevel(logging.INFO)

VERSION=1.0

def help_me():
    print("for more help go to>> https://github.com/marcin96/passgen/blob/master/Tutorial.pdf")
    
def update():
    os.system("cd ..")
    os.system("git clone https://github.com/marcin96/passgen.git")
    os.system("cd passgen")

#Main Method
#Analyses the parameters
def main(argv):
    #generate List
    if(argv[1]=="-gl"):
        listgen.generate_list(argv[1:])
    #generate Password
    elif(argv[1]=="-gp"):
        passgenerator.Gmain(argv[1:])
    #Evaluate
    elif(argv[1]=="-e"):
        evaluator.Emain(argv[1:])
    #Help
    elif(argv[1]=="-help"):
        help_me()
    elif(argv[1] in ["-v","-version"]):
        print(VERSION)
    elif(argv[1] in ["-u","-update"]):
        update()
    else:
        print("WRONG ARGUMENT")

if __name__ == "__main__":
    #Entry Point
    """if main"""
    main(sys.argv)
