
#numpy 用于高性能科学计算和数据分析，是常用的高级
#数据分析库的基础包

#1.安装 numpy pip3 install numpy

import numpy as np

arr1 = np.array([1,24,3,4])

print(arr1)
print(arr1.dtype)
print(arr1*10)

data = [[1,2,3],[4,5,6]]

arr2 =np.array(data)
print(arr2)

print(np.zeros(10)) #一位数组10个都是0 
print(np.ones(10)) #一位数组10个都是0 
print(np.empty([2,3,2])) #一位数组10个都是0 

arr3 = np.arange(10)
arr3[5:8] =10
print(arr3)

arr_slide = arr3[5:8].copy()
arr_slide[:] = 15
print(arr_slide)

print(arr3)