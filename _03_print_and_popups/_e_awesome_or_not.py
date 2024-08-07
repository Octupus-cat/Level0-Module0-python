from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    bob = random.randint(0, 3)
    # 2. Print your variable to the console
    print(bob)
    # 3. Get the user to enter something that they think is awesome
    question = simpledialog.askstring(title='question', prompt='what is something you think is awesome?')
    # 4. If your variable is  0
    # -- tell the user whatever they entered is awesome!
    if bob == 0:
        messagebox.showinfo(message='yeah, i agree, that is awesome')
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    if bob == 1:
        messagebox.showinfo(message='that is ok, i guess.')
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    if bob == 2:
        messagebox.showinfo(message='no, that is kinda boring')
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
    if bob == 3:
        messagebox.showinfo(message='that is the most awesome thing in the universe, in fact, it is more awesome than awesomeness itself')
    # Run the window's .mainloop() method
    window.mainloop()
