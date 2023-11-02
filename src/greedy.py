import queue
from cPacient import cPacient
from cColour import cColour
from queue import PriorityQueue

def who_shall_I_Take_Care_of_GREEDY(colapac:queue.PriorityQueue) -> cPacient:

    pacienteaux = colapac.get()
    return pacienteaux