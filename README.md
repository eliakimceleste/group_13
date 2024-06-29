# Groupe 13: Projet de **Python avancé et R**
Le projet est un devoir pour valider les compétences acquises lors du cours de __Python avancé et R__. Ce projet est divisé en trois tâches distinctes, chacun abordant des aspects du cours.

## Prérequis
- **Python 3.x** installé sur votre machine
- **tkinter** installé
- **pip** installé (devrait être inclus avec Python 3.x)
- **R** et le package `ggplot2` si vous voulez exécuter le code R

## Configuration de l'environnement virtuel et installation des dépendances

1. Clonez le référentiel sur votre ordinateur local

   ```
   git clone https://github.com/eliakimceleste/group_13.git
      ```
2. Accéder au dossier du projet

    ```
    cd group_13
      ```
3. Créer un environnement virtuel

   ##### Windows
   ```
   python -m venv env
    ```
   ##### Linux
   ```
   python3 -m venv env
    ```
4. Activer l'environnement virtuel
  
   ##### Windows
      ```
   .\env\Scripts\activate
      ```
   ##### Linux
   ```
   source env/bin/activate
    ```
5. Installer les packages à partir de requirements.txt

    ```
   pip install -r requirements.txt
    ```


## Usage
   ### Tâche1
   Accéder au dossier avec la commande  
   ```
cd task_1
```
   
   Exécutez le script  avec la commande :
   - Windows
       ```
      python numpy.py
       ```
   - Linux
        ```
      python3 numpy.py
        ```
   
   ### Tâche2
   Accéder au dossier avec la commande  
  ```
cd task_2
```

   Exécutez le script  avec la commande :
  ```
python hist.py
Rscript hist.R
python scatter.py
Rscript scatter.R
```
   
   ### Tâche3
   Accéder au dossier avec la commande  
  ```
cd task_3
```

   Exécutez le script  avec la commande :
   - Windows
       ```
      python app.py
       ```
   - Linux
        ```
      python3 app.py
        ```

## Rapport
Voir le [fichier](./documentation.docx) vers le rapport 



