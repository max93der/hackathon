import pygame
import csv
from parking import *

#prend un fichier csv en entrée et retourne une liste de parkings

def decrypt(filename):
    parking_list = []
    parking_sublist = []
    with open(filename) as file:
        reader  = csv.reader(file, delimiter=',')
        line_count = 0

        for row in reader:
            if line_count == 0:
                #print(f'les colones sont : {",".join(row)}')
                line_count += 1
            else:
                parking_list.append(parking(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]))) 
                #print(f'les colones sont : {",".join(row)}')
                line_count += 1
    
    

    return parking_list



    


        
