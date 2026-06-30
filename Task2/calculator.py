from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Modern Calculator")
root.geometry("430x610")
root.configure(bg="#1E1E2E")
root.resizable(False, False)

expression = ""
equation = StringVar()
history = []

def press(key):
    global expression
    expression += str(key)
    equation.set(expression)

def equal():
    global expression
    try:
        exp = expression
        result = str(eval(expression))
        history.append(f"{exp} = {result}")
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def show_history():
    win = Toplevel(root)
    win.title("History")
    win.geometry("320x360")
    win.configure(bg="#1E1E2E")
    List = Listbox(win, font=("Segoe UI",11), bg="#2A2A40", fg="white",
                   selectbackground="#F39C12", bd=0)
    List.pack(fill=BOTH, expand=True, padx=10, pady=10)
    if history:
        for item in history:
            List.insert(END, item)
    else:
        List.insert(END, "No history")

def key_press(event):
    k = event.keysym
    if k in ("Return","KP_Enter"):
        equal()
    elif k=="BackSpace":
        backspace()
    elif k=="Escape":
        clear()
    elif event.char in "0123456789+-*/().":
        press(event.char)

root.bind("<Key>", key_press)

display = Entry(root,textvariable=equation,font=("Segoe UI",24,"bold"),
                bg="#2A2A40",fg="white",bd=0,justify="right",
                insertbackground="white")
display.pack(fill="x",padx=15,pady=(15,10),ipady=16)

Button(root,text="History",command=show_history,
       font=("Segoe UI",10,"bold"),
       bg="#3498DB",fg="white",bd=0).pack(pady=(0,10))

frame = Frame(root,bg="#1E1E2E")
frame.pack(padx=8,pady=5)

buttons = [
    ["C","⌫","/","*"],
    ["7","8","9","-"],
    ["4","5","6","+"],
    ["1","2","3","="],
    ["0",".","(",")"]
]

colors = {
    "num":"#3E3A63",
    "op":"#F39C12",
    "eq":"#2ECC71",
    "clr":"#FF4D4D"
}

for i in range(4):
    frame.grid_columnconfigure(i,weight=1)

for r,row in enumerate(buttons):
    for c,txt in enumerate(row):
        if txt=="C":
            cmd=clear;color=colors["clr"]
        elif txt=="⌫":
            cmd=backspace;color=colors["clr"]
        elif txt=="=":
            cmd=equal;color=colors["eq"]
        elif txt in "+-*/":
            cmd=lambda t=txt: press(t); color=colors["op"]
        else:
            cmd=lambda t=txt: press(t); color=colors["num"]

        Button(frame,
               text=txt,
               command=cmd,
               font=("Segoe UI",16,"bold"),
               width=4,
               height=1,
               bg=color,
               fg="white",
               bd=0,
               relief="flat",
               cursor="hand2",
               activebackground=color,
               activeforeground="white").grid(
                    row=r,column=c,
                    padx=5,pady=5,
                    ipadx=5,ipady=6,
                    sticky="nsew"
               )


root.mainloop()
