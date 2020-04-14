import random
# 生成24个随机的整数，并写到input文件中，用\n换行
f=open("E:/2020test/input.txt",'w')
a=1
while a<=24:
    i=random.randint(3,100)
    f.write(str(i)+'\n')
    a=a+1
f.close()
# 定义一个类，实现转换。
class FizzBuzz():
    def getFizzBuzz(self,num):
        if num%3==0 and num%5==0:
            return "fizzbuzz"
        if num%3==0:
            return "fizz"
        if num%5==0:
            return "buzz"
        else:
            return str(num)

fb=FizzBuzz() #类的实例化

f=open("E:/2020test/input.txt",'r')
f2=open("E:/2020test/output.txt",'w') #生成一个output文件
for line in f:
    num2=int(line)  #line是字符串，没办法被getfizzbuzz使用，int转换下格式。
    x=fb.getFizzBuzz(num2)
    #print(x)
    f2.write(x+"\n")  #转换后的字符串写到output文件中
f.close()
f2.close()














