import pygame

class parking():

    def __init__(self, name, xCoord, yCoord, areaRadius, maxCap, morningOCC, noonOCC,eveningOcc,):

        self.name              = name
        self.xCoord            = xCoord
        self.yCoord            = yCoord
        self.maxcap            = maxCap
        self.morningOCC        = morningOCC
        self.eveningOCC        = noonOCC
        self.eveningOCC        = eveningOcc
        self.areaRadius        = areaRadius


    def afflluance_to_rgb(parking):

        if parking.affluance < 33:
            return (0, 255, 0)
        elif parking.affluance < 33 and parking.affluance > 66:
            return (255, 128, 0)
        elif parking.affluance < 66:
            return (255, 0, 0)
