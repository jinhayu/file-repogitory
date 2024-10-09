# 비트코딩 396
def main():
   class person:
    def __init__(self,name,workingfor,ATtime,workhour):
        self.name=name
        self.workingfor=workingfor
        self.ATtime=int(ATtime)
        self.workhour=workhour
        self.result=self.ATtime//100
        self.result1=self.ATtime%100
    def getAttime(self):
       return f"{self.result} 시 {self.result1} 분"

   p=person("yu jin ha","kumoh","0900",8)
   print(p.name)
   print(p.workhour)
   print(p.workingfor)
   print(p.getAttime())

main()