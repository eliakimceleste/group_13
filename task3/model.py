#Load the libraries
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from io import BytesIO
import torch
from diffusers import DiffusionPipeline



model_name = "hf-internal-testing/tiny-stable-diffusion-torch"
pipe = StableDiffusionPipeline.from_pretrained(model_name, torch_dtype=torch.float16) #Load the model
prompt = "a photo of an astronaut riding a horse on mars" #input from user
image = pipe(prompt).images[0] #Generate image
image.save("astronaut.png") #Save image
image.show() #Show image



# Charger le modèle et le pipeline de Hugging Face
model_id = "hf-internal-testing/tiny-stable-diffusion-pipe"
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = DiffusionPipeline.from_pretrained(model_id)
pipe = pipe.to(device)

# Fonction pour générer l'image
def generate_image():
    description = description_entry.get()
    if not description:
        messagebox.showwarning("Entrée manquante", "Veuillez entrer une description.")
        return
    
    # Afficher le spinner de chargement
    progressbar.start()
    root.update_idletasks()  # Mettre à jour l'interface pour afficher le spinner

    try:
        # Générer l'image
        with torch.no_grad():
            result = pipe(description)
            image = result.images[0]

        # Sauvegarder l'image dans un buffer
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        buffered.seek(0)

        # Mettre à jour l'interface utilisateur avec l'image générée
        image = Image.open(buffered)
        image = image.resize((300, 300))  # Redimensionnez selon vos besoins
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo

    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de la génération de l'image : {e}")
    
    finally:
        # Arrêter le spinner de chargement
        progressbar.stop()

# Initialiser la fenêtre principale
root = tk.Tk()
root.title("Générateur d'images à partir de texte")
root.geometry("600x400")

# Zone de texte pour saisir la description
description_entry = tk.Entry(root, width=50)
description_entry.pack(pady=10)

# Bouton pour générer l'image
generate_button = tk.Button(root, text="Générer l'image", command=generate_image)
generate_button.pack(pady=10)

# Indicateur de chargement (spinner)
progressbar = ttk.Progressbar(root, mode='indeterminate')
progressbar.pack(pady=10)

# Zone d'affichage pour l'image générée
image_label = tk.Label(root)
image_label.pack(pady=10)

# Exécuter l'application
root.mainloop()
