# Jarvis

Jarvis est un assistant virtuel Python à commandes vocales

## Installation

> Vous devez avoir Python **3.11** installé sur votre ordinateur

1. Cloner le repo avec `git clone`
2. Installer les dépendances avec `pip install -r requirements.txt`
3. Lancer le programme avec `python main.py`

## Modules

### Installation des modules

La procédure d'installation d'une module est relativement simple :

1. Téléchargez le module souhaité sous le format .zip

2. Dézippez le module pour en sortir le dossier

3. Ajoutez le module dans le dossier `/modules`

4. Ajoutez ses informations dans la variable `module` du fichier `/modules/modules-list.py` :
    ```
    "module_name": {
            "description": "description du module",
            "path": "module_name.main"
        }
    ```

### Formattage des modules

Les modules doivent suivre un format rigoureux :

- Le dossier doit comporter un `requirements.txt` si nécessaire
- Le fichier du module doit être nommé `main.py`
- Le fichier doit se trouver directement dans le dossier du module
- Le fichier doit avoir une class `Main` avec une majuscule
- Les méthodes de la class `Main` doivent être statiques
