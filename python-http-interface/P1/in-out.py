import random
f=open("E:/2020test/input.txt",'w')
a=1
while a<=24:
    i=random.randint(3,100)
    f.write(str(i)+'\n')
    a=a+1
f.close()
f=open("E:/2020test/input.txt",'r')
f2=open("E:/2020test/output.txt",'w')
for line in f:
    a=int(line)
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
f.close()
f2.close()
