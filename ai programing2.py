def main():
    class Rectangle:
        def __init__(self,width=1,height=1):
            self.x=width
            self.y=height
        def GetArea(self):
            return self.x*self.y
        def GetPerimeter(self):
            return 2*(self.x+self.y)
        def _sub_(self,newvalue):
            return self.x*self.y - newvalue.x*newvalue.y
        def  DiffArea(self,newvalue):
            return abs(self._sub_(newvalue))
    rect1=Rectangle(4,10)
    rect2=Rectangle(3.5,35.7)
    outcome=rect1.DiffArea(rect2)
    print(rect1.GetArea())
    print(rect1.GetPerimeter())
    print(outcome)
main()



            