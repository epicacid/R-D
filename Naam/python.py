import json
from pprint import pprint

with open('leerlingen.json') as leerlingen_file:    
    leerlingen = json.load(leerlingen_file)

pprint(leerlingen)