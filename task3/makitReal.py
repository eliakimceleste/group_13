import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
import torch
from diffusers import StableDiffusionPipeline



model_name = "hf-internal-testing/tiny-stable-diffusion-torch"
pipe = StableDiffusionPipeline.from_pretrained(model_name, torch_dtype=torch.float16) #Load the model




def generate_image():
    spinner.pack(pady=30)
    
    prompt = input.get()
    if prompt == '':
        messagebox.showwarning("Entrée manquante", "Veuillez entrer une description.")
        return
    ### spiner
    
    
    try:
        spinner.start()
        
        image = pipe(prompt).images[0] #Generate image
        image.save("image.png") #Save image
        # Charger et afficher l'image dans le widget d'affichage
        img = Image.open("image.png")
        img = img.resize((300, 300))  # Redimensionner l'image si nécessaire
        img_tk = ImageTk.PhotoImage(img)
        image_label.configure(image=img_tk)
        image_label.image = img_tk  # Garde une référence pour éviter la suppression par le garbage collector
        
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de la génération de l'image : {e}")
    
    finally:
        spinner.stop
        pass































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

# Widget pour le spinner (progress bar indeterminate)
spinner = Progressbar(ffrRight, mode='indeterminate', length=100)


# Placement de l'image dans ffrRight
image_label = tk.Label(ffrRight, bg='black')
image_label.pack(pady=20)

# Placement des cadres gauche et droit
ffrLeft.grid(column=0, row=0, sticky="nsew")
ffrRight.grid(column=1, row=0, sticky="nsew")

# Configuration des poids des colonnes pour que les cadres prennent tout l'espace
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=4)
root.grid_rowconfigure(0, weight=1)




root.mainloop()