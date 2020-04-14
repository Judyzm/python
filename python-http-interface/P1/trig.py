n=int(input("请输入星星层数喔："))
for i in range(1,n+1):
    print((n-i)*" ",end=" ")
    print((2*i-1)*"*")
print("星星出来喽！")