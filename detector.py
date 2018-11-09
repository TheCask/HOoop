class Detector(object):

    def __init__(self):
        self._senal_detectada = None

    def detectar(self, senal):

        deteccion = False
        for muestra in senal:
            if int(muestra) is not 0:
                deteccion =  True
                break

        print("Se detecto señal reflejada?:")
        print(deteccion)
        print("La señal detectada es:")
        print(senal)

        return (senal)