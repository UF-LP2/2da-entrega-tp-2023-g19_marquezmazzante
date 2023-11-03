from src.readFiles import readNurses
from src.readFiles import readPacients
from datetime import datetime
from library.cPacient import cPacient
from library.diagnose import diagnose
from library.cConsul import cConsul
from library.attention import who_shall_I_Take_Care_of
import time

NConsulMax = 10

def main_divide_and_conquer() -> None:

    listNurses = readNurses()
    listPacients = readPacients()

    time_actual = datetime.now()
    if (time_actual.hour > 6 and time_actual.hour < 10):       #turno mañana
        nNurses = 2
    elif (time_actual.hour > 10 and time_actual.hour < 16):    #turno hora pico
        nNurses = 5
    elif (time_actual.hour > 16 and time_actual.hour < 23):    #turno tarde
        nNurses = 3
    else:                                                      #turno noche
        nNurses = 1

    listWaiting: list[cPacient] = []
    listAtention: list[cPacient] = []
    listConsul: list[cConsul] = [cConsul(1),cConsul(2),cConsul(3),cConsul(4),cConsul(5),cConsul(6),cConsul(7),cConsul(8),cConsul(9),cConsul(10)]

    while(True):

        for i in range (len(listPacients)):
            pacientaux: cPacient = listPacients.pop(0)
            dummy = diagnose(pacientaux)

            if pacientaux.colour == 5:
                listAtention.append(pacientaux)
            else:
                listWaiting.append(pacientaux)

        consulaux = (len(listWaiting) // 10) + 1
        if (consulaux >= NConsulMax):
            Nconsul_open = NConsulMax
        else:
            Nconsul_open = consulaux

        for j in range(Nconsul_open):
            if listConsul[j].occupied == False:
                pacientaux = who_shall_I_Take_Care_of(listWaiting,0,len(listWaiting))
                listWaiting.remove(pacientaux)
                listAtention.append(pacientaux)
                print("se atendio a",pacientaux.name)
                listConsul[j].empty_consul()
            if listConsul[0] == None:
                break

        time.sleep(1)


if __name__ == "__main__":
    main_divide_and_conquer()
