def trace(func):
    def wrapper():
        print(func.__name__,'함수 시작')
    func() # 매개변수로 받은 함수를 호출
    print(func.__name__, '함수 끝')
    return wrapper 
@trace
def hello():
    print('hello')
@trace
def world():
    print('world')
hello()
world()