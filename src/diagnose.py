import binarytree
from btSymptoms import btsymptoms
from cPacient import cPacient
from cColour import cColour
from eSymptoms import esymptom
from eSymptoms import enumConverter

def search(symp: str, btree: binarytree) -> int:

    if(btree==None):
        return 0
    if(symp==btree.name):
        return btree.value

    aux = search(symp, btree.left)
    if aux==0:
        aux = search(symp, btree.right)
    return aux

def diagnose(pacient: cPacient):
    if pacient.symptoms[0] == esymptom(32) and len(pacient.symptoms) > 1:
        raise Exception("not valid pacient")

    assign = 0
    tree = btsymptoms()
    for i in range(len(pacient.symptoms)):
        if pacient.symptoms[i].value > 32:
            raise Exception("not valid symptom")
        assign = assign + search(enumConverter(pacient.symptoms[i].value), tree)

    if assign >= 90:
        pacient.colour = 1
    elif assign < 90 and assign >= 70:
        pacient.colour = 2
    elif assign < 70 and assign >= 50:
        pacient.colour = 3
    elif assign < 50 and assign >= 30:
        pacient.colour = 4
    elif assign < 30 and assign >= 10:
        pacient.colour = 5
    return pacient.colour



if __name__ == "__main__":

    verde = cColour(2)
    sintomitas: list[esymptom] = [esymptom(21),esymptom(22)]
    paciente = cPacient("alma", "marquez", 45296117, 1234, sintomitas)
    print(diagnose(paciente))
