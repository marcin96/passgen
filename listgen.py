#Main method of listgen
#The Argument can be a xml file or
#Just nothing and in this case
#the generation information must be given
#manually into the console
import pattern
import person

def gen(person,pattern):
    file = open(person.name+".txt","a")
    
    
def generate_from_file(filename):
    None
    
def generate_manually():
    pers = person.Person(input("person's alias:"))
    pat = pattern.pattern()
    pat.capital=bool(input("Capital Letters(True,False):"))
    pat.length=int(input("length:"))
    pat.numbers=bool(input("numbers(True,False):"))
    print("Add Tags > name,priority")
    print("Birthday,Name,Age,Name of Pet ect...")
    while(True):
        i=input("TAG>")
        if(i!=""):
            pers.add_tag(str(i.split(',')[0]),int(i.split(",")[1]))
        else:break
    gen(pers,pat)
    
def generate_list(argv):
    if(argv==None):
        generate_manually()


generate_list(None)
