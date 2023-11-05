from src.readFiles import readNurses
from src.readFiles import readPacients
from datetime import datetime
from datetime import timedelta
from library.cPacient import cPacient
from library.cConsul import cConsul
from library.attention import who_shall_I_Take_Care_of
import time


NConsulMax = 5

def main_divide_and_conquer() -> None:

    contador = 0

    listNurses = readNurses()
    listPacients = readPacients("Mock_Data_Pacients.csv")

    listWaiting: list[cPacient] = []
    listAtention: list[cPacient] = []
    listConsul: list[cConsul] = [cConsul(1), cConsul(2), cConsul(3), cConsul(4), cConsul(5), cConsul(6), cConsul(7),
                                 cConsul(8), cConsul(9), cConsul(10)]

    time_actual = datetime.now()

    while(True):

        if (time_actual.hour >= 6 and time_actual.hour < 10 and len(listPacients) > 1):          #turno mañana , 2 enfermeros

            try:
                pacientaux = listPacients.pop(0)
                dummy = listNurses[0].diagnose(pacientaux)
                if pacientaux.colour.value == 5:
                    listAtention.append(pacientaux)
                else:
                    listWaiting.append(pacientaux)

                pacientaux = listPacients.pop(0)
                dummy = listNurses[1].diagnose(pacientaux)
                if pacientaux.colour.value == 5:
                    listAtention.append(pacientaux)
                else:
                    listWaiting.append(pacientaux)
            except Exception:
                print("wrong symptoms")

        elif (time_actual.hour >= 10 and time_actual.hour < 16 and len(listPacients) > 4):       #turno hora pico , 5 enfermeros

            try:
                pacientaux = listPacients.pop(0)
                dummy = listNurses[0].diagnose(pacientaux)
                if pacientaux.colour.value == 5:
                    listAtention.append(pacientaux)
                else:
                    listWaiting.append(pacientaux)

                pacientaux = listPacients.pop(0)
                dummy = listNurses[1].diagnose(pacientaux)
                if pacientaux.colour.value == 5:
                    listAtention.append(pacientaux)
                else:
                    listWaiting.append(pacientaux)

                pacientaux = listPacients.pop(0)
                dummy = listNurses[2].diagnose(pacientaux)
                if pacientaux.colour.value == 5:
                    listAtention.append(pacientaux)
                else:
                    listWaiting.append(pacientaux)

                pacientaux = listPacients.pop(0)
                dummy = listNurses[3].diagnose(pacientaux)
                if pacientaux.colour.value == 5:
                    listAtention.append(pacientaux)
                else:
                    listWaiting.append(pacientaux)

                pacientaux = listPacients.pop(0)
                dummy = listNurses[4].diagnose(pacientaux)
                if pacientaux.colour.value == 5:
                    listAtention.append(pacientaux)
                else:
                    listWaiting.append(pacientaux)
            except Exception:
                print("wrong symptoms")

        elif (time_actual.hour >= 16 and time_actual.hour < 23 and len(listPacients) > 2):       #turno tarde , 3 enfermeros

            try:
                pacientaux = listPacients.pop(0)
                dummy = listNurses[0].diagnose(pacientaux)
                if pacientaux.colour.value == 5:
                    listAtention.append(pacientaux)
                else:
                    listWaiting.append(pacientaux)

                pacientaux = listPacients.pop(0)
                dummy = listNurses[1].diagnose(pacientaux)
                if pacientaux.colour.value == 5:
                    listAtention.append(pacientaux)
                else:
                    listWaiting.append(pacientaux)

                pacientaux = listPacients.pop(0)
                dummy = listNurses[2].diagnose(pacientaux)
                if pacientaux.colour.value == 5:
                    listAtention.append(pacientaux)
                else:
                    listWaiting.append(pacientaux)
            except Exception:
                print("wrong symptoms")
            print(time_actual.hour)

        elif (len(listPacients) > 0):                                                               #turno noche , 1 enfermero

            try:
                pacientaux = listPacients.pop(0)
                dummy = listNurses[0].diagnose(pacientaux)
                if pacientaux.colour.value == 5:
                    listAtention.append(pacientaux)
                else:
                    listWaiting.append(pacientaux)
            except Exception:
                print("wrong symptoms")


        consulaux = (len(listWaiting) // 10) + 1
        if (consulaux >= NConsulMax):
            Nconsul_open = NConsulMax
        else:
            Nconsul_open = consulaux


        for j in range(Nconsul_open):
            if len(listWaiting) == 0:
                break
            elif listConsul[0] == None:
                    break
            elif listConsul[j].occupied == False:
                pacientaux = who_shall_I_Take_Care_of(listWaiting,0,len(listWaiting))
                listWaiting.remove(pacientaux)
                listAtention.append(pacientaux)
                #print("se atendio a",pacientaux.name, pacientaux.colour.value, contador)
                #contador += 1
                listConsul[j].empty_consul()


        time.sleep(1)


if __name__ == "__main__":
    main_divide_and_conquer()
