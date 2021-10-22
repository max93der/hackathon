import pygame

class parking():

    def __init__(self, location_tp, affluance,  electrical_spaces, is_covered, price_hour, ):


        self.location_tp       = location_tp
        self.electrical_spaces = electrical_spaces
        self.is_covered        = is_covered
        self.price_hour        = price_hour
        self.affluance         =  affluance


    def afflluance_to_rgb(parking):

        if parking.affluance < 33:
            return (0, 255, 0)
        elif parking.affluance < 33 and parking.affluance > 66:
            return (255, 128, 0)
        elif parking.affluance < 66:
            return (255, 0, 0)
