#!/usr/bin/python

#Author Marcin Cherek
#Language: Python 3.4
#Version 1.0
#License: MIT

import tag
class Person():
    """
    This class handles a person with its tags
    The persons name will be also the file
    name of the generated passwords
    """
    tags=[]
    name=""
    def __init__(self,name):
        if(name!="" and name!=None):
            self.name=name
        else:
            None

    def add_tagD(self,name,priority):
        """
        Adds a tag
        """
        self.tags.append(tag.Tag(name,priority))

    def add_tag(self,tag):
        self.tags.append(tag)

    def rem_tag(self,tag_name):
        """
        removes a tag
        """
        None

    def isTag(self,tag_name):
        return tag_name in self.tags

    def getKey(self,tag):
        return tag.priority

    def sort_tags(self):
        """
        #sorts the tags after their priorities
        """
        sorted(self.tags,key=self.getKey)

