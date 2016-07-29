#Main method of listgen
#The Argument can be a xml file or
#Just nothing and in this case
#the generation information must be given
#manually into the console
import pattern
import person

#checks if password has Capital Letters
def hasCapitalLetters(passW):
    for i in passW:
        if(i.isupper()):
            return True
    return False
    
#Checks if password has Numbers
def hasNumber(passW):
    for i in ["0","1","2","3","4","5","6","7","8","9"]:
        if(i in passW):
            return True
    return False

#Checks if the password has the right pattern
def confirmedPattern(passW,pat):
    if(len(passW)<pat.min_length and len(passW)>pat.max_length):#Check length
        return False
    if(pat.numbers):
        if(hasNumber(passW)!=True):
            return False
    if(pat.capital):
        if(hasCapitalLetters(passW)!=True):
           return False
    return True
        
                
#Generates the passwords with the
#pattern information
def gen(person,pat):
    file = open(person.name+".txt","w+")
    person.sort_tags() #The tags are now sorted by their priority
    for i in person.tags:
        for w in person.tags:
            if(confirmedPattern(i.name+w.name,pat)):
                file.write(i.name+w.name+"\n")
    print("finished")

#generates passwords from xml file
#Also possible with multiple persons
def generate_from_file(filename):
    None

#In the case of generating wordlist
#without a xml file
def generate_manually():
    pers = person.Person(input("person's alias:"))
    pat = pattern.pattern()
    pat.capital=bool(input("Capital Letters(True,False):"))
    pat.min_length=int(input("minimal length:"))
    pat.max_length=int(input("maximal length:"))
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
