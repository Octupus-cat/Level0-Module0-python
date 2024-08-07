from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    messagebox.showinfo(message="your score is "+str(score)+".")
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    question1 = simpledialog.askstring(title='one', prompt='how many people are in the League logo?')
    #      // 3.  Use an if statement to check if their answer is correct
    if question1 == '5':
        score = 1
        messagebox.showinfo(message='you got it right! your score is now '+str(score)+'!')
    else:
        messagebox.showinfo(message='oh no! you were wrong. ):')
    question2 = simpledialog.askstring(title='two', prompt='what symbol is on the flag in the League logo?')
    if question2 == 'lighting bolt':
        score+=1
        messagebox.showinfo(message='good job! you were right! your score is now '+str(score)+'!')
    else:
        messagebox.showinfo(message='it was a lightning bolt. good luck next time!')
    question3 = simpledialog.askstring(title='three', prompt='what color is primarily used in the League logo?')
    #      // 4.  if the user's answer was correct, add one to their score

    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
    window.mainloop()
