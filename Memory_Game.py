import random
import time
from tkinter import *
#pencere özellikleri
root=Tk()
root.title("MEMORY GAME")
root.geometry("500x500")
root.tk_setPalette("white")

label = Label(root,fg="black",font="Helvetice 55 bold")

entry = Entry(bg="purple")
input_count = 3
string = ''
list = []
inp = []
inp2 = []
temp_inpcount = 0

def  takeInput():
    global input_count, temp_inpcount, string, list, inp, inp2

    inp.append(entry.get())
    entry.delete(0, 'end')

    if list[len(list)-1] == ' ':
        list.pop(input_count)

    for i in range(len(list)):
        string += str(list[i])
    inp2.append(string)

    if inp2 == inp:
        list.clear()
        inp.clear()
        inp2.clear()
        string = ''
        input_count = temp_inpcount
        temp_inpcount = 0
        newEntryArea()
        label.place(x = random.randint(30, 400), y = random.randint(30,300))
        showRandom(random.randint(0, 9))
    else:
        #giriş ve button kaldırılır
        entry.destroy() 
        button.destroy()
        e = Label(text = "\n\nYOU LOSE !!\nGAME IS OVER!!", fg = "black", font = "Helvetice 20 bold")
        e.pack()

#ekranda rastgele sayılar gösterir
def showRandom(random_number):
    global input_count, temp_inpcount

    label['text'] = random_number #sayıların ekranda görünmesi
    list.append(random_number)
    input_count -= 1

    if input_count > 0:
       root.after(2000, showRandom, random.randint(0,9))

    temp_inpcount += 1
    label.place(x = random.randint(30,400), y = random.randint(30,300))

    if input_count == 0:
        root.after(2000, showRandom, ' ')
        entry.pack(side = BOTTOM, ipadx = 10, ipady = 12)

#her adımda giriş alanını tekrar oluşturur
def newEntryArea():
          global entry
          entry.destroy()
          entry = Entry(bg="purple")



label.place(x = random.randint(30,400), y = random.randint(30,300))

showRandom(random.randint(0,9))
button = Button(text = "ENTER", command = takeInput, width = 5, height = 1, font = "Helvetice 25 bold", fg = "black", bg = "grey")

button.pack(side = BOTTOM)


root.mainloop()
