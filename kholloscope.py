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
    @modules bottle, datetime
"""
from bottle import route, run, template, static_file, response, debug
import datetime

"""    Configuration    """

_route = '/<classe>'
_port = 1357
_debug = True


"""    Données    """
def get_kholles():
    return

"""    Publication    """

@route(_route)
def kholle(classe):
    response.set_header('Content-Language', 'fr')
    return template('layout', name=classe.upper(), kholles=get_kholles())

@route('/assets/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='assets')

if _debug:
    debug(True)
    run(host='localhost', port=_port, reloader=True)
else:
    run(host='localhost', port=_port)
