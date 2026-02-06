a =int(input("Enter a Variable 1:"))
b =int(input("Enter a Variable 2:"))
temp = a
a = b
b = temp
print("value of a:",a)
print("value of b:",b)
#method 2
x =40
y = 33
x,y = y,x
print(x)
print(y)