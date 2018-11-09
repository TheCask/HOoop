import numpy as np
import math

class Generador(object):

    def __init__(self, amplitud, fase, frecuencia):
        self._amplitud = amplitud
        self._fase = fase
        self._frecuencia = frecuencia
        #  muestras por segundo
        self._frecuencia_muestreo = frecuencia*3


    def generar(self, tiempo_inicial, tiempo_final):

        cantidad_muestras = (tiempo_final - tiempo_inicial).seconds / self._frecuencia_muestreo

        muestras = range(int(cantidad_muestras))
        
        #ruido blanco para agregar a la senal
        whiteNoise = np.random.normal(size=len(muestras))
        
        ret = [self._amplitud*math.sin(2*(1/self._frecuencia)*i+self._fase) for i in muestras]

        #se retorna la senal mas el ruido blanco
        return ret + whiteNoise * 0.01
