import queue
from cPacient import cPacient
from cDisease import cDisease
from cColour import cColour
from queue import PriorityQueue
from divideAndConquer import who_shall_I_Take_Care_of
def prioridades(pacient: cPacient, cola: PriorityQueue):

    cola.put(pacient.disease.colour)

    return cola

if __name__ == "__main__":

    verde = cColour(2)
    fiebre = cDisease("fiebre", verde)
    paciente = cPacient("alma", "marquez", 45296117, 1234, fiebre)
    caca = cDisease("caca", verde)
    pacientelolo = cPacient("lolo", "mazzante", 45296117, 1235, caca)
    naranja = cColour(4)
    coma = cDisease("no se despierta", naranja)
    pacientaylor = cPacient("taylor", "swift", 45296117, 1236, coma)

    listapac=[paciente, pacientelolo, pacientaylor]


    print(who_shall_I_Take_Care_of(listapac,1, len(listapac)).name)

