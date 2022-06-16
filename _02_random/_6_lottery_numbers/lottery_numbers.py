import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket

    number1 = random.randint(1, 9)
    number2 = random.randint(1, 9)
    number3 = random.randint(1, 9)
    number4 = random.randint(1, 9)
    number5 = random.randint(1, 9)
    number6 = random.randint(1, 9)

    messagebox.showinfo(None, number1, number2, number3, number4, number5, number6)

    # TODO 2) Display the selected numbers to the user in a pop-up

    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
