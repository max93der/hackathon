import pygame

class parking():

    # ------------------------------------ DATA ------------------------------------
    # name          = nom du parking
    # xCoord        = coordonnées en x (en pixel dans un premier temps)
    # yCoord        = coordonnées en y (pareil)
    # areaRadius    = rayon du cercle qui représente le territoire du parking
    # maxCap        = capacité maximum du parking (dénominateur du ratio d'affluence)
    # morningOcc    = taux d'affluence au matin (numérateur du ratio d'affluence)
    # noonOcc       = taux d'affluence à midi (numérateur du ratio d'affluence)
    # eveningOcc    = taux d'affluence au soir (numérateur du ratio d'affluence)

    def __init__(self, name, xCoord, yCoord, areaRadius, maxCap, morningOCC, noonOCC, eveningOCC):
        self.name              = name
        self.xCoord            = xCoord
        self.yCoord            = yCoord
        self.areaRadius        = areaRadius
        self.maxcap            = maxCap
        self.morningOCC        = morningOCC
        self.eveningOCC        = noonOCC
        self.eveningOCC        = eveningOCC
