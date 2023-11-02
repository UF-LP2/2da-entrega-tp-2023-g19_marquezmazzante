import src.cPacient
import src.eSymptoms
import src.cColour
from src.cPacient import cPacient
from src.eSymptoms import esymptom
from src.cColour import cColour

def test_DyC1():
    symptoms: list[esymptom] = [esymptom(12),esymptom(7)]
    pacient1 = cPacient("alma", "marquez", 45296117, 1234, symptoms, cColour(3))
    pacient2 = cPacient("lolo", "mazzante", 45296117, 1235, symptoms, cColour(5))
    pacient3 = cPacient("taylor", "swift", 45296117, 1236, symptoms, cColour(5))
    pacientsims = cPacient("sims", "sims", 435534344, 43243)
    listapac = [pacient1, pacient2, pacient3, pacientsims]
    assert pacient1 == pacient1


def test_DyC2():
    symptoms: list[esymptom] = [esymptom(12),esymptom(7)]
    pacient1 = cPacient("alma", "marquez", 45296117, 1234, symptoms, cColour(1))
    listapac = [pacient1]
    assert listapac[0] == pacient1