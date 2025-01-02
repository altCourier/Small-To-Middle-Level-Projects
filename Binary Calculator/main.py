import tkinter as tk
from tkinter import messagebox

def main():
    calc = BinaryCalculator()
    calc.mainloop()

class BinaryCalculator(tk.Tk):
    binaryValues = ['1','0']

    def __init__(self):
        # INITIALIZE THE MAIN WINDOW
        super().__init__()
        self.title("Binary Calculator")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # LIST TO STORE BINARY VALUES
        self.binary_numbers = []

        # CURRENT TOTAL
        self.total = 0

        # ENTRY BOX
        self.entry_box = tk.Entry(self)
        self.entry_box.grid(row = 0, column = 0, sticky = "nw", pady = 2, padx = 1)
        self.entry_box.bind("<Return>", self.add_to_box)

        # BUTTON TO ENTRY
        self.entry_button = tk.Button(self, text = "ADD TO LIST")
        self.entry_button.grid(row = 0, column = 1, sticky = "nsew", padx = 2, pady = 1)
        self.entry_button.bind("<Button-1>", self.add_to_box)

        # LABEL TO SHOW TOTAL VALUE
        self.calculate = tk.Label(self, text = "CALCULATE")
        self.calculate.grid(row = 1, column = 1, sticky = "nsew", padx = 2, pady = 1)
        

        # LISTBOX AND SCROLLBAR
        self.frame = tk.Frame(self)
        self.frame.grid(row = 1, column = 0, sticky = "nsew")

        self.list_box = tk.Listbox(self.frame)
        self.list_box.grid(row = 0, column = 0)

        self.scroll_bar = tk.Scrollbar(self.frame, orient = "vertical", command = self.list_box.yview)
        self.scroll_bar.grid(row = 0, column = 1)
        self.list_box.config(yscrollcommand = self.scroll_bar.set)

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)


    # ADD TO LIST BOX
    def add_to_box(self, event = None):
        try: 
            value = self.entry_box.get()
            if value and self.is_binary(value):  
                self.list_box.insert(tk.END, value)
                self.binary_numbers.append(value)
                print(f"{value} has been added successfully.")
                self.entry_box.delete(0, tk.END)
            else:
                raise ValueError("Invalid Binary Value")
        except ValueError as e:
            tk.messagebox.showwarning(title = "WARNING!", message = "Unexpected input given, please enter a binary value.")

    # CHECK IF BINARY
    def is_binary(self, value: str) -> bool:
        return set(value).issubset({'0', '1'})

if __name__ == "__main__":
    main()