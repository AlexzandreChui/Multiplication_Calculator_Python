# Created By: Alex.C
# Created On: 2022/10/11
# This program calculates the product using only addition. 
print("Let's do Multiplication")
x = int(input("Enter your negative number:"))
y = int(input("Enter your positive number:"))

a = 0 

while y > 0:
    a += x
    y -= 1 
print("The product is "+str(a))