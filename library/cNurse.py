from library.cPacient import cPacient
from src.eSymptoms import esymptom
from src.btSymptoms import btsymptoms
from src.diagnose import search
from src.eSymptoms import enumConverter

class cNurse:
    def __init__(self,name,surname,DNI,licence):
        self.name: str = name
        self.surname: str = surname
        self.DNI: str = DNI
        self.licence: str = licence

    def diagnose(self, pacient: cPacient):
        if esymptom(32) in pacient.symptoms and len(pacient.symptoms) > 1:
            raise Exception("not valid pacient")

        assign = 0
        tree = btsymptoms()
        for i in range(len(pacient.symptoms)):
            if pacient.symptoms[i].value > 32:
                raise Exception("not valid symptom")
            assign = assign + search(enumConverter(pacient.symptoms[i].value), tree)

        if assign >= 90:
            pacient.colour = 5
            pacient.max_time = 0
        elif assign < 90 and assign >= 70:
            pacient.colour = 4
            pacient.max_time = 10
        elif assign < 70 and assign >= 50:
            pacient.colour = 3
            pacient.max_time = 60
        elif assign < 50 and assign >= 30:
            pacient.colour = 2
            pacient.max_time = 120
        else:
            pacient.colour = 1
            pacient.max_time = 240
        return pacient.colour
