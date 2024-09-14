def main():
    class constructor:
        def printm(self):
            return 123
    class constroter(constructor):
        def __init__(self):
            super().__init__()
        def print(self):
            print(self.printm())
    a=constroter()
    a.print()
main()