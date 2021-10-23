import pygame
import csv

from pygame.draw import line
from parking import *

#prend un fichier csv en entrée et retourne une liste de parkings

def decrypt(filename):
    parking_list = []
    parking_days = []
    parking_hours = []
    with open(filename) as file:
        
        reader  = csv.reader(file, delimiter=',')
        line_count = 0
        row_count  = 0
        hours_count = 0
        days_count = 0
        for row in reader:
            #print(row)
            #print(line_count)
            if line_count == 0:
                line_count += 1
            else:
                
                line_count +=1
                parking_hours.append(parking(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]))) 
                #print(len(parking_hours))
                if len(parking_hours) == 8:
                    parking_days.append(parking_hours)
                    #len(print(parking_days))
                    print("yep")
                if len(parking_days) == 12:
                    parking_list.append(parking_days)
                    #print("yop")
                    #parking_days.clear()
                if len(parking_list)==7:
                    print("yoooo")



    return parking_list


decrypt("parking_gen.csv")

"""
                parking_hours.append(parking(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]))) 
                #print(f'les colones sont : {",".join(row)}')
                hours_count +=1 
                if hours_count ==  11:
                    hours_count = 0
                    days_count += 1
                    parking_days.append(parking_hours)
                    parking_hours.clear
                if days_count == 6:
                    days_count = 0
                    #counter += 1 
                    #print(counter)
                    parking_list.append(parking_days)
                    parking_days.clear"""
    


        
