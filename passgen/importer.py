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

if __name__ == '__main__':
    print("found [",len(import_persons(input("FILE>"))),"] persons")
    
