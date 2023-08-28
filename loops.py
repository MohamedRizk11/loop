while True :
    x= int(input("inter the number :"))
    
    for x in range (x,x+1):
        for y in range (0,13):
            print (f"{x} X {y} = {x*y}")
    print("number\tsquare")       
    for x in range (0,66):
        print("-----------------------------")
        print(x,"\t",x**2)
cols=int(input("inter number of cols:"))
rows=int(input("inter number of rows:"))
for x in range(rows):
    for y in range (cols):
        print("*",end="love you")
    print(" ")    
        
