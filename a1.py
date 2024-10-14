import tkinter as tk
class Counterapp:
    def __init__(self,window):
        self.window=window
        self.label = tk.Label(window, text="0")
        self.label.pack()
        self.button = tk.Button(window, text = "+", command = self.ChangeLabel)
        self.button1=tk.Button(window, text = "-", command = self.ChangeLabe2)
        self.button2=tk.Button(window, text = "clear", command = self.ChangeLabe3)
        self.button.pack()
        self.button1.pack()
        self.button2.pack()
    def ChangeLabel(self):
        self.labeltext = self.label.cget("text")
        self.changeText = str(int(self.labeltext)+1)
        self.label.config(text = self.changeText)
    def ChangeLabe2(self):
        self.labeltext = self.label.cget("text")
        self.changeText = str(int(self.labeltext)-1)
        self.label.config(text = self.changeText)   
    def ChangeLabe3(self):
        self.label.config(text = "0")    

window = tk.Tk() 
app = Counterapp(window) 
window.mainloop() 