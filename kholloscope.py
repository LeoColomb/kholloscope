#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Kholloscope
    ~~~~~~~~~~~
    Petit framework pour grand kholloscope. Publier facilement,
    en Python, le kholloscope d'une classe préparatoire.

    https://github.com/LeoColomb/kholloscope
    Copyright (c) 2013, Léo Colombaro

    @version 0.0.3
    @copyright (c) 2013 Léo Colombaro
    @license MIT LICENSE
    @package Python 3
    @modules bottle, datetime, csv
"""
from bottle import route, run, view, static_file, debug, abort, error, request, response
from datetime import date, datetime
import csv

"""    Configuration    """

_annee = date(datetime.now().year, 9, 1)
_debug = True
_path  = ""
_port  = 1357
_route = '/<classe:re:[a-zA-Z]+>'


"""    Données    """

def get_kholles(cls):
    """ Analyser le fichier-tableau et le convertir en
        données Python

        @param cls Nom de la classe = Nom du fichier
        @return khl Liste de colles
    """
    try:
        datafile = open('data/' + cls + '.csv')
    except OSError:
        abort(404, text='Fichier inexistant')
    data = csv.reader(datafile, delimiter=';')
    khl = list(tuple(row) for row in data)
    datafile.close()
    return khl

def get_rank(grp):
    """ Calcule la semaine correspondante pour un groupe
        de colle donné.

        @param grp Groupe de colle
        @return rnk Rang actuel du groupe
    """
    if not grp:
        return
    return 2

"""    Publication    """

@route(_route)
@view('kholles')
def kholle(classe):
    group = request.query.grp
    if group:
        response.set_cookie(classe+"_grp", group)
    else:
        group = request.get_cookie(classe+"_grp")
    return dict(name=classe.upper(),
                kholles=get_kholles(classe),
                group=group,
                rang=get_rank(group))

@route('/assets/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='assets')

@error(404)
@view('base')
def error404(error):
    return dict(title='Erreur · 404',
                head=dict(tle='404', dsc='Vous me posez une colle : je ne connais pas cette page…'),
                base='<small class="text-muted">' + str(error) + '<small>')

debug(_debug)
run(host='localhost', port=_port, reloader=_debug)
