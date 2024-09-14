def main():
    class printm:
        def __init__(self,number1,number2):
            self.number1=number1
            self.number2=number2
        def new_line(self):
            print(self.number1)
            print(self.number2)
    a=int(input())
    b=int(input())
    p1=printm(a,b)
    p1.new_line()
main()