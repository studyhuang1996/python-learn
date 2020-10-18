
#pip3 install --index-url https://pypi.tuna.tsinghua.edu.cn/simple/ matplotlib
#pip3 install --index-url https://pypi.tuna.tsinghua.edu.cn/simple/ seaborn 
#绘图

import matplotlib.pyplot as pyplot

#绘制简单的曲线

#pyplot.plot([1,3,5],[4,8,10])
#pyplot.show()

import numpy as np

x= np.linspace(-np.pi,np.pi,100) #定义-3.14~3.14中，中间有100个数字
pyplot.plot(x,np.sin(x))
pyplot.show()