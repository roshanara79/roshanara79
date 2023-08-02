import tkinter 
import random
import pyperclip
import string


window = tkinter. Tk()
window.title("Password Manager")
window.geometry("800x800")

pass_label =tkinter.Label(window, text ='Passward length', font = 'arial 15 bold')
pass_label.grid(row=14, column=2)
pass_len =  tkinter.IntVar()
length = tkinter.Spinbox(window, from_=8, to_= 32,textvariable=pass_len)
length.grid(row=14, column=4, columnspan=5)

pass_str =tkinter. StringVar()

def Generator():
    Passward = ''
    for x in range (0,4):
        Passward = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(pass_len.get()-4):
        Passward = Passward+ random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation)
    pass_str.set(Passward)



add_button= tkinter.Button(window, text= 'Generate', command= Generator )
add_button.grid(row=14, column=3, columnspan=4)

add_button= tkinter.Entry(window, textvariable= pass_str)
add_button.grid(row=17, column=3, columnspan=4)




def add_button_clicked():
    username = username_entry.get()
    

    with open("data.txt",'a') as file:
        file.write(f"{username} \n")

    username_entry.delete(0, tkinter.END)
    



heading = tkinter.Label(window, text = 'PASSWARD GENERATOR', font ='Arial, 18 bold')
heading.grid(row=0, column=3)


username_label = tkinter.Label(text ="Enter Username ",  font='arial, 15 bold italic',width=15,bd=8, fg='black')
username_label.grid(row=10, column=2)




username_entry = tkinter.Entry(width=33)
username_entry.grid(row=10, column=3, columnspan=4)








add_button = tkinter.Button(text="Add", width=20, command=add_button_clicked)
add_button.grid(row=25, column=3, columnspan=4)

add_button = tkinter.Button(text="Accept", width=20, command=add_button_clicked)
add_button.grid(row=28, column=3, columnspan=4)
add_button = tkinter.Button(text="Reset", width=20, command=add_button_clicked)
add_button.grid(row=35, column=3,columnspan=4)

window.mainloop()
