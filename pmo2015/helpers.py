import os
import random

from django.conf import settings

with open(os.path.join(settings.DATA_DIR, 'pokemons.txt'), encoding='utf-8') as fi:
    _pokemon_list = fi.read().split('\n')[:-1]


def word_challenge():
    ret = ''.join(random.choice(_pokemon_list).split()[1:]).replace('-', '')
    return ret, ret
