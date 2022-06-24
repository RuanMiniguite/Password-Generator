from multiprocessing.sharedctypes import Value
from random import choice
import string
from time import sleep
from tkinter import *
import _thread
from idlelib.tooltip import Hovertip
#
def time(x):
  sleep(x)
  labelCopy['text'] = " "

def passwordGenerator():
  Password =''
  sizePassword = scaleVar.get()
  character = string.ascii_lowercase

  if var1.get() == 1:
    character = character + string.ascii_uppercase
  if var2.get() == 1:
    character = character + string.digits
  if var3.get() == 1:
    character = character + string.punctuation

  for i in range(sizePassword):
    Password += choice(character)

  # Set label new Password
  labelPassword['text'] = Password

  # Copying password to clipboard
  root.clipboard_clear()
  root.clipboard_append(Password)
  root.update()
  labelCopy['text'] = "Password Copied!"   # Show User
  _thread.start_new_thread(time, (3,))    # Delete Msg (3s)



# ----------------------------- SCREEN -----------------------------
# Setting default background color
bg = "#FFF"
bg_action = "#555"

# Boot/Conf screen
root = Tk()
root.title("Generator")
root.geometry("400x300+200+200")
root.resizable(False, False)
root.iconbitmap("Icon.ico")
root.config(bg=bg)

# Reset variable
var1     = IntVar()
var2     = IntVar()
var3     = IntVar()
scaleVar = IntVar()

# Title
labelTitle = Label (root, text="Password Generator!", 
                          font="Terminal 22", 
                          pady=10,
                          width=50,
                          bg=bg_action, 
                          fg=bg)

# Option UpperCase 
chk1 = Checkbutton (root, text="Uppercase",
                          variable=var1, 
                          onvalue=1,
                          offvalue=0,
                          font="Calibri 12",
                          bg=bg,
                          justify="left", 
                          anchor="w", 
                          width=15,
                          border=1,
                          padx=4)
var1.set(1)

# Option Number
chk2 = Checkbutton (root, text="Number",
                          variable=var2, 
                          onvalue=1,
                          offvalue=0,
                          font="Calibri 12",
                          bg=bg,
                          justify="left",
                          anchor="w",
                          width=15,
                          border=1,
                          padx=4)
var2.set(1)

# Option Special Character
chk3 = Checkbutton (root, text="Special Character",
                          variable=var3, 
                          onvalue=1,
                          offvalue=0,
                          font="Calibri 12",
                          bg=bg,
                          justify="left",
                          anchor="w",
                          width=15,
                          border=1,
                          padx=4)

# Option Size Password
scale = Scale(root, variable = scaleVar, 
                    orient='horizontal', 
                    from_= 4, 
                    to = 32, 
                    length=300,
                    sliderlength=15,
                    width=15,
                    font="Terminal 11",
                    activebackground=bg_action,
                    sliderrelief="flat",
                    troughcolor='#aaa',
                    relief="flat",
                    highlightbackground = bg,
                    bg=bg)
scaleVar.set(16)

# Password
labelPassword = Label(root, text="", 
                            font="Arial 15", 
                            pady=5, 
                            bg=bg)

# Msg Password Copy
labelCopy = Label(root, text="", 
                        font="Arial 8", 
                        pady=4, 
                        fg='red', 
                        bg=bg)

buttonGerar = Button(root,  text="GERAR SENHA",  
                            font="Terminal 20", 
                            command=passwordGenerator,
                            width=50, 
                            height=8, 
                            bg=bg_action, 
                            relief="raised", 
                            border=0, 
                            fg=bg)

myTip = Hovertip(chk1,'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
myTip = Hovertip(chk2,'0123456789')
myTip = Hovertip(chk3,'!#$%&()*+,-./:;<=>?@[\]^_`{|}~')

labelTitle.pack()
chk1.pack()
chk2.pack()
chk3.pack()
scale.pack()
labelPassword.pack()
labelCopy.pack()
buttonGerar.pack()

root.mainloop()