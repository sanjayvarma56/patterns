#Approach for Incremental Number Triangle
n=int(input("Enter the number: "))
for i in range(0,n):
    for j in range(0,n):
        print(i,end=" ")
    print()

#NEXT

n=int(input("Enter the number: "))
for i in range(0,n):
    for j in range(0,n):
        print(j,end=" ")
    print()

#NEXT 
  
n=int(input("Enter the number: "))
for i in range(0,n):
    for j in range(0,n):
        print(j+1,end=" ")
    print()

#NEXT
   
n=int(input("Enter the number: "))
for i in range(0,n):
    for j in range(0,i):
        print(j+1,end=" ")
    print()

#OR
class pattern:
    def triangle(self,n):
        for i in range(0,n):
            for j in range(0,i):
                print(j+1,end=" ")
            print()
s = pattern()
s.triangle(4)
s.triangle(2)
