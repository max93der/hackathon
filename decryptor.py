import pygame
import csv
from parking import *


def decrypt(filename):
    parking_list = []
    with open(filename) as file:
        reader  = csv.reader(file, delimiter=',')
        line_count = 0

        for row in reader:
            if line_count == 0:
                #print(f'les colones sont : {",".join(row)}')
                line_count += 1
            else:
                parking_list.append(parking(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]),  int(row[7]) )) 
                #print(f'les colones sont : {",".join(row)}')
                line_count += 1
    
    

    return parking_list


# if you wanna test  test just uncomment

for objects in decrypt("parking_gen.csv"):
    print(objects.areaRadius)
    


        
