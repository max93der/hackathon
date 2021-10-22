import pygame
from pygame import draw
class parking():

    def __init__(self, location_tp,total_spaces, available_spaces, electrical_spaces, is_covered, price_hour, ):


        self.total_spaces      = total_spaces
        self.location_tp       = location_tp
        self.available_spaces  = available_spaces
        self.electrical_spaces = electrical_spaces
        self.is_covered        = is_covered
        self.price_hour        = price_hour
