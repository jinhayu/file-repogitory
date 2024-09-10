def main():
    class user:
        def __init__(self):
            self.name=[]
        def append(self,string):
            self.name.append(string)
        def __getitem__(self,item):
            return self.name[item]
    person=user()
    for i in range(10):
        a=input()
        person.append(a)
    print(person.name)
    print(person[0])
main()
            