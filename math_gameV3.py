import random as rd
import time

settime=3 # You can set here your own time in seconds
while True:
    def question():
        value=rd.randint(0,9)
        return value



    fstnumber= question()
    secnumber=question()

    print(f'{fstnumber} + {secnumber} ?')
    answer = fstnumber+secnumber
    intial_time=time.time()
    userValue=input('your value : ')
    try :
        useCon = int(userValue)
    except:
        print('Charactes aren\'t allowed!')
        continue
    final_time= time.time()-intial_time

    if answer==useCon:
        if settime>=final_time:
            print(f'oww you are right, the answer is {answer} time taken {final_time:.2f} sec speedy!')
        else:
            print(f'You are right!, the answer is {answer} but you took {final_time:.2f} sec')
    else:
        print(f'Your answer is wrong the answer is {answer}')
