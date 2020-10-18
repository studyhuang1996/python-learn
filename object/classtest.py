#创建一个User类
class User():
    def __init__(self,name,age):
        self.__name=name  #私有属性，封装
        self.age = age
    def print_name(self):
        print('%s:%s' %(self.__name,self.age))

user1 = User("huang",18)
user2 =User('qianxu',18)
user1.print_name()
user2.print_name()

user1.name={'aaa'}
user1.print_name()