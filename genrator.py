import csv
from parking import *

with open('parking_gen.csv', 'w', encoding='UTF8', newline='') as file:
     
    writer =  csv.writer(file) 