Kholloscope
===========

**Petit Framework pour grand kholloscope.**  
Publier facilement, en Python, le kholloscope d'une classe préparatoire.

Utilisation
-----------

Ce projet vise à simplifier au maximum la mise en place d'un kholloscope, *via* Internet.
Cet outil propose les avantages suivants :

* Configuration simple — toujours sur [tableur](http://fr.wikipedia.org/wiki/Tableur)
* Interface ergonomique — complètement [bootstrap](http://getbootstrap.com)
* Vue mobile spécifique — entièrement [responsive](http://fr.wikipedia.org/wiki/Site_web_adaptatif)
* Programmé en Python — au [programme](http://python-prepa.github.io)
* Aucune dépendance logicielle — seulement [Python](http://www.python.org)
* Licence libre — pleinement [MIT](LICENSE)
* Multi-classes possible
* Poids minimal, documentation comprise

Installation
------------

L'unique nécessité est de disposer d'un serveur web sur lequel
est l'environnement Python est disponible.  
Votre établissement n'en dispose pas d'un ? Il existe des 
[solutions faciles](http://wiki.python.org/moin/FreeHosts).

Ensuite par étapes :

1. Décompresser l'[archive du projet](https://github.com/LeoColomb/kholloscope/archive/master.zip) 
dans un répertoire du serveur, de préférence à la racine.
2. Vérifier que la [configuration](#configuration) corresponde à vos besoins.
3. Modifier le [fichier du tableau de colles](#initialisation) dans le dossier `data`.
4. C'est fini !

Configuration
-------------

Dans le fichier `setup.py`, il est possible de paramétrer les valeurs suivantes :

### `_annee`
Date de début d'année
_Par défaut, `_debug = False`._

### `_debug`
Permet de passer en mode débogage, et obtenir davantage de détails lors d'une erreur.  
Particulièrement utile lors de problèmes à répétition. N'hésitez pas alors à ouvrir un 
[ticket](https://github.com/LeoColomb/kholloscope/issues/new) !  
_Par défaut, `_debug = False`._

### `_path`
Si jamais la racine du dossier du projet n'est pas la même que celle 
du serveur, attribuer à `_path` le chemin URL d'accès.  
Par exemple : Kholloscope de MPSI accessible à `http://example.com/un/deux/trois/mpsi`,
alors `_path = "un/deux/trois/"`.  
_Par défaut, `_path = ""`._

### `_port`
Au cas où l'accès HTTP au serveur se fait par un port diffèrent de `80`.  
_Par défaut, `_path = 8080`, et aucun changement n'est nécessaire._

### `_route`
Défini comment le nom de la classe doit être analysé à partir l'URI.  
_Par défaut, `_route = "/<classe:re:[a-zA-Z]+>"`._

Initialisation
--------------

Dans le dossier `data` sont sauvegardé les différents kholloscopes de chaque
classe. Pour cela, quelques indications :

* **Le nom du fichier est le nom de la classe en question.**  
  Il définira l'URI spécifique à cette classe, telle que [`_route`](#_route) l'indique.  
  Par exemple, le fichier s'appelle `mpsi.csv`, alors on y accède *via* `http://example.com/mpsi`.  
  Noter l'absence d'extension.

* **Le fichier doit être au format [CSV](http://fr.wikipedia.org/wiki/Comma-separated_values).**  
  Les avantages de ce format sont nombreux, mais nous importe celui de l'édition dans n'importe
  quel tableur-grapheur, et sa facilité de manipulation. 

* **La structure du tableau doit suivre les indications de la légende suivante.**  
  La première ligne permet d'énumerer le nom de chaque groupe.

  | Nom du groupe 1 | Nom du groupe 2 | Nom du groupe 3 | ... |
  |:---------------:|:---------------:|:---------------:|:---:|

  Ensuite, avec autant de semaine désirées sur l'horizontal, et autant de séance par semaine sur
  la verticale. Ainsi :

  | Semaine 1 | Semaine 2 | Semaine 3 | ... | 
  |:---------:|:---------:|:---------:|:---:|
  |*Matiere 1*|*Matiere 1*|*Matiere 1*|*...*|
  | Colleur   | Colleur   | Colleur   | ... |
  | Jour 0-6  | Jour 0-6  | Jour 0-6  | ... |
  | Salle     | Salle     | Salle     | ... |
  | Horaire   | Horaire   | Horaire   | ... |
  | Remarques | Remarques | Remarques | ... |
  |*Matiere 2*|*Matiere 2*|*Matiere 2*|*...*|
  | ...       | ...       | ...       | ... |

  En cas de doute, prenez exemple sur le fichier fournit dans l'archive.

Notes de version
----------------

### 1.0

* Première version exploitable
* Implemnatation
  * CSV Parser
  * Groupe delta
  * ...

Licence
-------

Bottle Web Framework — MIT License.  
Copyright (c) 2012, Marcel Hellkamp.  

Kholloscope Python — MIT License.  
Copyright (c) 2013, Leo Colombaro.  
