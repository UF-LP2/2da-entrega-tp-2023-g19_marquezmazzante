from library.cColour import cColour
from datetime import datetime
from datetime import timedelta
from library.eSymptoms import esymptom

class cPacient:
    def __init__(self,name,surname,DNI,code,symptoms = None,colour = None):
        self.name: str = name
        self.surname: str = surname
        self.DNI: str = DNI
        self.code: str = code
        if symptoms is None:
            self.symptoms: list[esymptom] = [esymptom(32)]
        else:
            self.symptoms: list[esymptom] = symptoms
        if colour is None:
            self.colour = cColour(1)
        else:
            self.colour: cColour = colour

        if (self.colour.value == 5):
            self.max_time = 0
        elif(self.colour.value == 4):
            self.max_time = 10
        elif(self.colour.value == 3):
            self.max_time = 60
        elif(self.colour.value == 2):
            self.max_time = 120
        elif(self.colour.value == 1):
            self.max_time = 240
        self.time_arrival: datetime = datetime.now()


    def timepassed(self) -> timedelta:                                ## me devuelve la cant de minutos que lleva el paciente esperando
        time_actual = datetime.now()
        timepassed: datetime = time_actual - self.time_arrival
        return timepassed

    def timeremaining(self) -> int:                             ## devuelve el tiempo que le queda al paciente
        minpassed: int = self.timepassed().seconds * 5
        return (self.max_time - minpassed)
