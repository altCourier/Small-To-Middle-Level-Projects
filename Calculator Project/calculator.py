from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master): # master is the main Tkinter window
        master.title("Calculator")
        master.geometry("357x420+0+0") # W: 357 px, H:420 px, +0+0: The pos starting at the top-left corner (0,0)
        master.config(bg="#FFDAB9") # bg colour will be gray
        master.resizable(False, False) # Window is non-resizable W: False, H: False

        self.equation = StringVar()
        # StringVar() is a tkinter variable class that holds a str value.
        # Can be linked to widgets
        # self.equation will hold whatever value is typed.
        self.entry_value = ''
        Entry(width= 30, bg ='#FFD1DC', font=('#333333', 18), textvariable=self.equation).place(x=0,y=0)
        # Entry widget
        # width = 17: number of character that can fit inside the entry widget.
        # bg = '#fff' background colour set to white
        # font: setting the font
        # textvariable = self.equation: links self.equation to entry widget.
        # .place(x=0, y=0) position at (0,0)

        Button(width=11,height=4,text='=', relief='sunken',bg="#fff0f5",command = self.solve).place(x=270 ,y=350 )
        Button(width=11,height=4,text='C', relief='sunken',bg="#fff0f5",command = self.clear).place(x=0 ,y=350 )
        
        # Button() widget creates a clickable button.
        # text = '' for any text placed on top
        # relief: controls border style of button how EDGES will look like.
        # flat (No 3D effect), raised,sunken,groove,ridge
        # bg: for background
        # command = ... to specify a function that should be called.
        # lambda: self.show().place(x= , y= ) => A anon func
        # .place(x=, y=) place it specific coordinates.


        # Automated the button process instead of ctrl C+V every single time:
        buttons = [
            ('(',0,50), (')',90,50),('%',180,50),('1',0,125),
            ('2',90,125), ('3',180,125),('4',0,200),('5',90,200),
            ('6',180,200), ('7',0,275),('9',180,275),('8',90,275),
            ('0',90,350), ('.',180,350),('+',270,275),('-',270,200),
            ('/',270,50), ('*',270,125)
        ]
        for (text, x, y) in buttons:
            self.create_button(text, x, y)

    # Create button
    def create_button(self, text, x, y):
        button =  Button(text=text, width=11, height=4, relief='sunken', bg='#fff0f5',command=lambda: self.show(text))
        button.place(x=x, y=y)
    
    # Show the values given by user
    def show(self,value):
        self.entry_value += str(value) # From 5 to +3 = 53 just as calculators
        self.equation.set(self.entry_value) # Update the self.entry_value

    # Clear the equations
    def clear(self):
        self.entry_value = '' # Reset entry value
        self.equation.set(self.entry_value) # Update

    # Solve for show
    def solve(self):
        try:
            result = eval(self.entry_value, {"__builtins__": None}, {})
            # {"__builtins__": None}
            # CON: Cannot use print() or os.system()
            # {} is the global namespace for eval() ---> cannot access any other variables
            # dependent outside of the expression.
            self.equation.set(result)

            """ EASTER EGG """
            if "29/10/1923" == self.entry_value:
                self.equation.set("Ne mutlu Türküm diyene!")

        except Exception as e:
            self.equation.set("Error")

root = Tk() # Main window is created: Tk() is a class
calculator = Calculator(root) # calculator object created
root.mainloop() # Keep the window open