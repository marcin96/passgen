#Author Marcin Cherek
#Language: Python 3.4
#Version 1.0
#License: MIT

#Designed to check the strength of a password
import re
import tag

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

#Checks if the password has special characters
def hasSpecialSymbols(passW):
    if(re.match(r'^_-:,;<>+"*ç%&/()=?"',passW)):
        return True
    return False

#Checks if the password has no connectio
#To the informations about the person
#Returns the strength of the Connection 0-10
def hasConnection(passW,tags):
    connection=0
    for i in tags:
        if(i.name.lower() in passW.lower()):
            connection += i.priority/2
    return connection

#Checks if the passWord has repeating patterns
def checkForRepeatingPatterns(passW):
    r = re.compile(r"(.+?)(?=\1)")
    return len(r.findall(passW))
    
#returns a integer from 0 to 10
#Specifies the strength of a password
def evaluate(passW,tags):
    #Check length
    points = len(passW)/10
    if(hasCapitalLetters(passW)):points+=1
    if(hasNumber(passW)):points+=1
    if(hasSpecialSymbols(passW)):points+=1
    points-=hasConnection(passW,tags)
    points-=checkForRepeatingPatterns(passW)/2
    return points

#
if __name__== "__main__":
    passW = input("password:")
    tags = []
    while(True):
        i = input("Tag>")
        if(i!=""):
            tags.append(tag.Tag(str(i.split(',')[0]).strip(),int(i.split(",")[1])))
        else:
            break
    print("strength:",evaluate(passW,tags))
