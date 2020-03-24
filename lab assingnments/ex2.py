#Problem1
a=5
house_number=300             #created an int object and created an object reference to var 1
print(house_number,a)

#problem2
myhousenumber=house_number #assignment
b=a
print(myhousenumber,b)
print(type(house_number),b)

ourHouse =int(house_number)
c=int(b)
print(ourHouse,c)

#Problem 3
a=3+5
b=5-4
c=(3*3)+6
d=b/a  #perfoms floating point division
e=b//a #performs integer division
f=e
f+=5  #combining operators
print(a,b,c,d,e,f)

#Problem 4
m=0b10 #base2
print(m)
n=0o10 #base 8
print(n)
p=0x4 #base 10
print(p)
numbersize=10**100 #no limitations on size
numbersize=numbersize*numbersize
print(numbersize)


#problem5
#real numbers
a=6.022-15.9997
c=42.0
s=2.143e4
print(a,c,s)


#problem 6
hello="Good morning"
print(hello)
print('what is your name?')
myName=input() #user input
print('it is good to meet you,'+myName)


#strngs operations 
str1="hello"+"world"   #concatenation
str2="hello"*3   #reptition
str3="hello"[0]  #indexing
str4="hello"[-1] #from end
str5="hello"[1:4] #slicing
str6=len("hello") #size
print(str1+'\n',str2+'\n'+str3+'\n',str4+'\n'+str5+'\n',str6)



# """    
# output


# 300 5
# 300 5
# <class 'int'> 5
# 300 5
# 8 1 15 0.125 0 5
# 2
# 8
# 4
# 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# -9.9777 42.0 21430.0
# Good morning
# what is your name?
# venky
# it is good to meet you,venky
# helloworld
#  hellohellohello
# h
#  o
# ell
#  5



#  """