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
    def add_tag(self,name,priority):
        self.tags.append(tag.Tag(name,priority))

    #removes a tag
    def rem_tag(self,tag_name):
        None

    def getKey(self,tag):
        return tag.priority

    #sorts the tags after their priorities
    def sort_tags(self):
        sorted(self.tags,key=self.getKey)

