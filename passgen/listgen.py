#!/usr/bin/python

#Author Marcin Cherek
#Language: Python 3.4
#Version 1.0
#License: MIT

"""
Generates Wordlists with specified pattern and person.
"""

import os
import time
import random
import string
import ast
from collections import OrderedDict
import datetime
from passgen import evaluator
from passgen import importer
from passgen import passgenerator
from passgen import tag
from passgen import pattern
from passgen import person
import logging
import random
import math
import sys
import platform
import itertools

logging.basicConfig()
logger= logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def isEnaughSpaceAviable(spaceN):
    """
    This method checks if there is
    enough spave aviable for the
    generation
    """
    try:
        st = os.statvfs(path)
    except(Exception):
        return -1
    sp_free = (st.f_bavail * st.f_frsize)
    if(sp_free>spaceN):
        return True
    return False

def howMuchSpaceNeeded(possibilities):
    """
    calculates how much space is
    needed in Bytes
    """
    return possibilities * 8

def howMuchPossibilities(tags,pat):
    """
    This method gives you the number of possibile
    combinations
    """
    possib = len(tags)
    diff = pat.max_length-pat.min_length
    if(pat.numbers):
        possib = possib *(diff*100) + 100
    if(pat.capital):
        possib *=3
    return possib
    
def workingTime(possibilities):
    """
    This method says how long
    a generation would take with
    the parameters
    """
    return possibilities /10000

def eliminateDoubles(seq):
    """
    Removes doubles from a list
    """
    return list(OrderedDict.fromkeys(seq))

def calculate_statistic(tags,pat):
    """
    Calculates if the generation should be done or not.
    *isEnaughSpaceAviable(spaceA,spaceN)
    *howMuchPossibilities
    *workingTime
    """
    pos = howMuchPossibilities(tags,pat)
    space_n = howMuchSpaceNeeded(pos)
    e_space = isEnaughSpaceAviable(space_n)
    work_t = workingTime(pos)
    print("Space Needed ~",space_n," bytes")
    print("Enough Space ~",e_space)
    print("Working Time ~",work_t, "seconds")
    print("Possible_passwords ~",pos)


def getCountTime(time):
    """
    if the needed time is below 1/10
    of a second 
    """
    if(time<1):return (1/10)/60

def printProgress (iteration, total, prefix = '', suffix = '', decimals = 2, barLength = 10):
    """
    creates terminal progress bar
    """
    filledLength    = int(round(barLength * iteration / float(total)))
    percents        = round(100.00 * (iteration / float(total)), decimals)
    bar             = '█' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r')
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),
    sys.stdout.flush()

def extractAllTags(pers):
    '''
    '''
    ret = []
    for i in pers.tags:
        ret.append(i.name)
    return ret

def sequence(tag_one_tag_two,lenght):
    '''
    '''
    if(len(tag_one)+len(tag_two)<lenght):
        return tag_one.join(tag_two)
    return None

def combi(ldata,lenght):
    '''
    '''
    collect = set()
    step = set([''])
    while step:
       step = set(a+b for a in step for b in ldata if len(a+b) <= lenght)
       collect |= step
    return sorted(collect)
                

def calculateCombinations(tags,pat):
    data = tags
    ret = []
    if(pat.special_characters != pattern.pattern_Status.forbidden):
        data.append(pat.speicalCh_list)
    if(pat.capital != pattern.pattern_Status.forbidden):
        for i in tags:
            if(str(i).isdigit()==False):
                data.append(i.upper())
                data.append(i.title())
    comb = combi(data,pat.max_length)
    for i in comb:
        if(evaluator.confirmedPattern(i,pat)):
           ret.append(i)
    return ret

def gen(pers,pat):
    """
    Main method of listgen
    The Argument can be a xml file or
    Just nothing and in this case
    the generation information must be given
    manually into the console
    """
    start_time = time.time()
    file = open(pers.name+".txt","w+")
    pers.sort_tags() #The tags are now sorted by their priority
    tags = extractAllTags(pers)
    combinations=calculateCombinations(tags,pat)
    for i in combinations:
        file.write(i)
        file.write("\n")
    count = len(combinations)
    print("\nfinished with "+str(count)+" results")
    print("Saved to " + pers.name+".txt"," [ ",
          datetime.datetime.now().date()," ] "," [ ",
          datetime.datetime.now().time()," ]")
    file.close()
    print("File size: [",os.stat((pers.name+".txt")).st_size  ," bytes]")
    print("Time : ", time.time()-start_time," sec")
    input("<Finish>")

def generate_from_file(filename):
    """
    generates passwords from xml file
    Also possible with multiple persons
    """
    if(filename.split(".")[1] in ["xml","XML"]):
        person_list = importer.import_persons(filename)
        pat = pattern.pattern()
        if(isinstance(persons_list[0],pattern.pattern())):
           pat = persons_list[0]
        for pers in persons_list:
           gen(pers,pat)
           print("Generating for>",pers.name)
    else:
        print("Wrong file extension")
        print("Please only ->xml")

def generate_manually():
    """
    In the case of generating wordlist
    without a xml file
    """
    pers = importer.InputPers()
    pat = importer.InputPat()
    calculate_statistic(pers.tags,pat)
    if(input("Wanna continue(yes/no)>") in ["y","Y","Yes","yes","YES"]):
        gen(pers,pat)
    else:
        print("finish")
        exit()

def generate_list(argv):
    """
    The main method in this module
    """
    if(argv==None or len(argv)==1):
        generate_manually()
    else:
        generate_from_file(argv[1])
        

if __name__== "__main__":
    generate_list(input("[]>"))
