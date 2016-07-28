#This class is for a single information
#About a person.
#It also handles the priority of the information.
#This is important for the generation of lists
class Tag():
    name=""
    priority=0
    def __init__(self,name,priority):
        if(self.__eval_arguments(name,priority)):
            self.name=name
            self.priority=priority
        else:
           None
    #Evaluates the given Arguments
    def __eval_arguments(self,name,priority):
        if(isinstance(name,str)!=True):
            return False
        if(name==None or name==""):
            return False
        if(priority<0 or priority>10):
            return False
        return True
