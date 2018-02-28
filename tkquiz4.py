from Tkinter import *
import tkMessageBox
from questions import *
top = Tk()
top.geometry('1366x728')
i = 0

photo = PhotoImage(file="dolphins.gif")
q = Label(top, image = photo)
q.photo = photo


name_label = Label(top, text="Your name: ", anchor = CENTER, height = 3, pady = 2, font = 'Helvetica -30 bold')
name_entry = Entry(top, bd=7, font = 'Helvetica -30 italic')
number_label = Label(top, text = "Your number: ", anchor = CENTER, height = 3, pady = 2, font = 'Helvetica -30 bold')
number_entry = Entry (top, bd = 7, font = 'Helvetica -30 italic')
level_label = Label(top, height = 2, bg = "blue", fg = "white", font = "Helvetica -30")
level = 1
name = ""
number = 0
score = 0
hello = Label(top)
intro = Label(top, text = "T H E   P Y T H O N   Q U I Z", height = 3, width = 2, pady = 3, font ='Haettenschweiler -45', fg = 'blue', bg = 'white')


def get_details():
	global name 
	global number
	name = name_entry.get()
	number = number_entry.get()
	name_label.destroy()
	name_entry.destroy()
	number_label.destroy()
	number_entry.destroy()
	submit1.destroy()
	hello.config(text = "Hello, "+name+"! Get ready to play.", height = 15, pady = 3, font ='Arial -20 bold', fg = 'black')
	hello.pack()
	b.pack()

submit1 = Button(top, text = "Submit", height = 3, width = 7, relief=RAISED,fg = "white", bg = "black", font = 'Helvetica -20 bold', command = get_details)

intro.pack(fill = X)
name_label.pack()
name_entry.pack()
number_label.pack()
number_entry.pack()
submit1.pack(expand = True)

#---------------------------------------------------------------------------------------------------------
qlist = [q1, q2, q3, q4,q5,q6,q7,q8,q9,q10,q11,q12,q13]
alist = []

correct = []
wrong = []
question = Label(top, height = 5, font ='Helvetica -22 bold' )
answer = IntVar()
b1 = Radiobutton(top, variable = answer, value = 1, font ='Helvetica -22 bold' )
b2 = Radiobutton(top, variable = answer, value = 2, font ='Helvetica -22 bold' )
b3 = Radiobutton(top, variable = answer, value = 3, font ='Helvetica -22 bold' )
b4 = Radiobutton(top, variable = answer, value = 4, font ='Helvetica -22 bold' )
options = [b1, b2, b3, b4]
submit2 = Button(top, text = "Submit", relief = RAISED, fg = "white", bg = "purple", font = "Arial -30 italic")
#-----------------------------------------------------------------------------------------------------------------------

def begin():
	hello.destroy()
	b.destroy()
	level_label.config(text = "Level 1")
	level_label.pack(fill=X)
	Button(top, text = "Quit", bg = "white", fg = "red", font = "Arial -20 bold", relief = GROOVE, anchor = S, command = top.quit).pack(fill = Y, side = BOTTOM)
	questions()

b = Button(top, text = "Begin", relief=RAISED,fg = "white", bg = "purple", font = "Arial -30 italic", command = begin)
over = Label(top, text = 'Quiz over!', font = 'Helvetica -30 bold', fg = 'blue', height = 5)


def result():
	score=0
	for x in range(13):
		if alist[x] == rlist[x]:
			correct.append(x+1)
			score+=1
		else:
			wrong.append(x+1)
	level_label.destroy()
	over.destroy()
	seeresult.destroy()
	Label(top, text = "Total score: "+str(score), font = 'Arial -25 bold', height = 5, fg = 'blue').pack()
	Label(top, text = "Correct answers: "+str(correct), font = 'Arial -25 bold', height = 5, fg = 'green').pack()
	Label(top, text = "Wrong answers: "+str(wrong), font = 'Arial -25 bold', height = 5, fg = 'red').pack()

seeresult = Button(top, text = "See result",font = 'Arial -20 italic', fg = 'white', bg = 'purple', height = 4, width = 30, command = result)

def next_level():
	global level
	level+=1
	changelevel.pack_forget()
	seeresult.pack_forget()
	level_label.config(text = "Level "+str(level))
	submit2.config(state = NORMAL)
	questions()


changelevel= Button(top, text = "Go to the next level", font = 'Arial -20 italic', fg = 'white', bg = 'purple', height = 4, width = 30, command = next_level)
def submit(x):
	alist.append(x)
	answer.set(0)
	if not (i==4 or i==8 or i==12) and i<13:
		questions()
	elif (i==4 or i==8 or i==12):
		submit2.pack_forget()
		question.pack_forget()
		b1.pack_forget()
		b2.pack_forget()
		b3.pack_forget()
		b4.pack_forget()
		changelevel.pack(expand = True)
	elif i==13:
		q.destroy()
		submit2.pack_forget()
		question.pack_forget()
		b1.pack_forget()
		b2.pack_forget()
		b3.pack_forget()
		b4.pack_forget()
		over.pack(fill=X)
		seeresult.config(text = "See result", command = result)
		seeresult.pack()


def questions():
	global i
	question.config(text = qlist[i].q)
	if i==12:
		q.config(height=100, anchor = S)
		q.pack()
	question.pack()
	b1.config(text = qlist[i].a1)
	b1.pack()
	b2.config(text = qlist[i].a2)
	b2.pack()
	b3.config(text = qlist[i].a3)
	b3.pack()
	b4.config(text = qlist[i].a4)
	b4.pack()
	i+=1
	submit2.config(command = lambda: submit(answer.get()))
	submit2.pack(expand=True)

mainloop()