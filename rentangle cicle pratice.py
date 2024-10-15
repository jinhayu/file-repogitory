import tkinter as tk
window = tk.Tk()
def DrawCircle(event):
    canvas.create_oval(event.x - 10, event.y - 10, event.x + 10, event.y + 10)
def DrawRect(event):
    canvas.create_rectangle(event.x - 10, event.y - 10, event.x + 10, event.y + 10)
canvas = tk.Canvas(window, width = 600, height = 400, bg = "white")
canvas.pack()
canvas.bind("<Button-3>", DrawCircle)
canvas.bind("<Button-1>",DrawRect)
window.mainloop()