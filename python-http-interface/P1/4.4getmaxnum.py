str=input("请输入三个数字，用空格分开:")
num1,num2,num3=str.split()
if (num1>num2)and (num2>num3):
    print("最大数为:",num1)
elif (num1<num2) and (num2<num3):
    print("最大数为：",num3)
else:
    print("最大数为：",num2)
