
def main():
    class comparison:
        def __init__(self,number1,number2):
            self.x=number1
            self.y=number2
        def __lt__(self,anoter):
            return self.x<anoter.x and self.y < anoter.y
    c1=comparison(4,2)
    c2=comparison(5,8)
    c3=c1 < c2
    print(c3)
main()
 
            
            

