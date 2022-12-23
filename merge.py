import json
import os

HOMEDIR = os.getenv('HOME')
OUTFILE = f'{HOMEDIR}/.config/karabiner/assets/complex_modifications/all.json'

title = 'Custom Config'
rules = []

files = os.listdir('.')
for file in files:
    if '.json' in file:
        f = open(file)
        j = json.load(f)
        rules += j['rules']

outfile = open(OUTFILE, 'w+')
json.dump({'title': title, 'rules': rules}, outfile)
outfile.close()
