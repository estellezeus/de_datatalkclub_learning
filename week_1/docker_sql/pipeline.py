import sys

import pandas as pd

print(sys.argv)

# Récupérer l'argument passé en paramètre lors de l'exécution; 0 récupère le nom du fichier
day = sys.argv[1]

print(f'Success for day = {day}!!')