# problem 1
s = 'Beautiful palace'
print(s[:])
print(s[::])
first_five_chars = s[:5]
print(first_five_chars)
third_to_fifth_chars = s[2:5]
print(third_to_fifth_chars)




# problem 2
py_string = 'learn python'
slice_object1 = slice(-1, -6, -1)
slice_object2 = slice(1, 6, -1)
slice_object3 = slice(1, 6, 1)
print(py_string[slice_object1], py_string[slice_object2],py_string[slice_object3])





# Problem 3
s = 'Learning is FUN'
reverseString = s[::-1]
print(reverseString)
s1 = s[2:8:2]
print(s1)
s1 = s[8:1:-1]
print(s1)

s1 = s[-4:-2]
s1 = s[8:1:-2]
print(s1)


s1 = s[-4:-2]
print(s1)

s = 'Python'
s1=s[100:]
print(s1)
s1= s[2:50]
print(s1)


# Problem 4
py_string = 'Python book'
slice_object = slice(3)
print(py_string[slice_object])

slice_object = slice(1, 6, 2)
print(py_string[slice_object])

# Problem 5
py_list = ['P', 'y', 't', 'h', 'o', 'n']
py_tuple = ('P', 'y', 't', 'h', 'o', 'n')

slice_object = slice(3)
print(py_list[slice_object])

slice_object = slice(1, 5, 2)
print(py_tuple[slice_object])
slice_object = slice(-1, -4, -1)
print(py_list[slice_object])

slice_object = slice(-1, -5, -2)
print(py_tuple[slice_object])




# """

# output

# Beautiful palace
# Beautiful palace
# Beaut
# aut
# nohty  earn 
# NUF si gninraeL
# ann
#  gninra
#  nna
#  F

# thon
# Pyt
# yhn
# ['P', 'y', 't']
# ('y', 'h')
# ['n', 'o', 'h']
# ('n', 'h')


# """