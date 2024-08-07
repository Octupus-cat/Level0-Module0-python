from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    messagebox.showinfo(message="your score starts at "+str(score)+". If you get a question right, you gain one point. If you get it wrong, you lose one point. good luck!")
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    question1 = simpledialog.askstring(title='one', prompt='how many people are in the League logo?')
    #      // 3.  Use an if statement to check if their answer is correct
    if question1 == '5':
        score = 1
        messagebox.showinfo(message='you got it right! your score is now '+str(score)+'!')
    else:
        score -= 1
        messagebox.showinfo(message='oh no! you were wrong. there are 5 people. your score is now '+str(score)+' ):')
    question2 = simpledialog.askstring(title='two', prompt='what symbol is on the flag in the League logo?')
    if question2 == 'lightning bolt':
        score += 1
        messagebox.showinfo(message='good job! you were right! your score is now '+str(score)+'!')
    else:
        score -= 1
        messagebox.showinfo(message='it was a lightning bolt. good luck next time! your score is now'+str(score)+'.')
    question3 = simpledialog.askstring(title='three', prompt='what color is primarily used in the League logo?')
    if question3 == 'orange':
        score += 1
        messagebox.showinfo(message='awesome! your score is now '+str(score)+'!')
    else:
        score -= 1
        messagebox.showinfo(message='the correct answer was orange, so your score is '+str(score)+'. better luck next time!')
    question4 = simpledialog.askstring(title='four', prompt='what is the Leagues full name?')
    if question4 == 'The LEAGUE of Amazing Programmers':
        score += 2
        messagebox.showinfo(message='wow! that was a hard one, so you get two points, bringing you up to '+str(score)+' points!')
    else:
        messagebox.showinfo(message='that one was really hard, and long, so you keep all your points. the correct answer was The LEAGUE of Amazing Programmers')
    question5 = simpledialog.askstring(title='five', prompt='one last question. What color are the words and pictures in the logo drawn in?')
    if question5 == 'white':
        score += 1
        messagebox.showinfo(message='you got that question right, so your score is now '+str(score)+'!')
    else:
        score -= 1
        messagebox.showinfo(message='the correct answer was white, so you got it wrong. now your score is '+str(score)+'.')
    messagebox.showinfo(message='you finished the quiz with '+str(score)+'/6. good job!')
    #      // 4.  if the user's answer was correct, add one to their score

    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
    window.mainloop()
