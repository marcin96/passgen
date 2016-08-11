#Author Marcin Cherek
#Language: Python 3.4
#Version 1.0
#License: MIT

"""
Generates Wordlists with specified pattern and person.
"""

import os
import time
import pattern
import random
import evaluator
import string
import ast
from collections import OrderedDict
import datetime
import importer
import tag
import person

def isEnaughSpaceAviable(spaceA,spaceN):
    """
    This method checks if there is
    enough spave aviable for the
    generation
    """
    None

def howMuchSpaceNeeded():
    """
    calculates how much space is
    needed
    """
    None

def howMuchPossibilities():
    """
    This method gives you the count of possbile
    combinations
    """
    None
    
def workingTime(tags,pattern):
    """
    This method says how long
    a generation would take with
    the parameters
    """
    None

def eliminateDoubles(seq):
    """
    Removes doubles from a list
    """
    return list(OrderedDict.fromkeys(seq))

def sequencePossibilities(tag):
    """Sequences Posibilities of One Word"""
    ret = []
    ret.append(tag)
    ret.append(tag.upper())
    ret.append(tag.lower())
    ret.append(string.capwords(tag))
    return eliminateDoubles(ret)

def sequencePossibilities_Of_Two(tag,other):
    """Sequences Posibilities of two Tags"""
    ret = []
    ret.append(tag+other)
    ret.append(string.capwords(tag)+other)
    ret.append(tag+string.capwords(other))
    ret.append(string.capwords(tag)+string.capwords(other))
    ret.append(tag.lower()+other)
    ret.append(tag+other.lower())
    ret.append(tag.lower()+other.lower())
    ret.append(tag.upper()+other.upper())
    ret.append(tag.upper()+other)
    ret.append(tag+other.upper())
    return eliminateDoubles(ret)
    
    
def generateSequenceOfTag(tag,length):
    """Generates Sequences of one Tag"""
    seq = []
    if(len(tag)<length):
        for iT in sequencePossibilities(tag):
            seq.append(iT)
        diff=length-len(tag)
        if(diff<3):
            rang = int(str(1)+diff*"0")
            for i in range(rang):
                for iT in sequencePossibilities(tag):
                    seq.append(iT+str(i))
                    seq.append(str(i)+iT)
    return eliminateDoubles(seq)

def generateSequenceOfTags(tags,length):
    """Generates sequences of more tags"""
    seq = []
    for i in tags:
            com = [tag.Tag(x.name+i.name,i.priority) for x in tags if (len(i.name)+len(x.name))<=length]
            for t in com:
                print(t.name)
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
        if(evaluator.confirmedPattern(i.name,pat)!=True):continue
        #The real generation sequence
        passWS = generateSequenceOfTag(i.name,pat.max_length)
        for passW in passWS:
            if(evaluator.confirmedPattern(passW,pat)):
                file.write(passW+"\n")
                count+=1
    print("finished with "+str(count)+" results")
    print("Saved to " + pers.name+".txt"," [ ",
          datetime.datetime.now().date()," ] "," [ ",
          datetime.datetime.now().time()," ]")
    file.close()
    print("File size: [",os.stat((pers.name+".txt")).st_size  ,"]")
    print("Time : ", getCountTime((start_time-time.time()))," min")

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
    pers = person.Person(input("person's alias:"))
    pat = pattern.pattern()
    pat.capital=ast.literal_eval(input("Capital Letters(True,False):"))
    pat.min_length=int(input("minimal length:"))
    pat.max_length=int(input("maximal length:"))
    pat.numbers=ast.literal_eval(input("numbers(True,False):"))
    print("Add Tags > name,priority (1-10)")
    print("Birthday,Name,Age,Name of Pet ect...")
    while(True):
        i=input("TAG>")
        if(i!=""):
            if(pers.isTag(str(i.split(',')[0]).strip())!=True):
                pers.add_tagD(str(i.split(',')[0]).strip(),int(i.split(",")[1]))
            else:print("#is already in the tags")
        else:break
    gen(pers,pat)

def generate_list(argv):
    """
    The main method in this module
    """
    if(argv==None or len(argv)==0):
        generate_manually()
    else:
        generate_from_file(argv[0])


if __name__== "__main__":
    generate_list(input())
