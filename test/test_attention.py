import pytest

from library.cPacient import cPacient,InvalidPacient
from library.cColour import cColour
from src.eSymptoms import esymptom
from library.attention import attend
from datetime import datetime
from datetime import timedelta

def test_attention1():
    symptoms: list[esymptom] = [esymptom(12),esymptom(7)]
    pacient1 = cPacient("alma", "marquez", 45296117, 1234, symptoms, cColour(3))
    pacient2 = cPacient("lorenzo", "mazzante", 45296117, 1235, symptoms, cColour(1))
    pacient3 = cPacient("juan", "perez", 45296117, 1236, symptoms, cColour(1))
    pacient4 = cPacient("mauro", "garcia", 435534344, 43243)
    pacient5 = cPacient("pilar","esteban", 34324342,14343,symptoms)
    listpac = [pacient1, pacient2, pacient3, pacient4,pacient5]
    assert attend(listpac,0,len(listpac))==pacient1

def test_attention2():
    symptoms: list[esymptom] = [esymptom(12),esymptom(7)]
    pacient1 = cPacient("alma", "marquez", 45296117, 1234, symptoms, cColour(5))
    pacient2 = cPacient("lorenzo", "mazzante", 45296117, 1235, symptoms, cColour(1))
    pacient3 = cPacient("juan", "perez", 45296117, 1236, symptoms, cColour(1))
    listpac = [pacient1,pacient2,pacient3]

    with pytest.raises(InvalidPacient):
        attend(listpac, 0, len(listpac))

def test_attention3():
    symp: list[esymptom]=[esymptom(12), esymptom(8), esymptom(9)]
    p1=cPacient("leo", "messi", 1313131, 13, symp, cColour(4))
    p1.time_arrival=datetime.now()
    p2=cPacient("alma", "marquez", 45296117, 4545, symp, cColour(4))
    p2.time_arrival=datetime.now()+timedelta(minutes=30)
    p3=cPacient("lorenzo", "mazzante", 48965478, 4555, symp, cColour(4))
    p3.time_arrival=datetime.now()+timedelta(hours=1)
    listpac = [p1,p2,p3]

    with pytest.raises(InvalidPacient):
        attend(listpac,0,len(listpac))




