#Author Marcin Cherek
#Language: Python 3.4
#Version 1.0
#License: MIT

import sys
import os
#Project Imports
import evaluator
import listgen
import passgenerator

def help_me():
    print("help")
    

#Main Method
#Analyses the parameters
def main(argv):
    #generate List
    if(argv[0]=="-gl"):
        listgen.generate_list(argv[1:])
    #generate Password
    elif(argv[0]=="-gp"):
        None
    #Evaluate
    elif(argv[0]=="-e"):
        None
    #Help
    elif(argv[0]=="-help"):
        None
    else:
        print("WRONG ARGUMENT")

#Entry Point
main(sys.argv)
