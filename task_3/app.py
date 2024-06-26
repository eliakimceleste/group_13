import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk, ImageSequence
import torch
from diffusers import StableDiffusionPipeline
import threading


model_name = "hf-internal-testing/tiny-stable-diffusion-torch"
pipe = StableDiffusionPipeline.from_pretrained(model_name, torch_dtype=torch.float16) #Load the model




def generate_image():
    image_label.pack_forget()
    spinner_label.pack(pady=30)
    prompt = input.get()
    if prompt == '':
        messagebox.showwarning("Entrée manquante", "Veuillez entrer une description.")
        spinner_label.pack_forget()
        return
    # Réinitialiser l'image affichée (nouvelle ligne)
    image_label.configure(image='')
    image_label.image = None

    def load_image():
        try:
            #spinner.start()
            # Afficher le spinner
            spinner_label.pack()
            loading_label.pack(pady=5)
            spinner_label.tkraise()
            # Générer l'image
            image = pipe(prompt).images[0]
            image.save("image.png")
            # Charger et afficher l'image dans le widget d'affichage
            img = Image.open("image.png")
            img = img.resize((300, 300))  # Redimensionner l'image si nécessaire
            img_tk = ImageTk.PhotoImage(img)
            image_label.configure(image=img_tk)
            image_label.pack(pady=20)
            image_label.image = img_tk  # Garde une référence pour éviter la suppression par le garbage collector
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la génération de l'image : {e}")
        finally:
            # spinner.stop()
            # spinner.pack_forget()
            spinner_label.pack_forget()

    # Démarrer un nouveau thread pour charger l'image
    thread = threading.Thread(target=load_image)
    thread.start()


def update_spinner(ind):
    frame = spinner_frames[ind]
    ind = (ind + 1) % len(spinner_frames)
    spinner_label.configure(image=frame)
    root.after(100, update_spinner, ind)







root = tk.Tk()
root.config(bg='white')
root.title('MakitReal')
root.geometry("800x500")

# Définir les polices
titleFont = Font(
    family="Bahnschrift 15",
    size=14,
    weight="bold",
)


textFont = Font(
    family='Bahnschrift 15',
    size=10,
    weight="normal",
)



# Création des cadres gauche et droit
ffrLeft = tk.Frame(root, bg='#fcffff', height=500, )
ffrRight = tk.Frame(root, height=500, )

# Afficher l'entête
title = tk.Label(ffrLeft, text='Bring your imagination to life', bg='#fcffff',font=titleFont)
sub = tk.Label(ffrLeft, text='Generate an image from a text prompt', bg='#fcffff',font=textFont)

# Récupérer le prompt de l'utilisateur
input = tk.StringVar()
promptEntry = tk.Entry(ffrLeft, textvariable=input,bg='white', font=textFont, width=30, bd=0, relief='flat')

# Afficher le bouton Generate
generate = tk.Button(ffrLeft, text="Generate", bg='#dbfcfc', command=generate_image)

# Afficher la sortie

# Placement des widgets dans ffrLeft
title.pack(pady=10)
sub.pack(pady=5)
promptEntry.pack(pady=5)
generate.pack(pady=10)


# Placement du cadre ffrRight avec un titre et widget d'affichage d'image
titl = tk.Label(ffrRight, text=input.get())
titl.pack(pady=50)

# Charger le GIF du spinner
spinner_gif = Image.open("task_3/loading.gif")
spinner_frames = [ImageTk.PhotoImage(frame.copy().resize((100, 100), Image.Resampling.LANCZOS)) for frame in ImageSequence.Iterator(spinner_gif)]

# Créer un label pour afficher le texte de chargement
loading_label = tk.Label(ffrRight, text="Chargement en cours...")
loading_label.pack_forget()

# Créer le label pour le spinner
spinner_label = tk.Label(ffrRight)
spinner_label.pack_forget()

# Commencer l'animation du spinner
root.after(0, update_spinner, 0)

# Widget pour le spinner (progress bar indeterminate)
#spinner = Progressbar(ffrRight, mode='indeterminate', length=100)


# Placement de l'image dans ffrRight
image_label = tk.Label(ffrRight, bg='black')
image_label.pack(pady=20)
image_label.pack_forget()


# Placement des cadres gauche et droit
ffrLeft.grid(column=0, row=0, sticky="nsew")
ffrRight.grid(column=1, row=0, sticky="nsew")

# Configuration des poids des colonnes pour que les cadres prennent tout l'espace
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=4)
root.grid_rowconfigure(0, weight=1)




root.mainloop()