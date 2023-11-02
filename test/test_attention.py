from library.cPacient import cPacient
from library.cColour import cColour
from library.eSymptoms import esymptom
from library.attention import who_shall_I_Take_Care_of
from library.diagnose import diagnose


def test_attention1():
    assert cColour(1).value == 1
    symptoms: list[esymptom] = [esymptom(12),esymptom(7)]
    pacient1 = cPacient("alma", "marquez", 45296117, 1234, symptoms, cColour(3))
    pacient2 = cPacient("lolo", "mazzante", 45296117, 1235, symptoms, cColour(1))
    pacient3 = cPacient("taylor", "swift", 45296117, 1236, symptoms, cColour(1))
    pacientsims = cPacient("sims", "sims", 435534344, 43243)
    listapac = [pacient1, pacient2, pacient3, pacientsims]
    assert pacient1 == pacient1
    assert who_shall_I_Take_Care_of(listapac,0,len(listapac))==pacient1


def test_attention2():
    symptoms: list[esymptom] = [esymptom(12),esymptom(7)]
    pacient1 = cPacient("alma", "marquez", 45296117, 1234, symptoms, cColour(1))
    listapac = [pacient1]
    assert listapac[0] == pacient1

def test_actual():
    assert 1 == 1

def test_diagnose1():
    sintomas:list[esymptom] =[esymptom(2),esymptom(15), esymptom(31)]
    alma=cPacient("alma", "marquez","45296117", 1234, sintomas)
    assert (diagnose(alma) == 1) == True
