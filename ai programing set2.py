# 참고문헌: 
def main():
    text ="python is great and python is dynamic and versatile"
    test=set(text.split())
    result=" ".join(test)
    file=open('a.txt','w')
    for i in result:
        file.write(i+"\n")
    file.close()

main()