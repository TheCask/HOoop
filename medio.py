import numpy as np

class Medio(object):

    def __init__(self, blancos):
        self.blancos = blancos

    def reflejar(self, una_senal, tiempo_inicial, tiempo_final):
        
        if len(self.blancos) > 0:
            for blanco in self.blancos:
                senal_reflejada =+ blanco.reflejar(una_senal, tiempo_inicial, tiempo_final)
        return senal_reflejada