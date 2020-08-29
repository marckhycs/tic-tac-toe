from tkinter import Tk
from tkinter import Button
from tkinter import Label
from tkinter import messagebox

def button_disable():
    b1.config(state = "disabled")
    b2.config(state = "disabled")
    b3.config(state = "disabled")
    b4.config(state = "disabled")
    b5.config(state = "disabled")
    b6.config(state = "disabled")
    b7.config(state = "disabled")
    b8.config(state = "disabled")
    b9.config(state = "disabled")

def winner():
    global win
    win = False
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg = "blue")
        b2.config(bg = "blue")
        b3.config(bg = "blue")
        win = True
        messagebox.showinfo("Tac Tac Toe", "X player wins!")
        button_disable()
    
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg = "blue")
        b5.config(bg = "blue")
        b6.config(bg = "blue")
        win = True
        messagebox.showinfo("Tac Tac Toe", "X player wins!")
        button_disable()
    
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg = "blue")
        b8.config(bg = "blue")
        b9.config(bg = "blue")
        win = True
        messagebox.showinfo("Tac Tac Toe", "X player wins!")
        button_disable()
    
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg = "blue")
        b4.config(bg = "blue")
        b7.config(bg = "blue")
        win = True
        messagebox.showinfo("Tac Tac Toe", "X player wins!")
        button_disable()
    
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg = "blue")
        b5.config(bg = "blue")
        b8.config(bg = "blue")
        win = True
        messagebox.showinfo("Tac Tac Toe", "X player wins!")
        button_disable()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg = "blue")
        b6.config(bg = "blue")
        b9.config(bg = "blue")
        win = True
        messagebox.showinfo("Tac Tac Toe", "X player wins!")
        button_disable()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg = "blue")
        b5.config(bg = "blue")
        b9.config(bg = "blue")
        win = True
        messagebox.showinfo("Tac Tac Toe", "X player wins!")
        button_disable()
    
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg = "blue")
        b5.config(bg = "blue")
        b7.config(bg = "blue")
        win = True
        messagebox.showinfo("Tac Tac Toe", "X player wins!")
        button_disable()

    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg = "blue")
        b2.config(bg = "blue")
        b3.config(bg = "blue")
        win = True
        messagebox.showinfo("Tac Tac Toe", "O player wins!")
        button_disable()
    
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg = "blue")
        b5.config(bg = "blue")
        b6.config(bg = "blue")
        win = True
        messagebox.showinfo("Tac Tac Toe", "O player wins!")
        button_disable()
    
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg = "blue")
        b8.config(bg = "blue")
        b9.config(bg = "blue")
        win = True
        messagebox.showinfo("Tac Tac Toe", "O player wins!")
        button_disable()
    
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg = "blue")
        b4.config(bg = "blue")
        b7.config(bg = "blue")
        win = True
        messagebox.showinfo("Tac Tac Toe", "O player wins!")
        button_disable()
    
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg = "blue")
        b5.config(bg = "blue")
        b8.config(bg = "blue")
        win = True
        messagebox.showinfo("Tac Tac Toe", "O player wins!")
        button_disable()

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg = "blue")
        b6.config(bg = "blue")
        b9.config(bg = "blue")
        win = True
        messagebox.showinfo("Tac Tac Toe", "O player wins!")
        button_disable()

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg = "blue")
        b5.config(bg = "blue")
        b9.config(bg = "blue")
        win = True
        messagebox.showinfo("Tac Tac Toe", "O player wins!")
        button_disable()
    
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg = "blue")
        b5.config(bg = "blue")
        b7.config(bg = "blue")
        win = True
        messagebox.showinfo("Tac Tac Toe", "O player wins!")
        button_disable()
    

click = True
c_click = 0

def clicked(b):
    global click
    global c_click
    if b["text"] == " " and click == True:
        b["text"] = "X"
        click = False
        c_click +=1
        winner()
    elif b["text"] == " " and click == False:
        b["text"] = "O"
        click = True
        c_click +=1
        winner()
    else:
        messagebox.showerror("Tic Tac Toe", "Box is already taken!" )

    

    


screen = Tk()
screen.title("Tic Tac Toe")

b1 = Button(screen, height = 4, width = 10,text = " ", font = ("Helvetica", 15),command = lambda: clicked(b1))
b2 = Button(screen, height = 4, width = 10,text = " ", font = ("Helvetica", 15),command = lambda: clicked(b2))
b3 = Button(screen, height = 4, width = 10,text = " ", font = ("Helvetica", 15),command = lambda: clicked(b3))

b4 = Button(screen, height = 4, width = 10,text = " ", font = ("Helvetica", 15),command = lambda: clicked(b4))
b5 = Button(screen, height = 4, width = 10,text = " ", font = ("Helvetica", 15),command = lambda: clicked(b5))
b6 = Button(screen, height = 4, width = 10,text = " ", font = ("Helvetica", 15),command = lambda: clicked(b6))

b7 = Button(screen, height = 4, width = 10,text = " ", font = ("Helvetica", 15),command = lambda: clicked(b7))
b8 = Button(screen, height = 4, width = 10,text = " ", font = ("Helvetica", 15),command = lambda: clicked(b8))
b9 = Button(screen, height = 4, width = 10,text = " ", font = ("Helvetica", 15),command = lambda: clicked(b9))

b1.grid(row = 0, column =0, pady = 2, padx = 2)
b2.grid(row = 0, column =1, pady = 2, padx = 2)
b3.grid(row = 0, column =2, pady = 2, padx = 2)

b4.grid(row = 1, column =0, pady = 2, padx = 2)
b5.grid(row = 1, column =1, pady = 2, padx = 2)
b6.grid(row = 1, column =2, pady = 2, padx = 2)

b7.grid(row = 2, column =0, pady = 2, padx = 2)
b8.grid(row = 2, column =1, pady = 2, padx = 2)
b9.grid(row = 2, column =2, pady = 2, padx = 2)

screen.mainloop()
