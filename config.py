#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Kholloscope
    ~~~~~~~~~~~
    Petit framework pour grand kholloscope. Publier facilement,
    en Python, le kholloscope d'une classe préparatoire.
    
    Fichier de configuration.
"""
from datetime import date, datetime

__first = date(datetime.now().year, 9, 1)
__debug = True
__path = ""
__port = 1357
__route = '/<classe:re:[a-zA-Z0-9_-]+>'
