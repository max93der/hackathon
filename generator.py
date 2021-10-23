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

def generate_file():
    header = ["name","xCoord","yCoord","areaRadius","maxCap","morningOcc","noonOcc","eveningOcc"]

    data = [
        ['Parking_A', 790, 175, 50, 200, rd.randint(0, 200), rd.randint(0, 200), rd.randint(0, 200)],
        ['Parking_B', 900, 165, 50, 200, rd.randint(0, 200), rd.randint(0, 200), rd.randint(0, 200)],
        ['Parking_C', 960, 145, 50, 200, rd.randint(0, 200), rd.randint(0, 200), rd.randint(0, 200)],
        ['Parking_D', 1045, 90, 50, 50, rd.randint(0, 50), rd.randint(0, 50), rd.randint(0, 50)],
        ['Parking_B28', 420, 220, 50, 80, rd.randint(0, 80), rd.randint(0, 80), rd.randint(0, 80)],
        ['Parking_Trifacultaire', 1125, 185, 50, 120, rd.randint(0, 120), rd.randint(0, 120), rd.randint(0, 120)],
        ['Parking_B52', 300, 160, 50, 70, rd.randint(0, 70), rd.randint(0, 70), rd.randint(0, 70)],
        ['Parking_B37', 400, 155, 50, 30, rd.randint(0, 30), rd.randint(0, 30), rd.randint(0, 30)]
    ]

    # ------------------------------------ WRITING ---------------------------------
    with open('parking_gen.csv', 'w', encoding='UTF8', newline='') as file:

        writer =  csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)
