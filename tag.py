#!/usr/bin/python

#Author Marcin Cherek
#Language: Python 3.4
#Version 1.0
#License: MIT

class Tag():
    """
    This class is for a single information
    About a person.
    It also handles the priority of the information.
    This is important for the generation of lists
    """
    name=""
    priority=0
    isnumeric = False
    def __init__(self,name,priority):
        if(self.__eval_arguments(name,priority)):
            self.name=name
            self.priority=priority
        else:
           None
           
    def __eval_arguments(self,name,priority):
        """
        Evaluates the given Arguments
        """
        if(isinstance(name,str)!=True):
            return False
        if(name==None or name==""):
            return False
        if(priority<0 or priority>10):
            return False
        return True
