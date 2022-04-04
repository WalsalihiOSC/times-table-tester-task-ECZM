"""The program is about Times Table Tester"""

import random
from tkinter import * 

class TimesTableTester:
    
    def __init__(self, parent):
        self.f1 = Frame(parent, height = 200, width = 350, border = 2, borderwidth = 3, relief = RIDGE)
        self.f1.grid(column = 0, row = 0)

        self.f1.grid_propagate(0)
        
        self.label1 = Label(self.f1, text = "Click Next to Start")
        self.label1.grid(column = 0, row = 0)

        button1 = Button(self.f1, text = "Check Answer", command = self.check_answer)
        button1.grid(column = 0, row = 2)

        self.entry1 = Entry(self.f1, width = 10)
        self.entry1.grid(column = 1, row = 0, sticky = E)

        button2 = Button(self.f1, text = "Next", command = self.next_question)
        button2.grid(column = 1, row = 2, sticky = E)

        self.label2 = Label(self.f1, text = "")
        self.label2.grid(column = 2, row = 0, ipadx = 10)

        self.label3 = Label(self.f1, text = "")
        self.label3.grid(column = 0, row = 1)

        self.label4 = Label(self.f1, text = "")
        self.label4.grid(column = 1, row = 1)

    def next_question(self):
        self.entry1.delete(0, 'end')
        self.label2.configure(text = "")

        self.a = random.randint(1, 12)
        self.b = random.randint(1, 12)

        self.label1.configure(text = "{} * {}".format(self.a, self.b))

    def check_answer(self):
        answer = int(self.a * self.b)
        if int(self.entry1.get()) != answer:
            self.label2.configure(text = "*Incorrect")
        else:
            int(self.entry1.get()) == answer
            self.label2.configure(text = "Correct!")
               
                
        

#Main Routine
if __name__ == "__main__":
    root = Tk()
    ttt = TimesTableTester(root)
    root.title("Times Table Tester")
    root.mainloop()
