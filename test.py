from tkinter import *
from PIL import  ImageTk, Image

root = Tk()
root.geometry("1920x1080")
root.title("Calculator")
root.config(bg="black")
root.wm_iconbitmap("images\icon.ico")
p = 300

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else :
            value = eval(screen.get())
            
        scvalue.set(value)
        screen.update()
            
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
    
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font = "lucida 35 bold")
screen.pack(fill = X, ipadx = 8, pady = 10, padx = 10)

n=0
for i in range(9, 6, -1):
    while(n<406):
        f = Frame(root, bg = "black")
        b = Button(f, text = f"{i}",padx = 28, pady = 16, font = "lucida 30 bold", bg = "#0fbf02", fg = "black")
        b.pack(side = LEFT, padx = 18, pady = 5, anchor = "w")
        b.bind("<Button-1>", click)
        f.place(x=p + n, y = 85)
        break 
    n = n+135
n=0 
for i in range(6, 3, -1):
    while(n<406):
        f = Frame(root, bg = "black")
        b = Button(f, text = f"{i}",padx = 28, pady = 16, font = "lucida 30 bold", bg = "#0fbf02", fg = "black")
        b.pack(side = LEFT, padx = 18, pady = 5, anchor = "w")
        b.bind("<Button-1>", click)
        f.place(x=p + n, y = 205)
        break 
    n = n+135
n=0 
for i in range(3, 0, -1):
    while(n<406):
        f = Frame(root, bg = "black")
        b = Button(f, text = f"{i}",padx = 28, pady = 16, font = "lucida 30 bold", bg = "#0fbf02", fg = "black")
        b.pack(side = LEFT, padx = 18, pady = 5, anchor = "w")
        b.bind("<Button-1>", click)
        f.place(x=p + n, y = 325)
        break 
    n = n+135
# n=0 
# for i in range(3):
#     l = ["-", "+", 0]
#     while(n<406):
#         f = Frame(root, bg = "black")
#         b = Button(f, text = f"{l[i]}",padx = 28, pady = 16, font = "lucida 30 bold", bg = "#0fbf02", fg = "black")
#         b.pack(side = LEFT, padx = 18, pady = 5, anchor = "w")
#         b.bind("<Button-1>", click)
#         f.place(x=p + n, y = 445)
#         break 
#     n = n+135
# n=0 
# for i in range(2):
#     l = ["*", "/", "%"]
#     while(n<406):
#         f = Frame(root, bg = "black")
#         b = Button(f, text = f"{l[i]}",padx = 28, pady = 16, font = "lucida 30 bold", bg = "#0fbf02", fg = "black")
#         b.pack(side = LEFT, padx = 18, pady = 5, anchor = "w")
#         b.bind("<Button-1>", click)
#         f.place(x=p + n, y = 565)
#         break 
#     n = n+135
# n=0 
# for i in range(1):
#     l = ["%"]
#     while(n<406):
#         f = Frame(root, bg = "black")
#         b = Button(f, text = f"{l[i]}",padx = 24, pady = 16, font = "lucida 30 bold", bg = "#0fbf02", fg = "black")
#         b.pack(side = LEFT, padx = 18, pady = 5, anchor = "w")
#         b.bind("<Button-1>", click)
#         f.place(x= 560 + n, y = 565)
#         break 
#     n = n+135
# n=0 
# for i in range(3):
#     l = ["C", ".", "="]
#     while(n<406):
#         f = Frame(root, bg = "black")
#         b = Button(f, text = f"{l[i]}",padx = 28, pady = 16, font = "lucida 30 bold", bg = "#0fbf02", fg = "black")
#         b.pack(side = LEFT, padx = 18, pady = 5, anchor = "w")
#         b.bind("<Button-1>", click)
#         f.place(x=p + n, y = 685)
#         break 
#     n = n+135
f = Frame(root, bg = "black")
b = Button(f, text = "-",padx = 32, pady = 16, font = "lucida 30 bold", fg = "black", bg = "#0fbf02")
b.pack(side = LEFT, padx = 18, pady = 5, anchor = "w")
b.bind("<Button-1>", click)

b = Button(f, text = "+",padx = 28, pady = 16, font = "lucida 30 bold", fg = "black", bg = "#0fbf02")
b.pack(side = LEFT, padx = 18, pady = 5, anchor = "w")
b.bind("<Button-1>", click)

b = Button(f, text = "0",padx = 28, pady = 16, font = "lucida 30 bold", fg = "black", bg = "#0fbf02")
b.pack(side = LEFT, padx = 18, pady =5, anchor = "w")
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg = "black")
b = Button(f, text = "*",padx = 29, pady = 16, font = "lucida 30 bold", fg = "black", bg = "#0fbf02")
b.pack(side = LEFT, padx = 18, pady =5, anchor = "w")
b.bind("<Button-1>", click)

b = Button(f, text = "/",padx = 34, pady = 16, font = "lucida 30 bold", fg = "black", bg = "#0fbf02")
b.pack(side = LEFT, padx = 18, pady =5, anchor = "w")
b.bind("<Button-1>", click)

b = Button(f, text = "%",padx = 23, pady = 16, font = "lucida 30 bold", fg = "black", bg = "#0fbf02")
b.pack(side = LEFT, padx = 19, pady =5, anchor = "w")
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg = "black")
b = Button(f, text = "C",padx = 23, pady = 18, font = "lucida 30 bold", fg = "black", bg = "#0fbf02")
b.pack(side = LEFT, padx = 18, pady =5)
b.bind("<Button-1>", click)

b = Button(f, text = ".",padx = 35, pady = 22, font = "lucida 30 bold", fg = "black", bg = "#0fbf02")
b.pack(side = LEFT, padx = 18, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "=",padx = 28, pady = 22, font = "lucida 30 bold", fg = "black", bg = "#0fbf02")
b.pack(side = LEFT, padx = 18, pady = 5, anchor = "w")
b.bind("<Button-1>", click)

f.pack()

root.mainloop()

