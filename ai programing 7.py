#참고문헌:https://devsalix.tistory.com/m/52
import tkinter as tk
count=0

def Plus():
    
    global count
    count+=1
    label.config(text=str(count))

def Minus():
   
    global count
    count-=1
    if count<0:
        count=0
    label.config(text=str(count))

def Clear():
    
    global count
    count=0
    label.config(text=str(count))


def main():
    global label
    window = tk.Tk()
    label = tk.Label(window, text = "0")
    label.pack()
    button1 = tk.Button(window, text = "+", command = Plus)
    button1.pack()
    button2 = tk.Button(window, text = "-", command = Minus)
    button2.pack()
    button3 = tk.Button(window, text = "clear", command = Clear)
    button3.pack()
    window.mainloop()
main()
