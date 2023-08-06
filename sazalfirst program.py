
a = 3
b = 4

print("the value of 3+4 is ", 3+4)
print("the value of 3-4 is ", 3-4)
print("the value of 3*4 is ", 3*4)
print("the value of 3%4 is ", 3%4)

#assignment operators

a = 34
a -= 12
a *= 12
a %= 12

#camparison operators

b = (14<=7)
b = (14>=7)
b = (14<7)
b = (14>7)
b = print(14==7)
print(b)


#logical operators
bool1 = True
bool2 = False
print("The value of bool1 and bool2 is", (bool1 and bool2))
print("The value of bool1 or bool2 is", (bool1 or bool2))
print("The value of not bool2 .is", (not bool2))


#typecasting

a = "3534"
a = int(a)
# print(type(a))
print(a+5)


a = input("Enter your name: ")
a = int(a) #convert a to an integer
print(type(a))

a = input("Enter first number: ")
b = input("Enter second number: ")
a = int(a)
b = int (b)
avg = (a+b)/2
print("The average of a and b is", avg)

#ch - 3 STRING

a = 34
b = "sazal's" #--> use this if you have single quotes in your strings
# = 'harry"s'
b = '''harry"s and
harry's'''
print(a, b)
print(type(b))
# print(type(b))

greeting = "Good morning, "
name = "sazal"
#print(type(name))
c = greeting + name
print(c)
