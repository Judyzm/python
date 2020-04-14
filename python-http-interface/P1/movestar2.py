import random
dot=['.']*24
n=random.randint(1,24)
for i in range(0,23):
    if i==n:
        dot[i]='*'
        break
s1=''
print(s1.join(dot))
while 1>=0:
    if i==0:
        print("右侧到底了")
        break
    if i==23:
        print("左侧到底了")
        break
    move=input("请输入移动星号的指令(L/l or R/r)：")
    if move in ('L','l'):
        dot[i],dot[i-1]=dot[i-1],dot[i]
        print((s1.join(dot)))
        i=i-1
    if move in ('R','r'):
        dot[i],dot[i+1]=dot[i+1],dot[i]
        print(s1.join(dot))
        i=i+1
    if move in ('exit','EXIT','Exit'):
        print("已成功退出")
        break

