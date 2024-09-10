def main():
    class FourCal:
        def __init__(self,number1,number2):
            self.number1=number1
            self.number2=number2
        def add(self):
            return self.number1+self.number2
        def sub(self):
             return self.number1-self.number2
        def mul(self):
            return self.number1*self.number2
        def div(self):
            return self.number1/self.number2
    a=FourCal(4,2)
    b=FourCal(3,8)
    print(a.add())
    print(a.mul())
    print(a.sub())
    print(a.div())
    print(b.add())
    print(b.mul())
    print(b.sub())
    print(b.div())
main()



