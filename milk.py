import tkinter as tk
from tkinter import messagebox
global milk_var
global persent 
def show_selection():
       selected_milkvar = milk_var.get()
       selected_persent = persent.get()
       messagebox.showinfo("선택 결과",f"선택한 메뉴: {selected_milkvar}\n선택한당도:{selected_persent}")
def main():
       global milk_var
       global persent
       window=tk.Tk()
       label = tk.Label(window, text = "공차 메뉴를 선택하세요:")
       label.pack()
       milk_var = tk.StringVar(value="타로 밀크티")
       milk_var1= tk.Radiobutton(window, text="타로 밀크티", 
       variable=milk_var, value="타로밀크티")
       milk_var1.pack()
       milk_var2 = tk.Radiobutton(window, text="브라운 슈가 쥬얼리 밀크티", 
       variable= milk_var, value="브라운 슈가 쥬얼리 밀크티")
       milk_var2.pack()
       milk_var3= tk.Radiobutton(window, text="초쿄 버블티", 
       variable= milk_var, value="초쿄 버블티")
       milk_var3.pack()
       label1 = tk.Label(window, text = "당도를 선택하세요:")
       label1.pack()
       persent=tk.StringVar(value="50%")
       persent1= tk.Radiobutton(window, text="50%", 
       variable=persent, value="50%")
       persent1.pack()
       persent2 = tk.Radiobutton(window, text="70%", 
       variable= persent, value="70%")
       persent2.pack()
       persent3= tk.Radiobutton(window, text="100%", 
       variable= persent, value="100%")
       persent3.pack()
       button = tk.Button(window, text="선택 확인", 
       command=show_selection)
       button.pack()
       window.mainloop()
main()