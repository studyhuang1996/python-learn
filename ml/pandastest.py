
#数据预处理和清洗的工具
#pip3 install --index-url https://pypi.tuna.tsinghua.edu.cn/simple/ pandas
import pandas as pd
from pandas import Series,DataFrame

obj=Series([2,3,5,6])

print(obj)
print(obj.index)
print(obj.values)


#dateframe

data= {'city':['shanghai','beijing','shanghai'],
       'year':[2017,2018,2019],
       'pop':[1.5,1.7,3.6]}

frame=DataFrame(data)
print(frame)