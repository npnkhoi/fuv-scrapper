import json
import os
import sys

folder = sys.argv[1]
file = '2022-2023 Spring 2023 Term.json'
folder2 = folder + '_pe'
# os.mkdir(f'logs/{folder2}')

a = json.load(open(f'logs/{folder}/{file}', 'r'))
b = json.load(open('assets/pe.json', 'r'))

c = a + b

print(len(a), len(b), len(c))

json.dump(c, open(f'logs/{folder2}/{file}', 'w+'))
