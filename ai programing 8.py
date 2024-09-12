#참고문헌:유대희(https://076923.github.io/posts/Python-tkinter-1/#google_vignette)
import tkinter as tk
import tkinter.font
def chagelbel(event):
    if entry.get()=="":
        label.config(text="아무것도입력되지않았습니다.")
    elif entry.get().isalpha():
         label.config(text="숫자만입력하세요.")
    else:
        sum=0
        for i in range(1, int(entry.get()) + 1):
            sum += i
        label.config(text=f"1부터 {entry.get()} 까지의 합 = {sum}")
        entry.delete(0, len(entry.get())) 





def main():
    global label
    global entry
    window=tk.Tk()
    window.title("누적합 프로그램")
    window.geometry("1200x720")
    font=tkinter.font.Font(family="맑은 고딕", size=20, slant="italic")
    label=tk.Label(window,text="몇 까지 합을 출력할까요?",font=font)
    label.pack()
    entry=tk.Entry(window,bg="blue",font=(100))
    entry.bind("<Return>",chagelbel)
    entry.pack(padx=5,pady=10)
    window.mainloop()
main()
    