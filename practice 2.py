# 상속문제
def main():
    class Circle:
        def __init__(self,radius):
            self.radius=radius
    class namecicle(Circle):
        def __init__(self, name,radius):
            super().__init__(radius)
            self.name=name
        def getdata(self):
            return f"{self.name},반지름={self.radius}"
    a=namecicle("waffle",5)
    print(a.getdata())
main()