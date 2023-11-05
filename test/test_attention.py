from library.cPacient import cPacient
from library.cColour import cColour
from src.eSymptoms import esymptom
from library.attention import attend
from datetime import datetime
from datetime import timedelta

def test_attention1():
    assert cColour(1).value == 1
    symptoms: list[esymptom] = [esymptom(12),esymptom(7)]
    pacient1 = cPacient("alma", "marquez", 45296117, 1234, symptoms, cColour(3))
    pacient2 = cPacient("lorenzo", "mazzante", 45296117, 1235, symptoms, cColour(1))
    pacient3 = cPacient("juan", "perez", 45296117, 1236, symptoms, cColour(1))
    pacientsims = cPacient("npc", "npc", 435534344, 43243)
    listapac = [pacient1, pacient2, pacient3, pacientsims]
    assert pacient1 == pacient1
    assert attend(listapac,0,len(listapac))==pacient1


def test_attention2():
    symptoms: list[esymptom] = [esymptom(12),esymptom(7)]
    pacient1 = cPacient("alma", "marquez", 45296117, 1234, symptoms, cColour(1))
    listapac = [pacient1]
    assert listapac[0] == pacient1

def test_attention3():
    symp: list[esymptom]= [esymptom(21), esymptom(4), esymptom(5)]
    pacient1=cPacient("leo", "messi", 13131313, 1333, symp, cColour(2))
    pacient2=cPacient("lorenzo", "mazzante", 452874999, 1234, symp, cColour(4))
    pacient3=cPacient("alma","marquez",45296117,236,symp, cColour(3))

    listapac=[pacient1,pacient2,pacient3]
    assert attend(listapac, 0, len(listapac))==pacient2

def test_attention4():
    symp: list[esymptom]=[esymptom(12), esymptom(8), esymptom(9)]
    p1=cPacient("leo", "messi", 1313131, 13, symp, cColour(4))
    p1.time_arrival=datetime.now()
    p2=cPacient("alma", "marquez", 45296117, 4545, symp, cColour(4))
    p2.time_arrival=datetime.now()+timedelta(minutes=30)
    p3=cPacient("lorenzo", "mazzante", 48965478, 4555, symp, cColour(4))
    p3.time_arrival=datetime.now()+timedelta(hours=1)

    listpacientes: list[cPacient]=[p1, p2, p3]

    assert attend(listpacientes, 0, len(listpacientes))==p1

