import tkinter as tk
from menu import Menu

values = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', 
 '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 
 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

class Play(Menu):
    def __init__(self):
        """
        Initiate the playing

        """
        tk.Tk.__init__(self)
        self.main_window()

        # Choose mode for the playthrough.
        self.choose_mode()
    
    def choose_mode(self):
            # Welcome Label
            welcome_label = tk.Label(self, text = "Before we begin,", font = "Courier")
            welcome_label.pack(pady = (80,0))

            # Choose Label
            choose_mode = tk.Label(self, text = "Choose your mode.", font = "Courier")
            choose_mode.pack(padx = 10, pady = 10)

            # Binary Button
            binary_button = tk.Button(self, text = "Binary", font = "Courier", command = lambda: self.start_game("binary"), width = 15)
            binary_button.pack(padx = 10, pady = 10)

            # Hexadecimal Button
            hex_button = tk.Button(self, text = "Hexadecimal", font = "Courier", command = lambda: self.start_game("hex"), width = 15)
            hex_button.pack(padx = 10, pady = 10)

            # Mishap Button
            go_back = tk.Button(self, text = "Oops, wrong button.", font = "Courier", command = self.go_back)
            go_back.pack(pady = 10)

    def start_game(self, mode):
        canvas = tk.Canvas(self, width = 400, height = 500, bg = "black")
        canvas.pack()

        
    def create_block(self):
        pass
    def move_block(self):
        pass
    def destory_block(self):
        pass

    # Go back to the main menu.
    def go_back(self):
        self.destroy()
        menu = Menu()
        menu.mainloop()