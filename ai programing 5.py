
def main():
    class comparison:
        def __init__(self,number1,number2):
            self.x=number1
            self.y=number2
        def __lt__(self,anoter):
            return self.x<anoter.x and self.y < anoter.y
        def __le__(self,anoter):
            return self.x<=anoter.x and self.y <=anoter.y
        def __eq__(self,anoter):
            return self.x==anoter.x and self.y ==anoter.y
        def __ne__(self,anoter):
            return self.x!=anoter.x and self.y !=anoter.y
        def __gt__(self,anoter):
            return self.x>anoter.x and self.y >anoter.y
        def __ge__(self,anoter):
            return self.x>=anoter.x and self.y >=anoter.y
    c1=comparison(4,2)
    c2=comparison(5,8)
    c3=c1 < c2
    c4=c1<=c2
    c5=c1==c2
    c6=c1!=c2
    c7=c1>c2
    c8=c1>=c2
    print(c3)
    print(c4)
    print(c5)
    print(c6)
    print(c7)
    print(c8)
main()
 
            

