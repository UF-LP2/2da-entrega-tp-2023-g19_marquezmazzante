import binarytree
from library.btSymptoms import btsymptoms
from library.cPacient import cPacient
from library.eSymptoms import esymptom
from library.eSymptoms import enumConverter

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
        pacient.colour = 5
    elif assign < 90 and assign >= 70:
        pacient.colour = 4
    elif assign < 70 and assign >= 50:
        pacient.colour = 3
    elif assign < 50 and assign >= 30:
        pacient.colour = 2
    else:
        pacient.colour = 1
    return pacient.colour

