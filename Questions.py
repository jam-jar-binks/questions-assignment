import time
import random

random.seed()
qs = random.randint(3,6)
qc = 1
fail = False

#questions

q0 = ("What is your name?","meaningless")
q1 = ("What is your favorite colour?","meaningless")
q2 = ("Who is the queen of England?","Queen Elizabeth II")
q3 = ("What the square root of 16?","4")
q4 = ("What continent is Italy located?","Europe")
q5 = ("What is your dream job?","meaningless")
q6 = ("What is the 5th planet from the sun?","Jupiter")
q7 = ("Is Pluto a planet?","yes")
q8 = ("When did D-Day take place?","June 6th, 1944")
q9 = ("Where is the Eiffel Tower located?","Paris")

var = [q0,q1,q2,q3,q4,q5,q6,q7,q8,q9]
q = random.sample(var,qs)
# intro
print("Answer me these questions three to six, Or your data shall be nix'd!")

#ask questions
time.sleep(0)
for _i in q:

    print("question " + str(qc))
    print(_i[0])
    answer = input()
    time.sleep(2)
    if _i[1] != "meaningless":
        if answer.casefold() != _i[1].casefold():
            print("The Answer was {}.".format(_i[1]))
            fail = True
            break
        
    qc = qc + 1
    

#win/lose
if fail == True:
    print("You have failed! No more data!")
    time.sleep(3)
else:
    print("You have answered my questions, you may keep your data.")
    time.sleep(3)
