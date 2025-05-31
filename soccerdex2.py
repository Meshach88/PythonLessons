from tkinter import *

window = Tk()
window.title("Soccer Dex")
window.config(bg="red")

#create instruction label
instructionlbl = Label(window, text="Enter a player's jersey number:")
instructionlbl.config(bg="red", fg="black", font=16)
instructionlbl.pack()

#create an entry textbox
jerseyEntry = Entry(window)
jerseyEntry.pack()

#add a button
showPlayerButton = Button(window, text="Show Player")
showPlayerButton.config(bg="blue", fg="white", font=14)
showPlayerButton.pack()

#add name label
namelbl = Label(window, text="Name: ")
namelbl.config(bg="red", fg="black", font=16)
namelbl.pack()

#add name value
namevaluelbl = Label(window, text="???")
namevaluelbl.config(bg="red", fg="black",font=16)
namevaluelbl.pack()


window.mainloop()