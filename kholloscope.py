#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Kholloscope
    ~~~~~~~~~~~
    Petit framework pour grand kholloscope. Publier facilement,
    en Python, le kholloscope d'une classe préparatoire.

    https://github.com/LeoColomb/kholloscope
    Copyright (c) 2013, Léo Colombaro

    @version 0.0.1
    @copyright (c) 2013 Léo Colombaro
    @license MIT LICENSE
    @package Python 3
    @modules bottle, datetime, csv
"""
from bottle import route, run, view, static_file, debug, abort, error, request
import datetime
import csv

"""    Configuration    """

_route = '/<classe:re:[a-z]+>'
_port = 1357
_debug = True


"""    Données    """

def get_kholles(classe):
    """ Analyser le fichier-tableau et le convertir en
        données Python

        @param classe Nom de la classe = Nom du fichier
        @return khl Liste de colles
    """
    try:
        datafile = open('data/' + classe + '.csv')
    except OSError:
        abort(404)
    data = csv.reader(datafile, delimiter=';')
    khl = list(tuple(row) for row in data)
    datafile.close()
    return khl

"""    Publication    """

@route(_route)
@view('kholles')
def kholle(classe):
    group = request.get_cookie("group")
    return dict(name=classe.upper(), kholles=get_kholles(classe))

@route('/assets/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='assets')

@error(404)
@view('base')
def error404(error):
    return dict(title='Erreur · 404', base='<div class="page-header"><h1>404<h1><p class="lead">Vous me posez une colle : je ne connais pas cette page…</p></div>')

if _debug:
    debug(True)
    run(host='localhost', port=_port, reloader=True)
else:
    run(host='localhost', port=_port)
