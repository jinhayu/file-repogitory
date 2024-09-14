def main():
    class inpormation:
        def __init__(self,name,age):
            self.name=name
            self.age=age
        def getdata(self):
            return f"당신의 이름은 {self.name} 이고 나이는 {self.age} 이군요"
    a=input("당신의 이름은 무엇입니까?")
    b=int(input("당신의 나이는 몇 살입니까?"))
    i=inpormation(a,b)
    print(i.getdata())
main()