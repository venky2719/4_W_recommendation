from tkinter import *
import os

app=Tk()

def frame2():
	os.system('Car_Recommendation_System.py')
	

########################

######################## Text Box
text=Text(app, height=4, width=25, bg='#252525', fg='yellow', font=('',14), bd=-2)
text.insert(5.0, "Developers :\Chandi,Keshav,Venketesh,Akshat")
text.config(state='disabled')
text.place(x=750, y=450)
########################

######################## Buttons
exit_button = Button(app, text = 'EXIT', width = 2, command = app.destroy, fg='grey', font=('',30), bd=-2)
exit_button.place(x=50,y=445)

continue_button = Button(app, text = 'CONTINUE', width = 8, height = 1, bg='#7CFC00', fg='red', font=('',30), borderwidth=5, command=frame2())
continue_button.place(x=560,y=250)
########################

app.mainloop()
