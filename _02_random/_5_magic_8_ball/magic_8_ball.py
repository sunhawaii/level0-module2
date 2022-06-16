import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    question = simpledialog.askstring(None, prompt="Ask a question to the all powerful magic eight ball.")
    # Make a variable and initialize it to a random number between 0 and 3
    number = random.randint(0, 3)

    if number == 0:
        messagebox.showinfo(None, "Yes")

    if number == 1:
        messagebox.showinfo(None, "No")

    if number == 2:
        messagebox.showinfo(None, "Ask Google.")

    if number == 3:
        messagebox.showinfo(None, "You shall die for asking the all powerful magic eight ball this question.")




























    # If the random number is 1

        # tell the user "No"

    # If the random number is 2

        # tell the user "Maybe you should ask Google?"

    # If the random number is 3

        # write your own answer
