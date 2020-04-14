import sys
class myExcption(Exception):
    def __init__(self,num,atmost):
        Exception.__init__(self)
        self.num=num
        self.atmost=atmost
# 自定义一个异常类，是exception的基类。

try:
    f=open("C:/Users/Administrator/Desktop/input.txt",'r')
    f2=open("C:/Users/Administrator/Desktop/output.txt",'w')

    for line in f:
        a=int(line)
        assert a>0
        if a>999:
           raise myExcption(a,999)

        # raise 语句抛出一个指定的异常,
        # 只有一个参数，指定了要被抛出的异常，它必须是一个异常的实例，或者异常的类.
        if a%3==0 and a%5==0:
            f2.write("FizzBuzz\n")
            continue
        if a%3==0:
            f2.write("Fizz\n")
            continue
        if a%5==0:
            f2.write("Buzz\n")
            continue
        else:
            f2.write(str(a)+"\n")
except OSError :
    # 发生异常时执行代码
    print("想要访问的文件不存在,请确认路径及文件正确!")
except ValueError:
    print("文件中包含字符串，请检查！",sys.exc_info())
except myExcption as ex:
    print(("触发了自定义异常！MyException:The num was "+"{0},expected smaller than {1}" ).format(ex.num,ex.atmost))
except :
    print("Unexpected error:", sys.exc_info())
else:
    print("未触发任何异常，按期望输出了结果!")
    # else 子句将在 try 子句没有发生任何异常的时候执行。
finally:
    try:
        print("close the files")
        f.close()
        f2.close()
    except NameError as e:
        print("Catch another Error: "+str(e))

