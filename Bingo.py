import tkinter as tk
import random

class Bingo:
    def __init__(self):
        f = open('goals.txt', 'r')
        content = f.read()
        li = list(content.split("\n"))
        f.close()
        
        self.root = tk.Tk()

        self.root.geometry("600x600")
        self.root.title("BINGO")

        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0,weight=1,uniform="1")
        self.buttonframe.columnconfigure(1,weight=1,uniform="1")
        self.buttonframe.columnconfigure(2,weight=1,uniform="1")
        self.buttonframe.columnconfigure(3,weight=1,uniform="1")
        self.buttonframe.columnconfigure(4,weight=1,uniform="1")
        self.buttonframe.rowconfigure(0,weight=1,uniform="1")
        self.buttonframe.rowconfigure(1,weight=1,uniform="1")
        self.buttonframe.rowconfigure(2,weight=1,uniform="1")
        self.buttonframe.rowconfigure(3,weight=1,uniform="1")
        self.buttonframe.rowconfigure(4,weight=1,uniform="1")

        self.buttons=[None] * 25
        self.active=[False] * 25

        for i in range(0,25):
            r = random.randint(0, len(li)-1)
            self.buttons[i] = tk.Button(self.buttonframe, text=li[r], font=('Arial', 10), command= lambda m=i: self.test(m), bg="#d6d6d6", activebackground="#d6d6d6", wraplength=110)
            self.buttons[i].grid(row=i % 5,column=i // 5, sticky="news")
            li.remove(li[r])

        self.buttons[12].config(text="Glitched Lobby (Free)")
        
        self.buttonframe.pack(fill="both", expand=True)

        self.root.mainloop()

    def test(self, pos):
        if not self.active[pos] :
            self.buttons[pos].config(bg="#E5FFDA")
            self.active[pos] = True
        else:
            self.buttons[pos].config(bg="#d6d6d6")
            self.active[pos] = False

bingo = Bingo()
