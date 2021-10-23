import random
class cityparking:

    def __init__(self, xCoord, y_Coord, AvSpaces, name, logo):
        
        self.xCoord = xCoord
        self.yCoord = y_Coord
        self.AvSpaces = AvSpaces
        self.name = name
        self.logo = logo

    def generate_parkings(coord_list, amount):
        parking_list = []

        for i in range(0, amount):
            parking_list.append(cityparking(coord_list[i][0], coord_list[i][1], random.randint(0, 5)))
        
        return parking_list
    

    

        
