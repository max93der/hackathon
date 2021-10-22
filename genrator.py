import csv
from parking import *


# ------------------------------------------------------------------------------
#
header = ["name","xCoord","yCoord","maxCap","morningOcc","noonOcc","eveningOcc"]

with open('parking_gen.csv', 'w', encoding='UTF8', newline='') as file:

    writer =  csv.writer(file)  
