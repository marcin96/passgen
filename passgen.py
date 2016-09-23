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

logging.basicConfig(filename='~log.log',level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

VERSION=1.0

def check_environment():
    '''
    Checks the python version
    '''
    if sys.version_info < (3.0):
        logger.critical("Wrong Python Version")
        raise "must use python 3.0 or greater"
    
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
    if(len(argv)==1):return 0
    if(argv[1]=="-gl"):
        print_hai()
        logger.info("<<Listgen>>")
        listgen.generate_list(argv[1:])
    #generate Password
    elif(argv[1]=="-gp"):
        print_hai()
        logger.info("<<passgenerator>>")
        passgenerator.Gmain(argv[1:])
    #Evaluate
    elif(argv[1]=="-e"):
        print_hai()
        logger.info("<<evaluator>>")
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

'''if __name__ == "__main__":
    #Entry Point
    """if main"""
    if(len(sys.argv)==1):
        help_me()
        exit()
    try:
        main(sys.argv)
    except RuntimeError:
        logger.error("Runtime Error, possibly to much possible passwords and to view hd space for file.")
    except TypeError:
        logger.error("Type Error, possibly wrong input#Wrong XML")
    except NameError:
        logger.error("Name Error, name not found,,,,this error shouldn't happen")
    except IOError:
        logger.error("IO Error , sth wrong with path, or you don't have permission to edit a file.")
    except OSError:
        logger.error("OS Error, wrong OS, passgen was only tested on Windows and Linux")
    except ValueError:
        logger.error("Wrong Value Input")
    else:
        logger.error("Not defined error")
'''
main(sys.argv)
