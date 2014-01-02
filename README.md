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
[solutions faciles et gratuites](http://wiki.python.org/moin/FreeHosts).

Ensuite par étapes :

1. Décompresser l'[archive du projet](https://github.com/LeoColomb/kholloscope/archive/master.zip) 
dans un répertoire du serveur, de préférence à la racine.
2. Vérifier la [configuration](#configuration) et l'ajuster pour corresponde aux besoins d'exploitation.
3. Ajouter le [fichier du tableau de colles](#initialisation) dans le dossier `data`.
4. C'est fini !

Configuration
-------------

Dans le fichier `config.py`, il est possible de paramétrer les valeurs suivantes :

### `__zone`
Zone du département pour la répartition des vacances scolaires. `a` `b`, ou `c`.  
_Par défaut, `__zone = 'c'`._

### `__debug`
Permet de passer en mode débogage, et obtenir davantage de détails lors d'une erreur.  
Particulièrement utile lors de problèmes à répétition. N'hésitez pas alors à ouvrir un 
[ticket](https://github.com/LeoColomb/kholloscope/issues/new) !  
_Par défaut, `__debug = False`._

### `__domain`
Préciser le domaine du serveur où est localisé l'application.
Par exemple : Kholloscope de MPSI accessible à `http://example.com/un/deux/trois/mpsi`,
alors `__domain = 'example.com/un/deux/trois'`.  

### `__port`
Au cas où l'accès HTTP au serveur se fait par un port diffèrent de `80`.  
_Par défaut, `__port = 80`, et aucun changement n'est nécessaire._

### `__route`
Défini comment le nom de la classe doit être analysé à partir l'URI.  
_Par défaut, `__route = '/<classe:re:[a-zA-Z0-9_-]+>'`._

### `__ordre`
Défini l'ordre montant/descendant pour la succession des groupes au fil 
des semaines. Exemple sur deux semaines successives :  
#### `+`
| Groupe 1  | Groupe 2  | Groupe 3  | ... | Groupe 15 |
|:---------:|:---------:|:---------:|:---:|:---------:|
| Groupe 15 | Groupe 1  | Groupe 2  | ... | Groupe 14 |
#### `-`
| Groupe 1  | Groupe 2  | Groupe 3  | ... | Groupe 15 |
|:---------:|:---------:|:---------:|:---:|:---------:|
| Groupe 2  | Groupe 3  | Groupe 4  | ... | Groupe 1  |
_Par défaut, `__ordre = '+'`._

### `__decal`
Nombre de semaines qui séparent celle de la rentrée scolaire à celle 
du début des colles.  
_Par défaut, `__decal = 0`._

### `__server`
Défini l'architecture du serveur et par extension le type d'exécution du script.  
Se référer aux explications du [guide Bottle](http://bottlepy.org/docs/dev/deployment.html#switching-the-server-backend).  
_Par défaut, `__server = 'wsgiref'`._

Initialisation
--------------

Dans le dossier `data` sont sauvegardé les différents kholloscopes de chaque
classe. Pour cela, quelques indications :

* **Le nom du fichier est le nom de la classe en question.**  
  Il définira l'URI spécifique à cette classe, telle que [`__route`](#_route) l'indique.  
  Par exemple, le fichier s'appelle `mpsi.csv`, alors on y accède *via* `http://example.com/mpsi`.  
  Noter l'absence d'extension.

* **Le fichier doit être au format [CSV](http://fr.wikipedia.org/wiki/Comma-separated_values).**  
  Les avantages de ce format sont nombreux, mais on retiendra l'édition dans n'importe
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

  Les jours de la semaine sont numérotés de 0 à 6 (Lundi à Dimanche).  
  En cas de doute, prendre exemple sur le fichier fournit dans l'archive.

Notes de version
----------------

### 1.0
_Première version exploitable_

* CSV Parser
* Mise en Python du tableau
* Affichage mobile
* Groupe + Vacs delta
* Multi-classes
* ...

Licence
-------

Bottle Web Framework — MIT License.  
Copyright (c) 2012, Marcel Hellkamp.  

Kholloscope Python — MIT License.  
Copyright (c) 2013, Leo Colombaro.  
