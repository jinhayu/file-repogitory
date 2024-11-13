def log_decorator(original_func): # 외부함수
    def wrapper(*args,**kwargs): # 내부함수
        result=original_func(*args,**kwargs) # 인자 받기
        print("Calling"+" "+original_func.__name__+" "+"with arguments",args) # 결과 값 출력
        return result #
    return wrapper

@log_decorator # 데코레이터 
def add(x, y):
   return x + y



print(add(2,3))
print(add(5, 6))

