x=0
for x in range (0,25):
    print (x**x)
    x+=1
x=0
while x<15:
    z=int (input("enter value of z "))
    print (x*z)
    x+=1
while True :
     z=str (input("enter value of z : "))
     
     if z =="x":
        print ("end of the game")
     try : 
        z=int(z)
        if z%2==0:
            print ("even")
        else :
            print ("odd")
    
     
     except ValueError:
        print ("enter a valid number")
    
