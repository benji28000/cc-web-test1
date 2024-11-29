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

### Migrer les migrations unapplied:
    
```  python manage.py migrate```

### Lancement du serveur:

``` python manage.py runserver 0.0.0.0:8000```
    
### Accéder au serveur sur le navigateur : 

``` http://localhost:8088```

### Créer la migration :

``` python manage.py makemigrations ```

### Applique la migration vers la BDD :

``` python manage.py migrate ```

### Ajouter des données au modèle :

```
>>> from collec_management.models import Collec
>>> collections = [
... Collec(title="Minecraft", description="Minecraft est un jeu vidéo de type aventure « bac à sable » (construction complètement libre) développé par le Suédois Markus Persson, alias Notch, puis par la société Mojang Studios. Il s'agit d'un univers composé de voxels et généré de façon procédurale, qui intègre un système d'artisanat axé sur l'exploitation puis la transformation de ressources naturelles (minéralogiques, fossiles, animales et végétales)."),
... Collec(title="Fortnite", description="Fortnite est un jeu en ligne développé par Epic Games sous la forme de différents modes de jeu qui partagent le même gameplay général et le même moteur de jeu. Les deux premiers modes de jeu sont Fortnite : Sauver le monde, un jeu coopératif de tir et de survie conçu pour quatre joueurs au maximum et dont le but est de combattre des zombies et de défendre des objets à l'aide de fortifications, et Fortnite Battle Royale, un jeu de battle royale en free-to-play où jusqu'à 100 joueurs se battent entre eux jusqu'au dernier survivant. Plusieurs autres modes de jeu sont ensuite ajoutés."),
... Collec(title="Call of Duty", description="Call of Duty ou COD (en français l'« Appel du devoir ») est une série de jeux vidéo de tir à la première personne sur la guerre, dont le premier opus est publié en 2003 par le studio Infinity Ward et l'éditeur Activision. Les épisodes prennent place lors de la Seconde Guerre mondiale ou lors de conflits modernes fictifs."),
... Collec(title="Les Sims", description="Les Sims est une série de jeux vidéo de simulation de vie de type bac à sable, développée par Maxis et édité par Electronic Arts. L'univers des Sims est une projection humoristique et décalée de la société de consommation où il n'existe pas d'objectif précis. Le joueur doit simplement gérer les besoins de ses personnages, nommés « sims », et leur faire mener la vie qu'il désire."),
... Collec(title="Battlefield",description="Battlefield (de l'anglais, signifiant littéralement « Champ de bataille ») est une série de jeux vidéo de tir à la première personne développée par DICE et éditée par Electronic Arts, qui a débuté par le jeu Battlefield 1942 en 2002."),
... Collec(title="League Of Legends", description="League of Legends (abrégé LoL) est un jeu vidéo sorti en 2009 de type arène de bataille en ligne, free-to-play, développé et édité par Riot Games sur Windows et Mac OS."),
... Collec(title="Valorant",description="Valorant (stylisé VALORANT) est un jeu vidéo free-to-play de tir à la première personne (FPS) en multijoueur développé et édité par Riot Games et sorti le 2 juin 2020."),
... Collec(title="Tomb Raider", description="Tomb Raider (/tum ˈreɪdər/) est une franchise constituée de jeux vidéo d'action-aventure, de comics, romans et de films se centrant sur les aventures du personnage de fiction Lara Croft, aventurière britannique inspirant le titre de la franchise (« Pilleur de tombe » en français)."),
... Collec(title="The Legend Of Zelda", description="The Legend of Zelda (ゼルダの伝説, Zeruda no densetsu?), ou simplement Zelda, est une série de jeux vidéo d'action-aventure produite par la société japonaise Nintendo et créée par Shigeru Miyamoto et Takashi Tezuka. Depuis 1986 et la sortie du jeu The Legend of Zelda sur la console NES, vingt-et-un jeux font officiellement partie de la saga principale."),
... Collec(title="PokémonN 1", description="PokémonN 1 (prononcé [pɔ.ke.mɔn], connue au Japon sous le nom de Pocket MonstersN 2) est une franchise créée par Satoshi Tajiri en 1995, présente en particulier en jeu vidéo, dans des séries éditées par Nintendo. Selon les statistiques de Nintendo en 2010, les jeux Pokémon se sont vendus à environ 250 millions d’unités. Le jeu vidéo Pokémon Rouge et Bleu s’est vendu à plus de 30 millions d’exemplaires, ce qui en fait un record des ventes dans l’histoire du jeu vidéo."),
... Collec(title="Street Fighter", description="Street Fighter (ストリートファイター, Sutorīto Faitā?) est une série de jeux vidéo de combat en un contre un développée par Capcom, dont le premier épisode est publié en 1987."),
... Collec(title="Resident Evil", description="Resident Evil, connue au Japon sous le nom Biohazard (バイオハザード, Baiohazādo?), est une série de jeux vidéo d'aventure, action et réflexion de type survival horror. La franchise appartient à la société japonaise Capcom.")
... ]
>>> for element in collections:
...    element.save()
exit()
```

### Extraire les données au format .json

``` python manage.py dumpdata collec_management.Collec --indent 3 > collec_management/fixtures/examples.json ```