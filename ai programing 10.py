def main():
    class Shape:
     def __init__(self, color = "green", filled = True):
      self.color = color
      self.filled = filled
     def getclor(self):
       return self.color
     def getfilled(self):
       return self.filled
    class Cicle(Shape):
      def __init__(self, color="green", filled=True,radius=1):
        super().__init__(color, filled)
        self.radius=radius
      def GetArea(self):
          return 3.14 * self.radius * self.radius
      def GetPerimeter(self):
        return 2 * 3.14 * self.radius
      def print(self):
        print("[원객체]")
        print("색상:",self.getclor())
        print("면적 :", self.GetArea())
        print("원주 :", self.GetPerimeter())
    cir1 = Cicle("red", True, 5)
    cir1.print()
main()



