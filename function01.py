#函数
def func(a,b):
    print("11")
    print("a= %s" %a )
    
    
func(1,2);

#可变参数的个数

def howlong(first,*other):
    return 1+len(other)

# print(howlong(1,2,3,3,4,5))


#函数迭代器和生成器

#iter() next（）

list1 = [1,2,4]

#迭代器 iter() next()
it=iter(list1)
print(next(it)) #1
print(next(it)) #2

#生成器 yeild
def  frange(start,stop,step):
    x= start
    while x < stop:
        yield x
        x = x + step
        
for i in frange(1,10,2):
    print(i)

#lambda 表达式

lambda: True

lambda x,y : x+y

#内置函数 filter（），map（），reduce（），zip

def func():
    a=1
    b=2
    return a+b

#闭包
def sum(a):
    def add(b):
        return a+b
    return add

num1 = sum(2)
print(num1(4))

## 闭包实现计数器
#
def counter(first=0):
    cnt=[first]
    def add_ond():
        cnt[0] +=1
        return  cnt[0]
    return add_ond
num1 = counter(3)
print(num1())
print(num1())

#闭包的使用
def a_line(a,b):
    def y_value(x):
        return a*x+b
    return y_value

y1= a_line(2,5)
print("闭包：",y1(3))

def b_line(a,b):
    return lambda x: a*x+b
y2=b_line(2,6)
print(y2(2))
#装饰器 aop
def timer(func):
    def wrapper():
        print('2323')
        func()
        print("ghjkghjk")
    return wrapper
 #语法
@timer
def zhuangshiqi():
    print("-----")
timer(zhuangshiqi())
#自定义上下文管理器
with open("name.txt") as f:
    for i in f.readline():
        print(i)
#模块的定义

# import 模块名称
# form 模块名称 import 方法名
import time as t
form time import sleep

#pep8编码规范 官网有规范文档