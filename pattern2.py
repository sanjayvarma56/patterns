# Take the number of rows from the user
# Loop through each row
# Print stars in the current row
# Move to the next line after each row
# Define a class named pattern
# Method to print a right triangle pattern
# Loop through each row
# Print stars in the current row
# Move to the next line after each row
# Create an object of the pattern class
# Print a right triangle with 4 rows
# Print a right triangle with 2 rows

#Right Triangle    
n=int(input("Enter the number: "))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    print()

#OR

class pattern:
    def right_triangle(self,n):
        for i in range(0,n):
            for j in range(0,i+1):
                print("*",end=" ")
            print()
s = pattern()
s.right_triangle(4)
s.right_triangle(2)
