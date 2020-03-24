#using arrays,create a linear method of time complexity problem
 
import array as a
import time
import matplotlib.pyplot as graph
import sys
print('enter loop value:',end='')
input_value=input()

#initilise/create an array
temp=a.array('i',[2,3,4,6,7,8,9])
array_size=sys.getsizeof(temp)
block_size=sys.getallocatedblocks()
total_time_array=[]
arr_len=[]
print('initial allocated list size:',sys.getsizeof(arr_len))
print('array size and block size beforre the execution:',array_size,block_size)
start_time=time.time()                 #capture starting execution time

#increasing array length every time by 4 times
for run_loop in range(0,int(input_value),1):
     arr_len.append(len(temp))
     for k in range(0,10000): 
          t=0
     for j in range(1,5):
         temp.append(run_loop+j)
         
     end_time=time.time()    #capture starting execution time
     total_time=round((end_time-start_time),7)
     total_time_array.append(total_time)
     
     run_loop+=run_loop

#plot the graph of execution time versus input size
array_size=sys.getsizeof(temp)
print('final list size:',sys.getsizeof(arr_len))
print('array size and block size after the execution: ',array_size,block_size) 
s=total_time_array  #execution time
p=arr_len            #array size
#print(s,p)
graph.plot(p,s)          # plot the graph (x axis=array size,y axis+execution time)
graph.show()

print(s,p)


# OUT PUT
# enter loop value:100
# initial allocated list size: 64
# array size and block size beforre the execution: 92 254411
# final list size: 912
# array size and block size after the execution:  1704 254411
# [0.0, 0.0010273, 0.0010273, 0.0020251, 0.0020251, 0.0030239, 0.0030239, 0.0040214, 0.0040214, 0.0049891, 0.0049891, 0.0059872, 0.0059872, 0.0069842, 0.0069842, 0.0080101, 0.0080101, 0.0080101, 0.009007, 0.009007, 0.0100038, 0.0100038, 0.0110011, 0.0110011, 0.0119989, 0.0119989, 0.012996, 0.012996, 0.0139954, 0.0139954, 0.0149913, 0.0149913, 0.0149913, 0.0159914, 0.0159914, 0.0169849, 0.0169849, 0.0179868, 0.0179868, 0.0189824, 0.0189824, 0.0199492, 0.0199492, 0.0209477, 0.0209477, 0.0219438, 0.0219438, 0.0229707, 0.0229707, 0.0239389, 0.0239389, 0.0249362, 0.0249362, 0.0259323, 0.0259323, 0.0269294, 0.0269294, 0.0279267, 0.0279267, 0.028924, 0.028924, 0.0299215, 0.0299215, 0.0309188, 0.0309188, 0.0319159, 0.0319159, 0.0319159, 0.0329134, 0.0329134, 0.0339108, 0.0339108, 0.0349081, 0.0349081, 0.0359054, 0.0359054, 0.0369031, 0.0369031, 0.0379002, 0.0379002, 0.0389268, 0.0389268, 0.0399244, 0.0399244, 0.0409214, 0.0409214, 0.041918, 0.041918, 0.0429158, 
# 0.0429158, 0.0429158, 0.0439148, 0.0439148, 0.0449104, 0.0449104, 0.0459099, 0.0459099, 0.046905, 0.046905, 0.0479031] [7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79, 83, 87, 91, 95, 99, 103, 107, 111, 115, 119, 123, 127, 131, 135, 139, 143, 147, 151, 155, 159, 163, 167, 171, 175, 179, 183, 187, 191, 195, 199, 203, 207, 211, 215, 219, 223, 227, 231, 235, 239, 243, 247, 251, 255, 259, 263, 267, 271, 275, 279, 283, 287, 291, 295, 299, 303, 307, 311, 315, 319, 323, 327, 331, 335, 339, 343, 347, 351, 355, 359, 363, 367, 371, 375, 379, 383, 387, 391, 395, 399, 403]
# PLEASE SEE GRAPH AS OUTPUT