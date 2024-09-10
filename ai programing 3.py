def main():
    class point:
        def __init__(self,number1,number2):
            self.x=number1
            self.y=number2
        def Print(self):
         print("(", self.x, ", ", self.y, ")")
        def __add__(self, pt):
         new_pt = point(self.x + pt.x, self.y + pt.y)
         return new_pt
        def __sub__(self, pt):
            new_pt = point(self.x - pt.x, self.y - pt.y)
            return new_pt
        def __mul__(self, pt):
            new_pt = point(self.x * pt.x, self.y * pt.y)
            return new_pt
        def __truediv__(self, pt):
            new_pt = point(self.x / pt.x, self.y / pt.y)
            return new_pt        
           
    pt1 = point(1, 2)
    pt2 = point(3, 4)
    pt3 = pt1 + pt2
    pt4=  pt1-pt2
    pt5=pt1*pt2
    pt6=pt1/pt2
    pt1.Print()
    pt2.Print()
    pt3.Print()
    pt4.Print()
    pt5.Print()
    pt6.Print()
main()       
