# a=b=c=1
# print(a , b , c)

# a=32
# print(a , b , c)
#You are developing a small calculator app. Write a program that takes two numbers from the user and swaps them without using a third variable, so users can correct their input order.


a = int(input("Num 1 "))
b = int(input("Num 2"))
print(a , b)
a = a+b
b= a-b
a = a-b 

print (a,b)