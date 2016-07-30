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


#Checks if the password has the right pattern
def confirmedPattern(passW,pat):
    if(len(passW)<pat.min_length and len(passW)>pat.max_length):#Check length
        return False
    if(pat.numbers):
        if(evaluator.hasNumber(passW)!=True):
            return False
    if(pat.capital):
        if(evaluator.hasCapitalLetters(passW)!=True):
           return False
    return True

#Generates Sequences of One Tag
def generateSequenceOfTag(tag,otherTag,length):
    seq = []
    seq.append(tag.upper())
    seq.append(tag.lower())
    if(len(tag)<length):
        diff=length-len(tag)
        if(diff<3):
            rang = int(str(1)+diff*"0")
            for i in range(rang):
                seq.append(tag + str(i))
                seq.append(tag.upper()+str(i))
                seq.append(tag.lower()+str(i))
                seq.append(string.capwords(tag)+str(i))
        if((length-(len(tag)+len(otherTag))<3)):
             for i in range(diff):
                seq.append(tag + otherTag + str(i))
                seq.append(tag.upper()+ otherTag.upper() +str(i))
                seq.append(tag.lower()+ otherTag.lower() +str(i))
                seq.append(string.capwords(tag)+ otherTag +str(i))
    seq.append(tag+otherTag)
    seq.append(string.capwords(tag))
    seq.append(string.capwords(tag)+otherTag)
    seq.append(tag+string.capwords(otherTag))
    seq.append(string.capwords(tag)+string.capwords(otherTag))
    return seq
        
    
#Generates the passwords with the
#pattern information
def gen(person,pat):
    file = open(person.name+".txt","a")
    person.sort_tags() #The tags are now sorted by their priority
    count=0
    for i in person.tags:
        for w in person.tags:
            #The real generation sequence
            passWS = generateSequenceOfTag(i.name,w.name,pat.max_length)
            for passW in passWS:
                if(confirmedPattern(passW,pat)):
                    file.write(passW+"\n")
                    count+=1
    print("finished with "+str(count)+" results")
    print("Saved to " + person.name+".txt")

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
    print("Add Tags > name,priority (1-10)")
    print("Birthday,Name,Age,Name of Pet ect...")
    while(True):
        i=input("TAG>")
        if(i!=""):
            pers.add_tag(str(i.split(',')[0]).strip(),int(i.split(",")[1]))
        else:break
    gen(pers,pat)
    
def generate_list(argv):
    if(argv==None):
        generate_manually()


generate_list(None)
