from random import randint

number=randint(1,100)
running=True

while running:
    guess=int(input("请输入一个整数："))

    if guess==number:
        print("你猜对了！")
        running=False
    elif guess<number:
        print("你猜的数值偏小，再试一下呢")
    elif guess>number:
        print("你猜的数值偏大，再试一下呢")
else:
    print("很厉害呢！")