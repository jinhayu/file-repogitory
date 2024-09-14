def main():
    class nonli:
        def __init__(self,number):
            self.number=number
        def printm(self):
            if self.number<10:
                return "small"
            return ""
    a=int(input())
    b=nonli(a)
    print(b.printm())
main()
