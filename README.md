# Rapport du groupe 13
Le projet est un devoir pour valider les compétences acquises lors du cours de __Python avancé et R__. Ce projet est divisé en trois tâches distinctes, chacun bordant des aspects du cours.

## Prérequis
- **Python 3.x** installé sur votre machine
- **pip** installé devrait être inclus avec Python 3.x

## Installation
1. Clonez le référentiel sur votre ordinateur local
   ```
   git clone https://github.com/eliakimceleste/group_13.git
   ```
2. Accéder au dossier du projet
	 ```
   cd group_13
   ```
3. Assurez-vous d'avoir installer __python__ sur votre ordinateur
## Usage

4. Créer un environnement virtuel pour y installer toutes dépendances
    ```
python -m venv 
 ```
  
Exécutez le script du jeu avec la commande :
 ```
python minimax.py
 ```


## Tâche3
Nous avons créeé un interface utilisateur à l'aide du module ``` tkinter ``` de python contenant une **zone de texte** pour saisir la description d'une image à générer, un **bouton** pour générer l'image, une **zone d'affichage** pour montrer l'image générée et un **spinner(indicateur de chargement)** qui apparaît pendant la génération de l'image.

Nous avons utilisé le modèle tiny ```tiny-stable-diffusion-torch``` de **StableDiffusion** qui est disponible sur **HuggingFace**.

