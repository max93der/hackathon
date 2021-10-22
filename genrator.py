import csv
from parking import *


header = ["name","xLocation","yLocation", "affluance", "total_capacity", "current_capacity","electiral_spaces",]
with open('parking_gen.csv', 'w', encoding='UTF8', newline='') as file:
     
    writer =  csv.writer(file) 

    writer.writerow(header)















