import calculator1

operator=int(input('''请选择运算符：
1 is +
2 is -
3 is *
4 is /
输入你的选择（1/2/3/4）:
'''))
if (operator<1 or operator>4):
    print("你的输入无效，请重新输入！")
else:
    num1 = int(input("请输入第1个数字："))
    num2 = int(input("请输入第2个数字："))
    if operator == 1:
        calculator1.add(num1,num2)
    if operator==2:
        calculator1.minus(num1,num2)
    if operator==3:
        calculator1.mult(num1,num2)
    if operator==4:
        calculator1.dev(num1, num2)
