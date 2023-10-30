import random
from pprint import pprint

sorteios = ['sorteio1', 'sorteio2', 'sorteio3']
participantes = ['joel', 'maria', 'jessica', 'moises', 'abel', 'josé', 'fernando']

pprint({sorteio: random.choice(participantes) for sorteio in sorteios})