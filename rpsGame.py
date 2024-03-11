import os,random,time as t

def rand():
    x =random.randrange(1,3)
    choice(x)
    return x

def choice(x):
    match x:
        case 1:
            print("Rock")
        case 2:
            print("Paper")
        case 3:
            print("Scissor")

def logic(y,z):
    if(y==1):
        a1,a2= ( (( ((0,0),(1,0)) [y==1 and z==3]),(0,1)) [y==1 and z==2] )
    elif(y==2):
        a1,a2= ( (( ((0,0),(1,0)) [y==2 and z==1]),(0,1)) [y==2 and z==3] )
    elif(y==3):
        a1,a2= ( (( ((0,0),(0,1)) [y==3 and z==1]),(1,0)) [y==3 and z==2] )

    return a1,a2


user=comp=sc_Computer=sc_User=0

while(True):
    
    os.system('cls')
    
    print(" \n 1:Rock \n 2:Paper \n 3:Scissor \n ")
    y=int(input())
    if y not in (1,2,3):
        print("Wrong Choice .. \n Restarting")
        t.sleep(2)
        continue
    
    os.system('cls')
    
    print("Your choice = ")
    choice(y)
    
    t.sleep(1.5)
    
    print(" \n \n For Computer :")
    z=rand()
    
    t.sleep(2)
    
    os.system('cls')
    
    c1,c2=logic(y,z)
    
    if(c1==c2):
        print("\n Its a Draw !")
    elif(c2>c1):
        print("\n Computer Won!")
        sc_Computer+=1
    else:
        print("\n User Won !")
        sc_User+=1
    
    t.sleep(3)
    
    os.system('cls')
    
    print("Current Scores  " )
    print("User : ")
    print(sc_User)
    print("Computer : ")
    print(sc_Computer)
    
    t.sleep(3)
    os.system('cls')
    
    another_game=input("Another Calculation : ? \n Yes ? or No ? ").lower()
    if another_game != 'yes':
        break
