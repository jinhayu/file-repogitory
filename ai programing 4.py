
def main():
    class user:
        def __init__(self):
            self.name=[]
        def push(self,string):
            self.name.append(string)
        def __getitem__(self,item):
            return self.name[item]
        def __len__(self):
            return len(self.name)
    person=user()
    for i in range(1000000):
        a=input()
        if a.isalpha():
            person.push(a)
        else:
            break
    print(person.name)
    print(person[0])
    print(len(person))
main()
   