from random import randint
from time import sleep

print("Welcome to Cube Game\nEvery turn cost 3 ILS\n")
num=int((input("Enter how many ILS you have: ")))
turns=int(num//3)
print("\nYou have " + str(turns) + " turns\nYour change: " + str(num%3) + " ILS\n")

prize=0
for n in range(turns):
    print("\n----------------\n\nRound number: " + str(n+1) + "\n")
    cube1=randint(1,6)
    cube2=randint(1,6)
    print("cube1: " + str(cube1) + "\ncube2: " + str(cube2))
    if(cube1==cube2):
        if(cube1==6):
            prize=prize+1000
        else:
            prize=prize+100
    elif(cube2==2):
        prize=prize+40
    elif(cube1==1):
        prize=prize+20
print("\n----------\nCalculating Your Price...\n")
sleep(3)
print("Your Prize: " + str(prize) + " ILS")

