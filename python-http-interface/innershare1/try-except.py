'''
1.首先执行try语句，捕捉try程序块下的异常情况
2.若未捕捉到异常，则忽略except字句，try子句继续执行
3.若捕捉到异常，try语句将异常传递给except，异常的类型与某个except之后的名称相符那么执行该except下的语句
4.如果异常没有已有的except匹配，则这个异常传递到解释器中
5.else是可选子句，没有发生任何异常时执行的代码。
6.无论有没有异常时均执行
7.raise 语句抛出一个指定的异常
'''

try:
    a=input("请输入一个数字：")
    x=int(a)
    if x>20:
         raise Exception('x 不能大于 20')
    print("输入的数字是:",x)
except ValueError:
    print("你输入的格式是：",type(a),"，请再次输入!")
else:
    print("无异常时执行")
finally:
    print("无论有没有异常时均执行")