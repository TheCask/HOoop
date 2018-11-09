import matplotlib.pyplot as pp
import numpy as np

class Radar(object):


    def __init__(self, generador, detector):
        self.generador = generador
        self.detector = detector

    def detectar(self, medio, tiempo_inicial, tiempo_final):

        una_senal = self.generador.generar(tiempo_inicial, tiempo_final)
        print("Señal generada:")
        print(una_senal)
        
        una_senal_reflejada = medio.reflejar(una_senal, tiempo_inicial, tiempo_final)
        print("Señal reflejada sin detectar:")
        print(una_senal_reflejada)
        
         #se crea y configura la figura para graficar los datos
        pp.figure(figsize=(12, 6))
        pp.ylabel('Señal', fontsize = 16)
        pp.xlabel('Tiempo', fontsize = 16)
        
        x = np.arange(len(una_senal))
        pp.scatter(x,una_senal,c='R', label = 'Generada')
        pp.scatter(x,una_senal_reflejada,c='B', label = 'Reflejada')
        pp.legend(loc='upper left')
        pp.show()

        return self.detector.detectar(una_senal_reflejada)

    #TODO agregar el metodo plotear_senal
