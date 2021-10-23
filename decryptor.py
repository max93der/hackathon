import pygame
import csv
from parking import *

#prend un fichier csv en entrée et retourne une liste de parkings

def decrypt(filename):
    parking_list = []
    parking_days = []
    parking_hours = []
    with open(filename) as file:
        reader  = csv.reader(file, delimiter=',')
        line_count = 0
        hours_count = 0
        for row in reader:
            if line_count == 0:
                #print(f'les colones sont : {",".join(row)}')
                line_count += 1
            else:
                
                parking_hours.append(parking(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]))) 
                #print(f'les colones sont : {",".join(row)}')
                line_count += 1
                if line_count %8 == 0:
                    parking_days.append(parking_hours)
                    parking_hours.clear
                    if hours_count % 12 == 0:
                        parking_list.append(parking_days)
                        parking_days.clear


    return parking_list

print(decrypt("parking_gen.csv")[0][0][0].name)



    


        
