#异常

try:
    year =int(input("输入年份："))
except ValueError as e:
    print("need number",e)
finally:
    print("不管是否发生异常，都执行，一般关闭文件")