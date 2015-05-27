# -*- coding:utf-8 -*-
from django.conf import settings
import os
import random


with open(os.path.join(settings.BASE_DIR, 'data', 'pokemons.txt'), encoding='utf-8') as fi:
    _pokemon_list = fi.read().split('\n')[:-1]


def word_challenge():
    ret = ''.join(random.choice(_pokemon_list).split()[1:])
    return ret, ret
