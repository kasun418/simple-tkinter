from tkinter import *
#from tkinter.ttk import * 

word = "" 
   
def press(letter): 
    
    global word 
    word = name.get()
 
    word = word + str(letter) 
    name.set(word)

def reverse():
	global word
	word = word[::-1]
	name.set(word)


def reset_entry_field(event,field):
	field.delete(0,'end')
	field["foreground"]="black"
  
def mouse_enter_leave(event,text,field_name):
	field_name.set(text)

def event_background(event, colour, field):
    field["background"] = colour


def select_colour(event, colour,field):
    field["foreground"] = colour


root = Tk()

root.configure(background="#e2e2ff")
root.title("SANDUNI WANASINGHE") 
root.geometry("505x350")
root.resizable(False,False)

top_frame = Frame(root, width=200, height= 10, bg='#e2e2ff')
top_frame.grid(row=0, column=0, padx=10,pady=10,)

middle_frame = Frame(root, width=180, height=400, bg='#e2e2ff')
middle_frame.grid(row=1, column=0, padx=10, pady=5)

bottem_frame = Frame(root, width=180, height=15, bg='#e2e2ff')
bottem_frame.grid(row=2, column=0, padx=10, pady=5)


# top frame features
mouse_move_strings = StringVar() 

lbl_top = Label(top_frame, textvariable=mouse_move_strings,width=60,height=1,background='#00ffff')
lbl_top.grid(row=0, columnspan=3)
lbl_top.bind("<Enter>",lambda event: mouse_enter_leave(event,"S14959",mouse_move_strings))
lbl_top.bind("<Leave>",lambda event: mouse_enter_leave(event,"",mouse_move_strings))

# Entry field feature
name= StringVar() 
word_field = Entry(top_frame, textvariable=name,font="none 9 bold", width=60, justify='right')
word_field.grid(row=1,columnspan=3)
# used argument for make the method reusable-
word_field.bind("<Button-3>",lambda event, arg=word_field: reset_entry_field(event,arg))

# middle frame features
# button functions section
button1 = Button(middle_frame, text=' S ', fg='black', bg='#8080ff', 
             command=lambda: press("S"), height=2, width=15).grid(row=2, column=0) 
   
  
button2 = Button(middle_frame, text=' A ', fg='black', bg='#8080ff', 
                 command=lambda: press("A"), height=2, width=15).grid(row=2, column=1) 


button15 = Button(middle_frame, text=' N ', fg='black', bg='#8080ff', 
                 command=lambda: press("N"), height=2, width=15).grid(row=2, column=2) 


button4 = Button(middle_frame, text=' D ', fg='black', bg='#8080ff', 
                 command=lambda: press("D"), height=2, width=15).grid(row=3, column=0) 


button5 = Button(middle_frame, text=' U ', fg='black', bg='#8080ff', 
                 command=lambda: press("U"), height=2, width=15).grid(row=3, column=1) 


button6 = Button(middle_frame, text=' I ', fg='black', bg='#8080ff', 
                 command=lambda: press("I"), height=2, width=15).grid(row=3, column=2) 


button2 = Button(middle_frame, text=' W ', fg='black', bg='#8080ff', 
                 command=lambda: press("W"), height=2, width=15).grid(row=4, column=0) 


button8 = Button(middle_frame, text=' G ', fg='black', bg='#8080ff', 
                 command=lambda: press("G"), height=2, width=15).grid(row=4, column=1)  


button9 = Button(middle_frame, text=' H ', fg='black', bg='#8080ff', 
                 command=lambda: press("H"), height=2, width=15).grid(row=4, column=2)

button10 = Button(middle_frame, text=' E ', fg='black', bg='#8080ff', 
                 command=lambda: press("E"), height=2, width=15).grid(row=5, column=0)

button11 = Button(middle_frame, text=' Space ', fg='black', bg='#8080ff', 
                 command=lambda: press(" "), height=2, width=15).grid(row=5, column=1)

button12 = Button(middle_frame, text=' Reverse ', fg='black', bg='#8080ff', 
                 command=lambda: reverse(), height=2, width=15).grid(row=5, column=2)

# bottem frame features
name_string = StringVar(bottem_frame, value='SANDUNI WANASINGHE')
name_field = Entry(bottem_frame, textvariable=name_string, font="none 9 bold", width=60, foreground='white')
name_field.grid(row=0, columnspan=8)

name_field.bind("<Enter>",lambda event: event_background(event,"black",name_field))
name_field.bind("<Leave>",lambda event: event_background(event,"white",name_field))

lbl_tag = Label(bottem_frame, text="Select the Display Colour:",height=1,background='#e2e2ff')
lbl_tag.grid(row=1, columnspan=4)

lbl_red = Label(bottem_frame,width=9,height=1,background='red')
lbl_red.grid(row=1, column=4)
lbl_red.bind("<Button-1>", lambda event: select_colour(event,"red",word_field))

lbl_blue = Label(bottem_frame,width=9,height=1,background='blue')
lbl_blue.grid(row=1, column=5)
lbl_blue.bind("<Button-1>", lambda event: select_colour(event,"blue",word_field))

lbl_yellow = Label(bottem_frame,width=9,height=1,background='#ffc85c')
lbl_yellow.grid(row=1, column=6)
lbl_yellow.bind("<Button-1>", lambda event: select_colour(event,"#ffc85c",word_field))

lbl_green = Label(bottem_frame,width=9,height=1,background='green')
lbl_green.grid(row=1, column=7)
lbl_green.bind("<Button-1>", lambda event: select_colour(event,"green",word_field))


root.mainloop()
