import pygame
import csv
from pygame.draw import line
from parking import *

#prend un fichier csv en entrée et retourne une liste de parkings

def decrypt(filename):
    parking_list = []
    parking_hours = []
    with open(filename) as file:
        
        reader  = csv.reader(file, delimiter=',')
        line_count = 0
        for row in reader:
            #print(row)
            #print(line_count)
            if line_count == 0:
                line_count += 1
            else:
                
                line_count +=1
                parking_hours.append(parking(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]))) 
                #print(len(parking_hours))
                if len(parking_hours) == 12:
                    parking_list.append(parking_hours)
                    

    return parking_list


decrypt("parking_gen.csv")

        
