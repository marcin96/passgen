#Author Marcin Cherek
#Language: Python 3.4
#Version 1.0
#License: MIT

#Main method of listgen
#The Argument can be a xml file or
#Just nothing and in this case
#the generation information must be given
#manually into the console
import pattern
import person
import random
import evaluator
import string
import ast
from collections import OrderedDict
import datetime
import importer


#Removes doubles from a list
def eliminateDoubles(seq):
    return list(OrderedDict.fromkeys(seq))

#Sequences Posibilities of One Word
def sequencePossibilities(tag):
    ret = []
    ret.append(tag)
    ret.append(tag.upper())
    ret.append(tag.lower())
    ret.append(string.capwords(tag))
    return eliminateDoubles(ret)

#Sequences Posibilities of two Tags
def sequencePossibilities_Of_Two(tag,other):
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
    
    
#Generates Sequences of one Tag
def generateSequenceOfTag(tag,otherTag,length):
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
        if(len(tag)+len(otherTag)<length):
            for iT in sequencePossibilities_Of_Two(tag,otherTag):
                seq.append(iT)
        if((length-(len(tag)+len(otherTag))<3)):
             for i in range(length-len(tag)+len(otherTag)):
                 for iT in sequencePossibilities_Of_Two(tag,otherTag):
                     seq.append(iT+str(i))
    return eliminateDoubles(seq)
        
    
#Generates the passwords with the
#pattern information
def gen(person,pat):
    file = open(person.name+".txt","w+")
    person.sort_tags() #The tags are now sorted by their priority
    count=0
    for i in person.tags:
        for w in person.tags:
            #The real generation sequence
            passWS = generateSequenceOfTag(i.name,w.name,pat.max_length)
            for passW in passWS:
                if(evaluator.confirmedPattern(passW,pat)):
                    file.write(passW+"\n")
                    count+=1
    print("finished with "+str(count)+" results")
    print("Saved to " + person.name+".txt"," [ ",
          datetime.datetime.now().date()," ] "," [ ",
          datetime.datetime.now().time()," ]")

#generates passwords from xml file
#Also possible with multiple persons
def generate_from_file(filename):
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
           
           

#In the case of generating wordlist
#without a xml file
def generate_manually():
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

#The main method in thi
def generate_list(argv):
    if(argv==None or len(argv)==0):
        generate_manually()
    else:
        generate_from_file(argv[0])

#
if __name__== "__main__":
    generate_list(input())
