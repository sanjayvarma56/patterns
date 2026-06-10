#Incremental Number Triangle Pattern
n=int(input("Enter the number: ")) 
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#Incremental Number Triangle
n=int(input("Enter the number: "))
for i in range(0,n):
    for j in range(0,i+1):
        print(j+1,end=" ")
    print()

class pattern:
    def incremental_number_triangle(self, n):
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()
s = pattern()
s.incremental_number_triangle(4)
s.incremental_number_triangle(2)