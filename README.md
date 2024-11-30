# Projet Django - cc

## Auteurs
Benjamin Perez benjamin.perez@etu.univ-orleans.fr
Matis Gasse matis.gasse@etu.univ-orleans.fr
Thibault Bée thibault.bee@etu.univ-orleans.fr
Théo Leclerc Gallois theo.leclerc-gallois@etu.univ-orleans.fr


## Commandes utilisées


### Création du projet : 

``` python manage.py startproject cc ```

### Création de l'app collec_management:

``` python manage.py startapp collec_management```

### Lancement du serveur:

``` python manage.py runserver 0.0.0.0:8000```
    
### Accéder au serveur sur le navigateur : 

``` http://localhost:8088```

### Créer la migration :

``` python manage.py makemigrations ```

### Applique la migration vers la BDD :

``` python manage.py migrate ```

### load les données dans la bdd :

``` python manage.py loaddata examples ```

### Créer l'admin Django :

``` python manage.py createsuperuser ```

### Commandes après l'ajout du modèle Element pour migrer :

``` python manage.py makemigrations ```

``` python manage.py migrate ```

### Commandes pour migrer les relations entre les Collections et Elements avec les Users

``` python manage.py makemigrations ```

``` python manage.py migrate ```