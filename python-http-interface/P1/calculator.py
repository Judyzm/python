
def add(num1,num2):
    return num1+num2
def minus(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
operatorDic={
    '1':['+',add],
    '2':['-',minus],
    '3':['*',multiply],
    '4':['/',divide]
            }

operator=input('''选择运算:
1 is +
2 is -
3 is *
4 is /
请输入你的选择（1/2/3/4）:
''')

if (int(operator)<1 or int(operator)>4):
    print("这不是一个合法的运算符")
else:
    num1 = int(input("请输入第一个数："))
    num2 = int(input("请输入第二个数："))
    print("{0}{1}{2}={3}".format(num1,operatorDic[operator][0],num2,operatorDic[operator][1](num1,num2)))