import queue
from cPacient import cPacient
from cDisease import cDisease
from cColour import cColour
from queue import PriorityQueue
from divideandconq import who_shall_I_Take_Care_of

def prioridades(pacient: cPacient, cola: PriorityQueue):

    cola.put(pacient.disease.colour)

    return cola

if __name__ == "__main__":

    colapac=queue.PriorityQueue()
    mitia=cColour
    fiebre=cDisease("fiebre", mitia.AMARILLO.value, 25, "fiebrecita", 4)
    paciente=cPacient("alma", "marquez", 45296117, 1234, fiebre, 10)
    prioridades(paciente, colapac )
    verde = cColour
    caca = cDisease("caca", verde.VERDE.value, 60, "cacona", 2)
    pacientelolo = cPacient("lolo", "mazzante", 45296117, 1235, caca, 9)
    prioridades(pacientelolo, colapac)
    naranja = cColour
    coma = cDisease("no se despierta", naranja.NARANJA.value, 15, "coma", 9)
    pacientaylor = cPacient("taylor", "swift", 45296117, 1236, coma, 12)
    prioridades(pacientaylor, colapac)

    listapac=[paciente, pacientelolo, pacientaylor]

    print(who_shall_I_Take_Care_of(listapac,1, len(listapac)).name)

