import tkinter as tk
from PIL import Image, ImageTk
from gradio_client import Client
from tkinter import messagebox, ttk
from deep_translator import GoogleTranslator
import threading

client = Client("ByteDance/SDXL-Lightning")

def translate_to_english(text):
    "Fonction pour traduire du français vers l'anglais"
    translator = GoogleTranslator(source='fr', target='en')
    translated = translator.translate(text)
    return translated

def generate_image():
    "Fonction pour la génération d'image"
    description = description_entry.get()

    try:
        description = translate_to_english(description)
    except Exception as e:
        messagebox.showerror("Erreur de traduction", f"Erreur lors de la traduction : {e}")
        return

    if not description:
        messagebox.showwarning("Entrée manquante", "Veuillez entrer une description.")
        return

    # Affichager d'un spinner de chargement
    loading_label.pack(pady=15)
    root.update_idletasks()  # Mise a jour de l'interfce pour afficher le spinner

    def generate_image_thread():
        try:
            # Requête vers l'API
            print("INFO -- Génération de l'image")
            image_url = client.predict(
                prompt=description,
                ckpt="4-Step",
                api_name="/generate_image"
            )

            # Télgement de l'image depuis l'URL
            image = Image.open(image_url)

            # Affichage de l'image (mise à jour dans le thread principal)
            root.after(0, update_image, image)

        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la génération de l'image : {e}")

        finally:
            # Fin de chargement du spinner
            loading_label.pack_forget()

    # Demarrage du thread pour générer l'image.................
    thread = threading.Thread(target=generate_image_thread)
    thread.start()

def update_image(image):
    "Fonction pour mettre à jour l'affichage de l'image dans l'interface"
    try:
        # Redimensionner l'image
        image = image.resize((300, 300))
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo
        description_entry.delete(0, tk.END)  # Réinitialiser l'entrée de texte 
    except Exception as e:
        messagebox.showerror("Erreur d'affichage", f"Erreur lors de l'affichage de l'image : {e}")

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Générateur d'images à partir de texte")
    root.geometry("600x400")

    # Zone de texte pour saisir la description
    description_entry = tk.Entry(root, width=50)
    description_entry.pack(pady=10)

    # Bouton pour générer l'image
    generate_button = tk.Button(root, text="Générer l'image", command=generate_image)
    generate_button.pack(pady=5)

    # Indicateur de chargment (spinner)
    loading_image = tk.PhotoImage(file="loading.gif")
    loading_label = tk.Label(root, image=loading_image)

    # Zone d'affichage pour l'image générée
    image_label = tk.Label(root)
    image_label.pack(pady=10)

    # Exécuter l'application
    root.mainloop()
