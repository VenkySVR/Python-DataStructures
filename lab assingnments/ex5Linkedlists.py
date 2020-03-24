import math
import sys
class Node: 
     def __init__(self, data):
         self.data = data 
         self.next = None 
def insert(root, item): 
     temp = Node(item)
     if (root == None):
         root = temp
     else :
         ptr = root
         while (ptr.next != None):
              ptr = ptr.next
         ptr.next = temp
     return root
def display(newlist): 
     while (newlist!= None) :
         print(newlist.data, end = " ")
         newlist = newlist.next 
def arrayToList(arr, n): 
     newlist = None
     for i in range(0, n, 1):
         newlist = insert(newlist, list[i])
         print(sys.getsizeof(newlist)) 
     return newlist

if __name__=='__main__':
     list = [100, 2.5, "xyz", 40, 56.6]
     n = len(list)
     newlist = arrayToList(list, n)
     print("Linked list size in bytes : ", sys.getsizeof(newlist), "list Array size in bytes ", sys.getsizeof(list))
     display(newlist)
class Rectangle:
     def __init__(self, length, breadth):
         self.length = length
         self.breadth = breadth
     def area(self):
         return self.length*self.breadth
# breadth = 120 units, length = 160 units, 1 sq unit cost = Rs 2000
r=Rectangle(160, 120)
z=r.area()
print("Area of Rectangle: %f sq units"%(z))




# OUTPUT
# 56
# 56
# 56
# 56
# 56
# Linked list size in bytes :  56 list Array size in bytes  104
# 100 2.5 xyz 40 56.6 Area of Rectangle: 19200.000000 sq units