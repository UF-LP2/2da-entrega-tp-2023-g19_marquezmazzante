import queue
from cPacient import cPacient
from eSymptoms import esymptom
from cColour import cColour
from attention import who_shall_I_Take_Care_of

#def prioridades(pacient: cPacient, cola: PriorityQueue):
#
 #   cola.put(pacient.disease.colour)
#
 #   return cola

if __name__ == "__main__":
    verde = cColour(2)
    fiebre: list[esymptom] = [esymptom(21)]
    caca: list[esymptom] = [esymptom(1), esymptom(31)]
    nodespierta: list[esymptom] = [esymptom(7)]
    naranja = cColour(4)

    paciente = cPacient("alma", "marquez", 45296117, 1234, fiebre, verde)
    pacientelolo = cPacient("lolo", "mazzante", 45296117, 1235, caca, verde)
    pacientaylor = cPacient("taylor", "swift", 45296117, 1236, nodespierta, naranja)
    pacientesims = cPacient("sims", "sims", 435534344, 43243)

    listapac = [paciente, pacientelolo, pacientaylor, pacientesims]


    print(who_shall_I_Take_Care_of(listapac,0,len(listapac)).name)

