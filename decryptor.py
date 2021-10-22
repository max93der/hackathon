import pygame
import csv
from parking import *


def decrypt(filename):

    with open(filename) as file:
        reader  = csv.reader(file, delimiter=',')
        line_count = 0

        for row in reader:
            if line_count != 0:
                
                
        
