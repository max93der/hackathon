import csv
from parking import *


# ------------------------------------------------------------------------------
# name          = nom du parking
# xCoord        = coordonnées en x (en pixel dans un premier temps)
# yCoord        = coordonnées en y (pareil)
# maxCap        = capacité maximum du parking (dénominateur du ratio d'affluence)
# morningOcc    = taux d'affluence au matin (numérateur du ratio d'affluence)
# noonOcc       = taux d'affluence à midi (numérateur du ratio d'affluence)
# eveningOcc    = taux d'affluence au soir (numérateur du ratio d'affluence)

header = ["name","xCoord","yCoord","maxCap","morningOcc","noonOcc","eveningOcc"]

data = [
    ['Parking_A', 28748, 'AL', 'ALB'],
    ['Parking_B', 2381741, 'DZ', 'DZA'],
    ['Parking_C', 199, 'AS', 'ASM'],
    ['Parking_D', 468, 'AD', 'AND'],
    ['Parking_B28', 1246700, 'AO', 'AGO'],
    ['Parking_Trifacultaire', 1246700, 'AO', 'AGO'],
    ['Parking_B52', 1246700, 'AO', 'AGO'],
    ['Parking_B37', 1246700, 'AO', 'AGO']
]

with open('parking_gen.csv', 'w', encoding='UTF8', newline='') as file:
     
    writer =  csv.writer(file) 

    writer.writerow(header)















