# -*- coding: utf-8 -*-

import json

with open('dane_bazy.json', 'r') as myfile:
    data_json = myfile.read()

parsed = json.loads(data_json)

name = parsed['login']
intro = parsed['password']
print(name)
print(intro)


