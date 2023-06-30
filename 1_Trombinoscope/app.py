from tkinter import *
from PIL import Image, ImageTk
from tkinter import Tk, Canvas

window = Tk()

window.title("trombinoscope")
window.geometry("900x600")
window.config(background="#20d654")
window.iconbitmap("57122.ico")

# créer la frame principale
frame = Frame(window, bg="#20d654")#, bd=1)

# créer un titre
label_title = Label(frame, text="Tr0mBiNoScOpE", font=("Arial", 50), bg="#20d654", fg="white")
label_title.grid(row=0, column=0,sticky=N)

# Possiblité de convertir l'image :
def covertir():
    imageCharge = Image.open("my_image")
    imageConvertie = ImageTk.PhotoImage(imageCharge)
    laphoto = Label(window, image=imageConvertie)
    laphoto.pack(anchor=W)

Button(window, text = "Button", image = "laphoto", compound=LEFT)

# création d'image
width = 300
height = 300
image = PhotoImage(file="my_image").zoom("15").subsample(32)
canvas = Canvas(frame, width=width, height=height, bg="#20d654")
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=S)

# créer une sous-boîte
right_frame = Frame(frame, bg="#20d654")

# on place la sous-boîte à droite de la frame principale
right_frame.grid(row=0, column=1, sticky=W)

# créer un sous-titre
label_title1 = Label(right_frame, text="Qui voulez vous voir?", font=("Arial", 18), bg="#20d654", fg="white")
label_title1.grid(row=0, column=1, sticky=E)


# afficher la frame
frame.pack(expand=YES)


liste = Listbox(right_frame, bg="#20d62e", height=15, fg="white", font= "Arial", relief=FLAT)
liste.insert(1, "name_1")
liste.insert(2, "name_2")
# ...

liste.grid(row=2, column=1, sticky=NE)

# affichage de la fenêtre
window.mainloop()