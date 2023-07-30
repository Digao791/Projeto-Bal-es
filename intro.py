from tkinter import *
from PIL import Image, ImageTk
import baloes

def acessar_competicao():
    link = url_var.get()
    baloes.site = link
    root.destroy()
    import main
   
   

root = Tk()

root.geometry("650x700")
root.title("Gerenciamento")


image_path = "C:\\Users\\Cliente\\Desktop\\projeto_baloes\\logo.png"
pil_image = Image.open(image_path)
tk_image = ImageTk.PhotoImage(pil_image)
label_logo = Label(root, image = tk_image)
label_logo.grid(row=0, column=0, columnspan=2, sticky="new")

url_var = StringVar()

url_entry = Entry(root, textvariable=url_var, font=("Arial", 12), bd=2, width=70)
url_entry.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

btn = Button(master=root, text="Acessar competição", width=15, height=1, command=lambda :acessar_competicao())
btn.grid(row=3, column=0, padx=5, pady=5)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)


root.mainloop()
