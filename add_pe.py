import json
import os

folder = '2023-01-31-12-34-56'
file = '2022-2023 Spring 2023 Term.json'
folder2 = folder + '_pe'
os.mkdir(f'logs/{folder2}')

a = json.load(open(f'logs/{folder}/{file}', 'r'))
b = json.load(open('assets/pe.json', 'r'))

c = b + a

print(len(a), len(b), len(c))

json.dump(c, open(f'logs/{folder2}/{file}', 'w+'))
