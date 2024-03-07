import os,random,time as t

def rand():
    x =random.randrange(1,3)
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
        return ( (( ((0,0),(1,0)) [y==2 and z==1]),(0,1)) [y==2 and z==3] )
    elif(y==3):
        return ( (( ((0,0),(0,1)) [y==3 and z==1]),(1,0)) [y==3 and z==2] )

    return a1,a2

user=comp=0

while(True):
    
    os.system('cls')
    
    print(" \n 1:Rock \n 2:Paper \n 3:Scissor")
    y=int(input())
    
    os.system('cls')
    
    print("Your choice = ")
    choice(y)
    
    t.sleep(1.5)
    
    if(y<1 or y>4):
        print("Wrong Choice .. \n Restarting")
        continue
    
    z=rand()
    print(" \n \n For Computer :")
    choice(z)
    
    t.sleep(2)
    
    os.system('cls')
    
    c1,c2=logic(y,z)
    
    if(c1==c2):
        print("\n Its a Draw !")
    elif(c2>c1):
        print("\n Computer Won!")
    else:
        print("\n User Won !")
    
    t.sleep(3)
    another_game=input("Another Calculation : ? \n Yes ? or No ? ").lower()
    if another_game != 'yes':
        break
    
    