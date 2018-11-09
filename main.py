from radar import *
from medio import *
from blanco import *
from generador import *
import datetime
import math
from detector import *

def main():

    # Time interval for meditions
    tiempo_inicial = datetime.datetime(2016, 3, 5, 1)
    tiempo_final = datetime.datetime(2016, 3, 5, 10)

    # signal generator parameters
    amplitud = 0.2
    fase = 1
    frecuencia = 20 * math.pi

    #Generador
    gen = Generador(amplitud, fase, frecuencia)

    #Detector
    det = Detector()

    #Radar
    rad = Radar(gen, det)

    # target parameters
    amplitud_de_frecuencia_del_blanco = amplitud + 100
    tiempo_inicial_del_blanco = datetime.datetime(2016, 3, 5, 2)
    tiempo_final_del_blanco = datetime.datetime(2016, 3, 5, 4)
    
    #Blanco
    blan = Blanco(amplitud_de_frecuencia_del_blanco, tiempo_inicial_del_blanco, tiempo_final_del_blanco)

    #Medio
    med = Medio([blan])

    #Emite la senal para deteccion
    rad.detectar(med, tiempo_inicial, tiempo_final)

if __name__ == "__main__":
    main()
