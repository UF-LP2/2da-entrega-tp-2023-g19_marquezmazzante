from library.cPacient import cPacient
from library.eSymptoms import esymptom
from library.diagnose import diagnose
from library.diagnose import search
from library.btSymptoms import btsymptoms

def test_diagnose1():
     sintomas:list[esymptom] =[esymptom(2),esymptom(15), esymptom(31)]
     alma=cPacient("alma", "marquez","45296117", 1234, sintomas)
     assert diagnose(alma) == 5
def test_diagnose2():
     sintomas:list[esymptom]=[esymptom(1)]
     loren=cPacient("lolo","mazzante","45296117", 1234, sintomas)
     assert diagnose(loren) == 5

def test_search1():
     tree = btsymptoms()
     assert search("bloody vomit", tree) == 50

def test_search2():
     tree = btsymptoms()
     assert search("bled", tree) == 90
