class people:
    name=''
    age=0
    __weight=0
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.__weight=w
    def speak(self):
        print("%s说：我%d岁了"%(self.name,self.age))

class student(people):
    grade=''
    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w)
        self.grade=g
    def speak(self):
        print("%s说：我%d岁了，我在读%d年级。"%(self.name,self.age,self.grade))
class speaker():
    topic=''
    name=''
    def __init__(self,n,t):
        self.name=n
        self.topic=t
    def speak(self):
        print("我叫%s,我是一个演说家，我演讲的题目是%s"%(self.name,self.topic))

class sample(speaker,student):
    a=''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)
test=sample("tom",25,80,3,"python")
test.speak() #方法相同，默认调用括号找那个前排的父类方法，即：speaker类重的speak方法。

