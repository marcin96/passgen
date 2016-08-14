#!/usr/bin/python

#Author Marcin Cherek
#Language: Python 3.4
#Version 1.0
#License: MIT

"""
This module is for searching local informations
about you. It creates a profile for generating possible passwords
for you.
It can also search for bad security settings.
After all it creates with the help of module dokumentator.py
A statistic about you in the form of html.
"""

import os
import sys
import getpass
import os
import socket

def searchForInf(homedir):
    None

def searchForSettings():
    None

def searchForPassWords(homedir):
    None

def search():
    username = getpass.getuser()
    homedir = os.environ['Home']
    hostname = socket.gethostname()
    print("username:",username)
    print("homedir",homedir)
    print("hostname",hostname)

if __name__=="__main__":
    search()
