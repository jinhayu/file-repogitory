#참고문헌:(https://gorokke.tistory.com/129#google_vignette)
def main():
    class user_stack:
        def __init__(self):
            self.name=[]
        def push(self,item):
            self.name.append(item)
        def pop(self):
            return self.name.pop()
        def peek(self):
            return self.name[-1]
        def isempy(self):
            return not self.name
    person=user_stack()
    print(person)
    print(person.isempy())
    for i in range(100000000):
        a=input()
        if a.isalpha():
            person.push(a)
        else:
            break
    print(person.pop())
    print(person.name)
    print(person.pop())
    print(person.name)
    print(person.peek())
    print(person.name)
         
main()
        
        
            