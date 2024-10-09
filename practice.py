def main():
    class song:
        def __init__(self,name):
            self.name=name
        def result(self):
            return f"내노래는 {self.name}"
    a=song("nessun dorema")
    b=song("공주는 잠 못이루고")
    print(a.result())
    print(b.result())
main()