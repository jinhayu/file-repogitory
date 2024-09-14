def main():
    class int_print:
        def __init__(self,number):
            self.number=number
        def getintdate(self):
            return self.number
    a=int(input())
    b=int_print(a)
    print(b.getintdate())
main()            