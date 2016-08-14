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

def sequencePossibilities(tag,pat):
    """Sequences Posibilities of One Word"""
    ret = []
    ret.append(tag)
    ret.append(tag.lower())
    if(pat.capital != pattern.pattern_Status.forbidden):
        ret.append(tag.upper())
        ret.append(string.capwords(tag))
    if(pat.special_characters != pattern.pattern_Status.forbidden):
        for i in pat.specialCh_list:
            ret.append(tag+i)
            ret.append(tag.upper()+i)
            ret.append(string.capwords(tag)+i)
            ret.append(i+tag)
            ret.append(i+tag.upper())
            ret.append(i+string.capwords(tag))
    return eliminateDoubles(ret)

def sequencePossibilities_Of_Two(tag,other,pat):
    """Sequences Posibilities of two Tags"""
    ret = []
    ret.append(tag+other)
    ret.append(tag.lower()+other)
    ret.append(tag+other.lower())
    ret.append(tag.lower()+other.lower())
    if(pat.capital):
       ret.append(string.capwords(tag)+other)
       ret.append(tag+string.capwords(other))
       ret.append(string.capwords(tag)+string.capwords(other))
       ret.append(tag.upper()+other.upper())
       ret.append(tag.upper()+other)
       ret.append(tag+other.upper())
    return eliminateDoubles(ret)
    
    
def generateSequenceOfTag(tag,pat):
    """Generates Sequences of one Tag"""
    seq = []
    if(len(tag)<pat.max_length):
        for iT in sequencePossibilities(tag,pat):
            seq.append(iT)
        diff=pat.max_length-len(tag)
        if(diff>0 and pat.numbers != pattern.pattern_Status.forbidden):
            if(diff>2):diff=2
            rang = int(str(1)+diff*"0")
            for i in range(rang):
                for iT in sequencePossibilities(tag,pat):
                    if(evaluator.hasNumber(iT)==0):
                        seq.append(iT+str(i))
                        seq.append(str(i)+iT)
    return eliminateDoubles(seq)

def generateSequenceOfTags(tags,length):
    """Generates sequences of more tags
       Combines tags together that fits the pattern.
    """
    seq = []
    for i in tags:
            com = [tag.Tag(x.name+i.name,i.priority) for x in tags if (len(i.name)+len(x.name))<=length]
            for t in com:
                seq.append(t)
    return eliminateDoubles(seq)


def getCountTime(time):
    """
    if the needed time is below 1/10
    of a second 
    """
    if(time<1):return (1/10)/60

def get_tags(tags,length):
   """
   Like a puzzle algorithm it combines tags together to one tag
   """
   seq = []
   ret = []
   hasMorePossibilities=True
   for i in tags:ret.append(i)
   while(hasMorePossibilities):
      ret = generateSequenceOfTags(ret,length)
      if(ret!=[]):
          for i in ret:
              seq.append(i)
      else:
          hasMorePossibilities=False
          break
   return seq

# Print iterations progress
def printProgress (iteration, total, prefix = '', suffix = '', decimals = 2, barLength = 10):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : number of decimals in percent complete (Int)
        barLength   - Optional  : character length of bar (Int)
    """
    filledLength    = int(round(barLength * iteration / float(total)))
    percents        = round(100.00 * (iteration / float(total)), decimals)
    bar             = '█' * filledLength + '-' * (barLength - filledLength)
    if(platform.system()=="Windows"):os.system("cls")
    else:os.system("clear")
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),
    #sys.stdout.flush()
    if iteration == total:
        sys.stdout.write('\n')
        #sys.stdout.flush()
        if(platform.system()=="Windows"):os.system("cls")
        else:os.system("clear")

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
    count=0
    seq = get_tags(pers.tags,pat.max_length)
    for i in pers.tags:seq.append(i)
    for i in seq:
        if(len(i.name)>pat.max_length or len(i.name)<pat.min_length):continue
        #The real generation sequence
        passWS = generateSequenceOfTag(i.name,pat)
        for passW in passWS:
            printProgress(count,len(passWS),prefix = 'Progress:', suffix = 'Complete')
            if(evaluator.confirmedPattern(passW,pat)):
                file.write(passW+"\n")
                count+=1
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

def inputTopat_status(inputW):
    """
    String to the enum type pattern_StatusSpe
    """
    if(inputW=="musthave"):
        return pattern.pattern_Status.forced
    elif(inputW=="optional"):
        return pattern.pattern_Status.optional
    elif(inputW=="forbidden"):
        return pattern.pattern_Status.forbidden

def generate_manually():
    """
    In the case of generating wordlist
    without a xml file
    """
    pers = person.Person(input("person's alias:"))
    pat = pattern.pattern()
    pat.capital=inputTopat_status(input("Capital Letters(musthave,optional,forbidden):"))
    pat.numbers=inputTopat_status(input("numbers(musthave,optional,forbidden):"))
    pat.special_characters=inputTopat_status(input("Special characters(musthave,optional,forbidden):"))
    if(pat.special_characters):
            char_tmp = input("Which caracters do you want to allow(separate with comma,for all write ALL):")
            if(char_tmp=="ALL"):
                pat.specialCh_list = pat.all_specials.split(" ")
            else:
                for i in char_tmp.split(","):
                    pat.specialCh_list.append(i)
    pat.min_length=int(input("minimal length:"))
    pat.max_length=int(input("maximal length:"))
    print("Add Tags > name,priority (1-10)")
    print("Birthday,Name,Age,Name of Pet ect...")
    while(True):
        i=input("TAG>")
        if(i!=""):
            if(pers.isTag(str(i.split(',')[0]).strip())!=True):
                pers.add_tagD(str(i.split(',')[0]).strip(),int(i.split(",")[1]))
            else:print("#is already in the tags")
        else:break
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
