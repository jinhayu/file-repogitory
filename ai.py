# 두근 두근 파이썬 원클래스
def main():
   # cicle의 클래스는 a객체의 설계도
   class Cicle:
    # 생성자
    def __init__(self):
        self.radius=100
    # 원 의 둘레
    def calcPermiter(self):
        return self.radius*self.radius*3.14
    # 원의 면적
    def calcAtrea(self):
     return self.radius*2*3.14
    # a의 객체는 cicle()의 인스턴스
   a=Cicle()
   # a가 radius를 가르킴
   print(f"반지름:{a.radius}")
   print(f"원의 면적:{a.calcAtrea()}")
   print(f"원의 둘레:{a.calcPermiter()}")
main()