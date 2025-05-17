from tkinter import *

#create a new GUI window
window = Tk()
window.title("Soccerdex")
window.config(bg = "Red")

#instruction label
instructionlbl = Label(window, text="Enter a player's jersey number")
instructionlbl.config(bg='red', fg='black', font=16)
instructionlbl.pack()

#an entry textbox
jerseyEntry = Entry(window)
jerseyEntry.pack()

#Showplayer button
showPlayerbtn = Button(window, text="Show Player")
showPlayerbtn.config(bg="Blue", fg="White", font = 16)
showPlayerbtn.pack()

#name label
namelbl = Label(window, text="Name:")
namelbl.config(bg="Red", fg="Black", font=14)
namelbl.pack()

#nameval label
namevallbl = Label(window, text='???')
namevallbl.config(bg='red', fg='black', font = 14)
namevallbl.pack()

#position label
positionlbl = Label(window, text="Position:")
positionlbl.config(bg="Red", fg="Black", font=14)
positionlbl.pack()

#positionval label
positionvallbl = Label(window, text="???")
positionvallbl.config(bg="red", fg="black", font=14)
positionvallbl.pack()

#citizenship label

#citizenshipval label

#appearances label

#appearancesval label

#goals label

#goalval label

#reset button





window.mainloop()