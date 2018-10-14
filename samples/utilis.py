# This is sample utility program

print("This is sample Utility program")

if 77 > 22 :
	print("77 is bigger")
else :
	print("22 is Smaller")

#Variables
x = 100
y = "RAM"
z = y + "Kumar"

print("This is y: " + y)
print("This is Z: " + z)

print(type(x))

if x == y :
	print("x and y are equal")
else :
	print("x and y are not equal")

#Numbers
print("The Numbers")
a = 10
b = 7.7
c = 10e3 #10000
d = 7+7j

print(type(a))
print(type(b))
print(c)

print(type(d))
print(d)

#casting (int,float and str)
print("The Casting")
id1 = int(7)
id2 = int(8.7)
id3 = int("9")

print(id1)
print(id2)
print(id3)

ft1 = float(6)
ft2 = float(7.7)
ft3 = float("8")
ft4 = float("9.9")

print(ft1)
print(ft2)
print(ft3)
print(ft4)

st1 = str("7")
st2 = str("9.9")
st3 = str("RK")

print(st1)
print(st2)
print(st3)

#Strings
print("Python Strings")

str1 = str(' Ram,kumar ')
print(str1[1])
print(len(str1)) # prints length
str1 = str1.strip()
print(len(str1))
print(str1.strip()) # strips white spacess begining and end
print(str1[3:8]) # prints kumar exclusive of 3 and 8 positions
print("Upper: " + str1.upper())
print ("Lower: " + str1.lower())

print(str1.replace('k', 'K'))
print(str1.split(','))

#Taking input from user
print("Enter your Name:")
name=input()
print("Hi " + name)


	
