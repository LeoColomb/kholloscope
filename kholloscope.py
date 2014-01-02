#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kholloscope
~~~~~~~~~~~
Petit framework pour grand kholloscope. Publier facilement,
en Python, le kholloscope d'une classe préparatoire.

https://github.com/LeoColomb/kholloscope
Copyright (c) 2013, Léo Colombaro

:version: 0.0.9
:copyright: (c) 2013 Léo Colombaro
:license: MIT LICENSE
:package: Python 2.7+
:modules: bottle, datetime, csv
"""

__name__ = 'Kholloscope'
__description__ = "Petit framework pour grand kholloscope."
__version__ = '0.1.0'
__author__ = "Léo Colombaro"
__license__ = 'MIT'

from bottle import (
    route, run,
    view, static_file,
    debug, abort,
    error, request,
    response )
from datetime import datetime
from math import ceil
import csv
import config

############
### Données
############
data = {'color': ['success', 'info', 'warning', 'danger', 'default'],
        'cells': ['Colleur', 'Jour', 'Salle', 'Horaire'],
        'days': ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
        }

def get_kholles(cls):
    """Analyser le fichier-tableau et le convertir
    en données Python

    :param cls: Nom de la classe = Nom du fichier
    :return khl: Liste de colles
    """
    try:
        datafile = open('data/' + cls + '.csv')
    except OSError:
        abort(404, text='Fichier inexistant')
    data = csv.reader(datafile, delimiter=';')
    khl = list(tuple(row) for row in data)
    datafile.close()
    return khl

def get_rank(grp, max):
    """Calcule la semaine correspondante pour un groupe
    de colle donné.

    :param grp: Groupe de colle
    :param max: Nombre de groupe dans la classe
    :return rnk: Rang actuel du groupe
    """
    if not grp:
        return -1
    vacfile = open('data/zone_c.csv')
    data = csv.reader(vacfile, delimiter=';')
    vacs = list(tuple(row) for row in data)
    vacfile.close()
    now = (datetime.now() + timedelta(2)).isocalendar()[1]
    # Début de semaine le samedi
    delt = config.__decal
    if now < 32:
        now += 52
    for vac in vacs[1:]:
        if int(vac[1]) <= now:
            # Vacances passées, décompte des semaines non "ouvrées"
            delt += (int(vac[1]) - int(vac[0]))
        elif int(vac[0]) <= now < int(vac[1]):
            # En vacances, arrêt de la progression dans le kholloscope
            delt += now - int(vac[0])
            break
    # Ordre * ( Maintenant - Delta des vacances - Début de l'année
    # + Décalage groupe ) % Modulo max groupe
    return (int(config.__ordre + '1') * (now - delt - int(vacs[0][1]) - int(grp)) % max,
        now - delt - int(vacs[0][1])
        )

################
### Publication
################
@route(config.__route)
@view('kholles')
def kholle(classe):
    group = request.query.grp
    if group:
        response.set_cookie(classe + "_grp", group, None, max_age=3600 * 24 * 30)
    else:
        group = request.get_cookie(classe + "_grp")
    kholles = get_kholles(classe)
    rangs=get_rank(group, len(kholles[0]))
    data['max'] = ceil((len(kholles) - 2.) / 6.)
    return dict(name=classe.upper(),
                kholles=kholles,
                group=group,
                rang=rangs[0],
                sem=rangs[1],
                data=data)

@route('/assets/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='assets')

@error(404)
@view('base')
def error404(error):
    return dict(title='Erreur · 404',
                head={'tle': '404', 'dsc': 'Vous me posez une colle : je ne connais pas cette page…'},
                base='<small class="text-muted">' + str(error) + '<small>')

debug(config.__debug)
run(server=config.__server, host=config.__domain, port=config.__port, reloader=config.__debug)
