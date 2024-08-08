from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
    random_num = random.randint(1, 100)

    # 2. Print out the random variable that you made in step #1
    print(random_num)
    # 3. Code a for loop to run steps 4-10, 10 times
    messagebox.showinfo(message='in this game you will have 10 tries to guess a random number from 1 to 100')
    for i in range(10):
        # 4. Ask the user for a guess using a pop-up window, and save their response
        guesser = simpledialog.askinteger(title='guess', prompt='Guess a number from 1 to 100.')
        # 5. If the guess is correct
        # 6. Win. Use 'sys.exit(0)' to end the program
        if guesser == random_num:
            messagebox.showinfo(message='you won! good job!')
            sys.exit(0)
        if guesser > random_num:
            messagebox.showinfo(message='you were too high.')
        if guesser < random_num:
            messagebox.showinfo(message='you were to low')
        # 7. if the guess is high
            # 8. Tell them it's too high
        # 9. Else if the guess is low
            # 10. Tell them it's too low
    messagebox.showinfo(message='You lost! Good luck next time!')
    # 11. Outside of the loop, tell the user they lost

    window.mainloop()
