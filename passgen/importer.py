#!/usr/bin/python

#Author Marcin Cherek
#Language: Python 3.4
#Version 1.0
#License: MIT

import os
import sys
from xml.dom import minidom
from passgen import person
from passgen import tag
from passgen import pattern

#return persons and a pattern in a List
#If there is a pattern it will be on the position 0
#in the returned list
#this should be considered.
def import_persons(xml_file):
    ret = []
    xmldoc = minidom.parse(xml_file)
    pat_element = xmldoc.getElementsByTagName("pattern")
    if(len(pat_element) != 0):
        pat_element = pat_element[0]
        pat = pattern.pattern()
        pat.capital = pat_element.attributes['capital'].value
        pat.numbers = pat_element.attributes['numbers'].value
        pat.min_length= pat_element.attributes['min_length'].value
        pat.max_length= pat_element.attributes['max_length'].value
        ret.append(pat)
    itemlist = xmldoc.getElementsByTagName("person")
    print("Items [",len(itemlist),"]")
    for pers in itemlist:
        person_tmp = person.Person(pers.attributes['name'].value)
        taglist = pers.getElementsByTagName("tag")
        for tg in taglist:
            t = tag.Tag(tg.attributes['name'].value,int(tg.attributes['priority'].value))
            person_tmp.add_tag(t)
        person_tmp.sort_tags()
        ret.append(person_tmp)
    return ret

def inputTopat_status(inputW):
    """
    String to the enum type pattern_StatusSpe
    """
    if(inputW.lower().strip() in ["musthave","must","m"]):
        return pattern.pattern_Status.musthave
    elif(inputW.lower().strip() in ["optional","opt","o"]):
        return pattern.pattern_Status.optional
    elif(inputW.lower().strip() in ["forbidden","forb","f"]):
        return pattern.pattern_Status.forbidden

def InputPat():
    '''
    '''
    pat = pattern.pattern()
    pat.capital=inputTopat_status(input("Capital Letters(musthave,optional,forbidden):"))
    pat.numbers=inputTopat_status(input("numbers(musthave,optional,forbidden):"))
    pat.special_characters=inputTopat_status(input("Special characters(musthave,optional,forbidden):"))
    if(pat.special_characters!=pattern.pattern_Status.forbidden):
            char_tmp = input("Which caracters do you want to allow(separate with comma,for all write ALL):")
            if(char_tmp=="ALL"):
                pat.specialCh_list = pat.all_specials.split(" ")
            else:
                for i in char_tmp.split(","):
                    pat.specialCh_list.append(i)
    pat.min_length=int(input("minimal length:"))
    pat.max_length=int(input("maximal length:"))
    return pat

def correct_input(inp):
    '''
    '''
    if("," not in inp):return False
    return True

def InputPers():
    '''
    '''
    pers = person.Person(input("person's alias:"))
    print("Add Tags > name,priority (1-10)")
    print("Birthday,Name,Age,Name of Pet ect...")
    while(True):
        i=input("TAG>")
        if(i!="" and correct_input(i)):
            if(pers.isTag(str(i.split(',')[0]).strip())!=True):
                pers.add_tagD(str(i.split(',')[0]).strip(),int(i.split(",")[1]))
            else:print("#is already in the tags")
        else:
            if( i==""):break;
            else:
                print("check your input #Wrong Syntax")
    return pers

if __name__ == '__main__':
    print("found [",len(import_persons(input("FILE>"))),"] persons")
    
