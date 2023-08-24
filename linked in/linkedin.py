"""print ("i create an account in linked in ")
fruits = ["apple", "banana", "cherry"]
for apple in fruits:
  print("*")
  
def pattern(n):
      k = 2 * n - 2
      for i in range(0,n):
           for j in range(0,k):
               print(end=" ")
           k = k - 1
           for j in range(0, i+1):
                print("*", end=" ")
           print("")
  
pattern(20)
a = int(input('Enter the number a:'))
b = int(input('Enter the number b:'))
for a  in range(0,10):

    print (a,b)
for b in range (0,20):
    print(b,a)"""

a = int(input('Enter the number a:'))
b = int(input('Enter the number b:'))
c = str(input('Enter the number c:'))
for a in range (0,100):
    print (end=" ")
if c == '*':
    print (a*b)
elif c=='-':
    print (a-b)
elif c=='+':
    print (a+b)
elif c=='/':
    print (a/b)
else :
    print ("error")
