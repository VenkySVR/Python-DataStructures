import operator
# problem 1
a = 4
b = 3

print ("The addition of numbers is :",end="")
print (operator.add(a, b))

print ("The difference of numbers is :",end="")
print (operator.sub(a, b))

print ("The product of numbers is :",end="")
print (operator.mul(a, b))

#problem 2
a = 5
b = 2
print ("The true division of numbers is : ",end="")
print (operator.truediv(a,b))
print ("The floor division of numbers is : ",end="")
print (operator.floordiv(a,b))

print ("The exponentiation of numbers is : ",end="")
print (operator.pow(a,b))

print ("The modulus of numbers is : ",end="")
print (operator.mod(a,b))

# problem 3

a = 3
b = 3

if(operator.lt(a,b)):
    print ("3 is less than 3")
else : print ("3 is not less than 3")


if(operator.le(a,b)):
    print ("3 is less than or equal to 3")
else : print ("3 is not less than or equal to 3")

if (operator.eq(a,b)):
    print ("3 is equal to 3")
else : print ("3 is not equal to 3")


# problem 4
a = 4
b = 3
if (operator.gt(a,b)):
    print ("4 is greater than 3")
else : print ("4 is not greater than 3")

if (operator.ge(a,b)):
    print ("4 is greater than or equal to 3")
else : print ("4 is not greater than or equal to 3")

if (operator.ne(a,b)):
    print ("4 is not equal to 3")
else : print ("4 is equal to 3")


# """
# output 


# The addition of numbers is :7
# The difference of numbers is :1
# The product of numbers is :12
# The true division of numbers is : 2.5
# The floor division of numbers is : 2
# The exponentiation of numbers is : 25
# The modulus of numbers is : 1
# 3 is not less than 3
# 3 is less than or equal to 3
# 3 is equal to 3
# 4 is greater than 3
# 4 is greater than or equal to 3
# 4 is not equal to 3

# """