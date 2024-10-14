import tkinter as tk
def ChangeLabel():
    labeltext = label.cget("text")
    changeText = str(int(labeltext)+1)
    label.config(text = changeText)
def ChangeLabe2():
    labeltext = label.cget("text")
    changeText = str(int(labeltext)-1)
    label.config(text = changeText)   
def ChangeLabe3():
    label.config(text = "0")    

window = tk.Tk()
label = tk.Label(window, text = "0")
label.pack()
button = tk.Button(window, text = "+", command = ChangeLabel)
button1 = tk.Button(window, text = "-", command = ChangeLabe2)
button2 = tk.Button(window, text = "clear", command = ChangeLabe3)
button.pack()
button1.pack()
button2.pack()
window.mainloop()
