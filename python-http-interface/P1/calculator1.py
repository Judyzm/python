class Mycalculator:
    '''这是我的的计算器'''
    def __init__(self):
        pass
    def add (self,num1,num2):
        print("{0}+{1}={2}".format(num1,num2,num1+num2))
    def minus(self,num1,num2):
        print("{0}-{1}={2}".format(num1,num2,num1-num2))
    def multiply(self,num1,num2):
        print("{0}*{1}={2}".format(num1,num2,num1*num2))
    def devide(self,num1,num2):
        print("{0}/{1}={2}".format(num1,num2,num1/num2))

    def __del__(self):
        pass

calc=Mycalculator()
operator=input("""选择运算符：
1 is +
2 is -
3 is *
4 is /
请输入你的选择（1/2/3/4）:""")
if (int(operator)<1 or int(operator)>4):
    print("这不是一个合法的运算符")
else:
    num1 = int(input("请输入第一个数："))
    num2 = int(input("请输入第二个数："))
    if (operator=="1"):
        calc.add(num1,num2)
    #if (operator == "4"):
        # print (calc.devide(num1, num2))
    if (operator=="2"):
        calc.minus(num1, num2)
    if (operator=="3"):
        calc.multiply(num1,num2)
    if (operator=="4"):
        calc.devide(num1,num2)

