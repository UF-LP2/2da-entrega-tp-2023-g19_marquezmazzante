from cDisease import cDisease
from datetime import datetime
class cPacient:
    def __init__(self,name,surname,DNI,code,disease,time_arrival):
        self.name: str = name
        self.surname: str = surname
        self.DNI: str = DNI
        self.code: str = code
        self.disease: datetime = disease
        self.time_arrival: int = time_arrival

    def timepassed(self) -> int:                                ## me devuelve la cant de minutos que lleva el paciente esperando
        time_actual = datetime.now()
        timepassed: datetime = time_actual - self.time_arrival
        minpassed: int = timepassed.total_seconds()/60
        return minpassed

    def timeremaining(self) -> int:                             ## devuelve el tiempo que le queda al paciente
        minpassed: int = self.timepassed()
        return (self.disease.max_time - minpassed)
