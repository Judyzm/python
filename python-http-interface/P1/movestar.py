import random

class star:
    def movestar(self):
        n = random.randint(1, 24)
        print((n - 1) * '.' + '*' + (24 - n) * '.')
        while 1 != 0:
            if n==0:
                print("左侧到底了")
                break
            if n==25:
                print('右侧到底了')
                break

            mov = input("请输入移动星号的指令(L/l or R/r)")
            if (mov in ['L', 'l']) and n >= 1:
                print((n - 1) * '.' + '*' + (24 - n) * '.')
                n = n - 1
            if (mov in ['R', 'r']) and n <= 24:
                print((n - 1) * '.' + '*' + (24 - n) * '.')
                n = n + 1
b = star()
b.movestar()


