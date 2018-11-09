import datetime

class Blanco(object):

    def __init__(self, amplitud, tiempo_inicial_blanco, tiempo_final_blanco):
        self._amplitud = amplitud
        self._tiempo_inicial_blanco = tiempo_inicial_blanco
        self._tiempo_final_blanco = tiempo_final_blanco

    def reflejar(self, senal, tiempo_inicial, tiempo_final):

        inicio_reflejo = None
        fin_reflejo = None
        senal_respuesta = None

        if self._tiempo_inicial_blanco < tiempo_inicial:
            inicio_reflejo =  tiempo_inicial
        else:
            inicio_reflejo = self._tiempo_inicial_blanco 
        
        if self._tiempo_final_blanco > tiempo_final:
            fin_reflejo =  tiempo_inicial
        else:
            fin_reflejo = self._tiempo_final_blanco

        tiempo_efectivo_reflejo = fin_reflejo - inicio_reflejo

        #la senal reflejada solo se detecta si dura mas de 10 seg
        if tiempo_efectivo_reflejo.total_seconds() > 10:
            senal_respuesta = senal / 2 #self._amplitud
        else:
            senal_respuesta = senal * 0

        return senal_respuesta