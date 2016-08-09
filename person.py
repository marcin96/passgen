#Author Marcin Cherek
#Language: Python 3.4
#Version 1.0
#License: MIT


#This class handles a person with its tags
#The persons name will be also the file
#name of the generated passwords
import tag
class Person():
    tags=[]
    name=""
    def __init__(self,name):
        if(name!="" and name!=None):
            self.name=name
        else:
            None

    #Adds a tag
    def add_tagD(self,name,priority):
        self.tags.append(tag.Tag(name,priority))

    def add_tag(self,tag):
        self.tags.append(tag)

    #removes a tag
    def rem_tag(self,tag_name):
        None

    def isTag(self,tag_name):
        return tag_name in self.tags

    def getKey(self,tag):
        return tag.priority

    #sorts the tags after their priorities
    def sort_tags(self):
        sorted(self.tags,key=self.getKey)

