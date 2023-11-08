import pytest
from src.btSymptoms import btsymptoms
from src.searchsymptoms import search
from library.cPacient import cPacient
from src.eSymptoms import esymptom
from src.readFiles import readPacients
from library.cNurse import cNurse


def test_diagnose1():
    nurse = cNurse("alma", "marquez", 1522, 1254)
    listPacients: list[cPacient] = readPacients("DATA_PACIENT.csv")
    diagnoses: list[int] = [3,1,5,1,5,5,3,4,2,4,1,1,4,4,2,1,3,1,5,1,5,3,5,3,2,3,1,1,2,1,2,1,1,1,4,2,5,3,1,1,1,4,2,2,1,2,1,2,2,5]

    for i in range(len(diagnoses)):
        assert nurse.diagnose(listPacients[i]) == diagnoses[i]

def test_diagnose2():
    nurse = cNurse("alma", "marquez", 1522, 1254)
    pacientByDefault = cPacient("sims", "sims", 435534344, 43243)
    assert nurse.diagnose(pacientByDefault) == 1

def test_diagnose3():
    nurse = cNurse("alma", "marquez", 1522, 1254)
    symptoms1 = [esymptom(32),esymptom(12)]
    pacient1 = cPacient("Lorenzo","Mazzante", 44958354, 212312,symptoms1)
    with pytest.raises(Exception):
          nurse.diagnose(pacient1)

def test_diagnose4():
     nurse=cNurse("alma", "marquez", 1522, 1254)
     pacientByDefault = cPacient("sims", "sims", 435534344, 43243)
     assert nurse.diagnose(pacientByDefault) == 1

def test_search1():
      tree = btsymptoms()
      assert search("bloody vomit", tree) == 50

def test_search2():
      tree = btsymptoms()
      assert search("bled", tree) == 90

#h