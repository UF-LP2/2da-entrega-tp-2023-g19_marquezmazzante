import pytest

from library.cPacient import cPacient
from library.diagnose import diagnose
from library.eSymptoms import esymptom
from src.readFiles import readPacients

def test_diagnose1():
     listPacients: list[cPacient] = readPacients()
     listPacients = readPacients()
     diagnoses: list[int] = [3,1,5,1,5,5,3,4,2,4,1,1,4,4,2,1,3,1,5,1,5,3,5,3,2,3,1,1,2,1,2,1,1,1,4,2,5,3,1,1,1,4,2,2,1,2,1,2,2,5]

     for i in range (len(diagnoses)):
          assert diagnose(listPacients[i]) == diagnoses[i]
          i = i +1

def test_diagnose2():
     pacientByDefault = cPacient("sims", "sims", 435534344, 43243)
     assert diagnose(pacientByDefault) == 1

def test_diagnose3():
     symptoms1 = [esymptom(32),esymptom(12)]
     pacient1 = cPacient("Lorenzo","Mazzante", 44958354, 212312,symptoms1)
     with pytest.raises(Exception):
          diagnose(pacient1)


# def test_search1():
#      tree = btsymptoms()
#      assert search("bloody vomit", tree) == 50
#
# def test_search2():
#      tree = btsymptoms()
#      assert search("bled", tree) == 90

