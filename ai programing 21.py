def main():
    class nonli:
        def __init__(self,number):
            self.number=number
        def printm(self):
            if self.number<10:
                return "small"
            else:
                self.number>10
                return "big"
    a=int(input())
    b=nonli(a)
    print(b.printm())
main()
    