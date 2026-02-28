import random as rd
import time

def numSel():
    
    botNumbers=rd.randint(0,9)
    return botNumbers

def timming():
    timmer = time.time()
    return timmer


hast=timming()       
print(hast)
    

value1=numSel()
value2=numSel()
print(value1,'+',value2,'?')
answer=value1+value2
userAns=int(input('Enter the answer '))



if userAns==answer:
    print("Yes the answer is ",answer)
else:
    print('You are wrong!. The answer is ',answer)
