import json
import os
import sys

folder = sys.argv[1]
file = '2022-2023 Spring 2023 Term.json'

a = json.load(open(f'logs/{folder}/{file}', 'r'))
b = json.load(open('assets/pe.json', 'r'))
c = json.load(open('assets/sport.json', 'r'))

res = a + b + c


json.dump(res, open(f'logs/{folder}/{file}', 'w+'))
json.dump(a, open(f'logs/{folder}/{file[:-5]}_backup.json', 'w+'))
