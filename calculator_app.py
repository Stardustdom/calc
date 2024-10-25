import tkinter as tk
import tkinter.ttk as ttk
#tkinter: a library for building GUI applications in Python
#tkinter.ttk: for building themed GUI applications in Python (themed widgets)

# add() function is called for adding two numbers
def add(x, y): 
    return x + y

# subtract() function is called for subtracting two numbers
def subtract(x, y):
    return x - y

# multiply () function is called for multiplying two numbers
def multiply(x, y):
    return x * y

# divide() function is called for dividing first number by second number
def divide(x, y):
    if y == 0:
        return "Error! Division by zero." # error message in case of ZeroDivision error
    return x / y

class CalculatorApp:
    def __init__(self, root):
        '''
        The self parameter is a reference to the current instance of the class and is used to access variables and methods from the class. The root parameter is the Tkinter root window, which is the main window of the application.
        '''
        self.root = root # allows the class to access the Tkinter root window and its methods.
        self.root.title("Python Calculator") # sets the title of the Tkinter root window to "Python Calculator"( displayed in the title bar of the window displayed in the title bar of the window)

        # Create style object used to configure the appearance of ttk widgets
        self.style = ttk.Style() 

        # Set font sizes

        # configuration of style for all the ttk.Label widgets
        self.style.configure('TLabel', font=('Helvetica', 24, 'bold'))
        # configuration of style for all the ttk.Button widgets
        self.style.configure('TButton', font=('Helvetica', 24, 'bold'))
        # configuration of style for all the ttk.Entry widgets
        self.style.configure('TEntry', font=('Helvetica', 36))

        # Create input fields
        self.num1_label = ttk.Label(root, text="Number 1:", anchor=tk.CENTER)
        '''
        self.num1_label.grid: This is a method that adds the label to the grid geometry manager.
        text="Number 1:": This sets the text that will be displayed on the label.
        anchor=tk.CENTER: This sets the alignment of the text within the label. In this case, it's centered.

        '''
        self.num1_label.grid(row=0, column=0, sticky="nsew")
        '''
        self.num1_label.grid: This is a method that adds the label to the grid geometry manager.
        row=0: This specifies the row number where the label will be placed.
        column=0: This specifies the column number where the label will be placed.
        sticky="nsew": This makes the label expand in all directions (north, south, east, west) to fill any available space in the cell.'''
        self.num1_entry = ttk.Entry(root, justify=tk.CENTER, width=10,font=('Helvetica', 24, 'bold'))
        '''
        self.num1_entry: This is an instance variable that will hold a reference to an Entry widget (a single-line text box).
        ttk.Entry: This is a class from the ttk module that creates an Entry widget.
        root: This is the parent widget, likely the main window of the application.
        justify=tk.CENTER: This sets the alignment of the text within the entry field. In this case, it's centered.
        width=10: This sets the width of the entry field in characters.
        '''
       
        self.num1_entry.grid(row=0, column=1, sticky="nsew")
        '''
        self.num1_entry.grid: This is a method that adds the entry field to the grid geometry manager.
        row=0: This specifies the row number where the entry field will be placed.
        column=1: This specifies the column number where the entry field will be placed.
        sticky="nsew": This makes the entry field expand in all directions (north, south, east, west) to fill any available space in the cell.'''
        self.num2_label = ttk.Label(root, text="Number 2:", anchor=tk.CENTER)
        self.num2_label.grid(row=1, column=0, sticky="nsew")
        self.num2_entry = ttk.Entry(root, justify=tk.CENTER, width=10,font=('Helvetica', 24, 'bold'))
        self.num2_entry.grid(row=1, column=1, sticky="nsew")



        # Create operation buttons
        self.add_button = ttk.Button(root, text="+", command=lambda: self.calculate(add))
        self.add_button.grid(row=2, column=0, sticky="nsew")

        self.subtract_button = ttk.Button(root, text="-", command=lambda: self.calculate(subtract))
        self.subtract_button.grid(row=2, column=1, sticky="nsew")

        self.multiply_button = ttk.Button(root, text="*", command=lambda: self.calculate(multiply))
        self.multiply_button.grid(row=3, column=0, sticky="nsew")

        self.divide_button = ttk.Button(root, text="/", command=lambda: self.calculate(divide))
        self.divide_button.grid(row=3, column=1, sticky="nsew")

        # Create result label
        self.result_label = ttk.Label(root, text="Result:", anchor=tk.CENTER)
        self.result_label.grid(row=4, column=0, sticky="nsew")
        self.result_entry = ttk.Entry(root, justify=tk.CENTER, width=10, font=('Helvetica', 24, 'bold'))
        self.result_entry.grid(row=4, column=1, sticky="nsew")

        # Set row and column weights
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
        for i in range(2):
            root.grid_columnconfigure(i, weight=1)

    def calculate(self, operation):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            result = operation(num1, num2)
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, str(result))
            self.num1_entry.delete(0, tk.END)
            self.num1_entry.insert(0, str(result))  # Update num1 input field
            self.num2_entry.delete(0, tk.END)  # Clear num2 input field
        except ValueError:
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, "Invalid input")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()