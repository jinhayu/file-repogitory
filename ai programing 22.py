def main():
    class constror:
        def printm(self):
            return "hello"
    class constor1(constror):
        def __init__(self):
            super().__init__()
        def print(self):
            print(self.printm())
    a=constor1()
    a.print()
main()