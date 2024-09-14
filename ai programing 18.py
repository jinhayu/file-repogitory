def main():
    class printmodule:
        def __init__(self,flo):
            self.flo=flo
        def getfloatdata(self):
            return self.flo
    a=float(input())
    b=printmodule(a)
    print(b.getfloatdata())
main()

            