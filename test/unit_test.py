import pytest
from src.symptomsbt import diagnose
from src.cPacient import cPacient
from src.eSymptoms import esymptom
from src.symptomsbt import search
from src.symptomsbt import btsymptoms

def diagnose_test1():
    sintomas:list[esymptom] =[esymptom(2),esymptom(15), esymptom(31)]
    alma=cPacient("alma", "marquez","45296117", 1234, sintomas)
    assert (diagnose(alma) == 1) == True

def diagnose_test2():
    sintomas:list[esymptom]=[esymptom(1)]
    loren=cPacient("lolo","mazzante","45296117", 1234, sintomas)
    assert(diagnose(loren)==1) == True

def search_test1():
    tree=btsymptoms()
    assert search("bloody vomit", tree) == 50

def search_test2():
    tree=btsymptoms()
    assert search("bled", tree) == 90

