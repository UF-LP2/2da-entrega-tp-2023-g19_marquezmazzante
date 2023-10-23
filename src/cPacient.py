from cDisease import cDisease
class cPacient:
    def __init__(self,name,surname,DNI,code,disease,time_arrival):
        self.name: str = name
        self.surname: str = surname
        self.DNI: str = DNI
        self.code: str = code
        self.disease: cDisease = disease
        self.time_arrival: int = time_arrival

    def timepassed(self) -> int:
        time_actual: int
        return (time_actual - self.time_arrival)


