# ex1
a_list = [84,84,86,86,85,85,85,83,23,45,84,1,2,]
def first_second(given_list):
    a = given_list
    a.sort(reverse=True)
    print(a)
    first = a[0]
    second = None
    for element in a_list:
        if element != first:
            second = element
            return first, second

f,s = first_second(a_list)
print(f,s)

# ex2


firstMatrix = [[1,2,3],[4,5,6],[7,8,9]]
secondMatrix = [[1,0,1],[1,1,0],[1,1,1]]
thirdMatrix = [[2,0],[0,2]]
def sum_of_diagonal(matrixItems):
    sum = 0
    for i in range(len(matrixItems)):
        sum += matrixItems [i][i]
        return sum
print("First Matrix:",sum_of_diagonal(firstMatrix))
print("Second Matrix:",sum_of_diagonal(secondMatrix))
print("Third Matrix:",sum_of_diagonal(thirdMatrix))


# prob 2

listItems = ["Karnataka", "Bihar", 500,"Kerala", "Jammu", "Telangana",340,"Maharastra","Gujarat", 1000, 2000]
str_items = []
num_items = []
for item in listItems:
    if isinstance(item, str):
        str_items.append(item)
    elif isinstance(item,int) or isinstance(item, float):
        num_items.append(item)
print(str_items)
print(num_items)
str_asc_items =str_items.sort(key=str.lower)
print(str_asc_items)
str_des_items = str_items.sort(key=str.lower, reverse=True)
print(str_des_items)
num_sortlow_items = num_items.sort()
print(num_sortlow_items)
num_sorthigh_items = num_items.sort(reverse=True)
print(num_sorthigh_items)
#
# 
# 
# 
my_tuple = ()
print(my_tuple)
my_tuple = (1, 2, 3)
print(my_tuple)
my_tuple = (1, "Hello", 3.4)
print(my_tuple)
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

# indexing
my_tuple = ('p','é','r','m','i','t')
print(my_tuple[0])
print(my_tuple[5])
n_tuple =('mouse',[8,4,6],(1,2,3))
print(n_tuple[0][3])
print(n_tuple[1][1])
my_tuple = (4, 2, 3, [6, 5])
my_tuple[3][0] = 9
print(my_tuple)

my_tuple= ('p','r','o','g','r','a','m','i','z')
print(my_tuple)

del my_tuple
# print(my_tuple)


# """


# output


# [86, 86, 85, 85, 85, 84, 84, 84, 83, 45, 23, 2, 1]
# 86 85
# First Matrix: 1
# Second Matrix: 1
# Third Matrix: 2
# ['Karnataka', 'Bihar', 'Kerala', 'Jammu', 'Telangana', 'Maharastra', 'Gujarat']
# [500, 340, 1000, 2000]
# None
# None
# None
# None
# ()
# (1, 2, 3)
# (1, 'Hello', 3.4)
# ('mouse', [8, 4, 6], (1, 2, 3))
# p
# t
# s
# 4
# (4, 2, 3, [9, 5])
# ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
# """