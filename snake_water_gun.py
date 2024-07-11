'''
snake 1
gun -1
water 0'''
import random
computer= random.choice([-1,0,1])

you=input("Enter your choice:")
dic={"s":1,"g":-1,"w":0}
revdic={-1:"Gun",0:"Water",1:"Snake"}
younum=dic[you]
print("You choose : ",revdic[younum],"\nComputer choose : ",revdic[computer])

if(computer == younum):
    print("It is a draw:")
else:
    if(computer==1 and younum==0):
        print("You loose!")
    elif(computer==1 and younum==-1):
        print("You win!")
    elif(computer==0 and younum==-1):
        print("You loose!")
    elif(computer==0 and younum==1):
        print("You win!")
    elif(computer==-1 and younum==0):
        print("You win!")
    elif(computer==-1 and younum==1):
        print("You loose!")
    else:
        print("Something went wrong")
    