from tkinter import *
from PIL import  ImageTk, Image

root = Tk()
root.geometry("")
root.title("Calculator")
root.config(bg="#7DE5ED")
root.wm_iconbitmap("images\icon.ico")

# #Defining image
# bg = PhotoImage(file = "images/wooden.png")

# #Create a Label
# my_label = Label(root, image = bg)
# my_label.place(x=0, y=0, relwidth = 1, relheight = 1)

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

f = Frame(root, bg = "#81C6E8")
b = Button(f, text = "9",padx = 28, pady = 16, font = "lucida 30 bold")
b.pack(side = RIGHT, padx = 18, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "8",padx = 28, pady = 16, font = "lucida 30 bold")
b.pack(side = RIGHT, padx = 18, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "7",padx = 28, pady = 16, font = "lucida 30 bold")
b.pack(side = RIGHT, padx = 18, pady = 5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg = "#81C6E8")
b = Button(f, text = "6",padx = 28, pady = 16, font = "lucida 30 bold")
b.pack(side = RIGHT, padx = 18, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "5",padx = 28, pady = 16, font = "lucida 30 bold")
b.pack(side = RIGHT, padx = 18, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "4",padx = 28, pady = 16, font = "lucida 30 bold")
b.pack(side = RIGHT, padx = 18, pady = 5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg = "#81C6E8")
b = Button(f, text = "3",padx = 28, pady = 16, font = "lucida 30 bold")
b.pack(side = RIGHT, padx = 18, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "2",padx = 28, pady = 16, font = "lucida 30 bold")
b.pack(side = RIGHT, padx = 18, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "1",padx = 28, pady = 16, font = "lucida 30 bold")
b.pack(side = RIGHT, padx = 18, pady = 5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg = "#81C6E8")
b = Button(f, text = "-",padx = 32, pady = 16, font = "lucida 30 bold")
b.pack(side = RIGHT, padx = 18, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "+",padx = 28, pady = 16, font = "lucida 30 bold")
b.pack(side = RIGHT, padx = 18, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "0",padx = 28, pady = 16, font = "lucida 30 bold")
b.pack(side = RIGHT, padx = 18, pady =5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg = "#81C6E8")
b = Button(f, text = "*",padx = 29, pady = 16, font = "lucida 30 bold")
b.pack(side = RIGHT, padx = 18, pady =5)
b.bind("<Button-1>", click)

b = Button(f, text = "/",padx = 34, pady = 16, font = "lucida 30 bold")
b.pack(side = RIGHT, padx = 18, pady =5)
b.bind("<Button-1>", click)

b = Button(f, text = "%",padx = 23, pady = 16, font = "lucida 30 bold")
b.pack(side = RIGHT, padx = 19, pady =5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg = "#81C6E8")
b = Button(f, text = "C",padx = 23, pady = 18, font = "lucida 30 bold")
b.pack(side = RIGHT, padx = 18, pady =5)
b.bind("<Button-1>", click)

b = Button(f, text = ".",padx = 35, pady = 22, font = "lucida 30 bold")
b.pack(side = RIGHT, padx = 18, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "=",padx = 28, pady = 22, font = "lucida 30 bold")
b.pack(side = RIGHT, padx = 18, pady = 5)
b.bind("<Button-1>", click)

f.pack()

root.mainloop()