import pygame
import csv
from parking import *


def decrypt(filename):
    parking_list = []
    with open(filename) as file:
        reader  = csv.reader(file, delimiter=',')
        line_count = 0

        for row in reader:
            if line_count != 0:
                parking_list.append(parking(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) ) 
                line_count += 1

    return parking_list
        
