class Time:
    def getValue(self):
        self.h = int(input("Enter hour:"))
        self.m = int(input("Enter minute:"))
        self.s = int(input("Enter seconds:"))

    def addValue(self,t1,t2):
        self.s = t1.s + t2.s
        self.m = t1.m + t2.m + self.s//60
        self.h = t1.h + t2.h + self.m//60
        self.m = self.m%60
        self.s = self.s%60

    def putValue(self):
        print("h="+self.h)
        print("m="+self.m)
        print("s="+self.s)

t1 = Time()
t2 = Time()
t3 = Time()

t1.getValue()
t2.getValue()

t3.addValue(t1,t2)
t3.putValue()