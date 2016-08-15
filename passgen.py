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
    print("""
    usage: passgen [-version] [-help] [-gl] [-gp] [-e] [-update]
    -gl Password List Generator
    -gp Inteligent Password Generator
    -e Password Evaluator
    -v shows the Version
    -help shows the Help
    """)
    print("for more help go to>> https://github.com/marcin96/passgen/blob/master/Tutorial.pdf")
    
def update():
    print("cd ..")
    print("git clone https://github.com/marcin96/passgen.git")
    print("cd passgen")
    print("#DOIT")


def print_hai():
    print(
        """
 _______  _______  _______  _______  _______  _______  _       
(  ____ )(  ___  )(  ____ \(  ____ \(  ____ \(  ____ \( (    /|
| (    )|| (   ) || (    \/| (    \/| (    \/| (    \/|  \  ( |
| (____)|| (___) || (_____ | (_____ | |      | (__    |   \ | |
|  _____)|  ___  |(_____  )(_____  )| | ____ |  __)   | (\ \) |
| (      | (   ) |      ) |      ) || | \_  )| (      | | \   |
| )      | )   ( |/\____) |/\____) || (___) || (____/\| )  \  |
|/       |/     \|\_______)\_______)(_______)(_______/|/    )_)
                                                               
        """
        )
    
#Main Method
#Analyses the parameters
def main(argv):
    #generate List
    if(argv[1]=="-gl"):
        print_hai()
        listgen.generate_list(argv[1:])
    #generate Password
    elif(argv[1]=="-gp"):
        print_hai()
        passgenerator.Gmain(argv[1:])
    #Evaluate
    elif(argv[1]=="-e"):
        print_hai()
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
