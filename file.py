#文件的内建函数

# #1.打开文件,
# file_test = open("name.txt","w")
# #写入文件信息
# file_test.write("python文件内建函数")
# #关闭
# file_test.close()

# #2.读取文件
# file2=open("name.txt")

# print(file2.read())
# file2.close()

# #3.追加写文件
# file3=open("name.txt","a")
# file3.write(" 追加写入文件信息，a")
# file3.close()

#4.读取一行
# file4=open("name.txt")
# print(file4.readline())

#逐行读取
# file5=open("name.txt")
# for i in file5.readlines():
#     print(i)
#     print("=====")
# file5.close()


#seek

file6=open("name.txt")
#文件的读取位置
print("当前文件位置:",file6.tell()) #打印0
#读取1个字符
file6.read(1)
print(file6.tell()) #打印 1
#重置位置
file6.seek(0)
print(file6.tell()) #打印 1
file6.close()

