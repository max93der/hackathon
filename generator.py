import csv
import random as rd
from parking import *


# ------------------------------------ DATA ------------------------------------
# name          = nom du parking
# xCoord        = coordonnées en x (en pixel dans un premier temps)
# yCoord        = coordonnées en y (pareil)
# areaRadius    = rayon du cercle qui représente le territoire du parking
# maxCap        = capacité maximum du parking (dénominateur du ratio d'affluence)
# morningOcc    = taux d'affluence au matin (numérateur du ratio d'affluence)
# noonOcc       = taux d'affluence à midi (numérateur du ratio d'affluence)
# eveningOcc    = taux d'affluence au soir (numérateur du ratio d'affluence)

def generate_file(x1, y1, x2, y2, x3, y3, x4,y4, x5, y5, x6, y6, x7, y7, x8, y8):
    header = ["name","xCoord","yCoord","areaRadius","maxCap", "Occupation"]
    radius = 35
    data = [
        ['Parking_A', x1, y1,radius , 200 , rd.randint(1, 200)],
        ['Parking_B', x2, y2, radius, 200 , rd.randint(1, 200)],
        ['Parking_C', x3, y3, radius, 200 , rd.randint(1, 200)],
        ['Parking_D', x4, y4, radius, 50  , rd.randint(1, 50)],
        ['Parking_B28', x5, y5, radius, 80, rd.randint(1, 80)],
        ['Parking_Trifacultaire', x6, y6, radius, 120, rd.randint(1, 120)],
        ['Parking_B52', x7, y7, radius, 70 , rd.randint(1, 70)],
        ['Parking_B37', x8, y8, radius, 30 ,rd.randint(1, 30)]
    ]

    
    # ------------------------------------ WRITING ---------------------------------
    with open('parking_gen.csv', 'w', encoding='UTF8', newline='') as file:
       
        writer =  csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)


generate_file(790, 175,900, 165, 960, 145, 1045, 90, 420, 220, 1125, 185, 300, 160, 400, 155)




