# 점프투 파이썬 262p 상속문제 
def main():
    class Calculator:
        def __init__(self,val1):
            self.val1=val1
            self.value=0
        def val(self):
            self.value+=self.val1
            return self.value
    class upgradeCalculator(Calculator):
        def __init__(self, val1,val2):
            super().__init__(val1)
            self.val2=val2
        def add(self):
            result=self.val()+self.val2
            return result
        def sub(self):
            result=self.val()-self.val2
            return result
        def mul(self):
            result=self.val()*self.val2
            return result
        def div(self):
            result=self.val()/self.val2
            return result
    a=upgradeCalculator(3,2)
    print(a.add())
    print(a.sub())
    print(a.mul())
    print(a.div())
main()