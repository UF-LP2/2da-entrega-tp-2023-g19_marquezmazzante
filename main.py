from src.readFiles import readNurses
from src.readFiles import readPacients
from datetime import datetime
from datetime import timedelta
from library.cPacient import cPacient, InvalidPacient
from library.cConsul import cConsul
from library.attention import attend
import time
from threading import Thread

Hour: datetime=datetime.now()
running = True

def tiempito():
    global Hour
    global running
    while running:
        Hour=Hour+timedelta(minutes=1)
        time.sleep(1)

Npacientes = 100
NConsulMax = 5

def main() -> None:
    global running
    listNurses = readNurses()
    listPacients = readPacients("Mock_Data_Pacients.csv", Npacientes)

    listWaiting: list[cPacient] = []
    listAtention: list[cPacient] = []
    listConsul: list[cConsul] = [cConsul(1), cConsul(2), cConsul(3), cConsul(4), cConsul(5), cConsul(6), cConsul(7),
                                 cConsul(8), cConsul(9), cConsul(10)]

    t1 = Thread(target=tiempito, )
    t1.daemon = True    #Establece el hilo en 2do plano para poder interrumpir el ciclo
    t1.start()
    try:
        while running:

            if (Hour.hour >= 6 and Hour.hour < 10 and len(listPacients) > 1):          #turno mañana , 2 enfermeros

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
                    print("pacient with wrong symptoms")

            elif (Hour.hour >= 10 and Hour.hour < 16 and len(listPacients) > 4):       #turno hora pico , 5 enfermeros

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
                    print("pacient with wrong symptoms")

            elif (Hour.hour >= 16 and Hour.hour < 23 and len(listPacients) > 2):       #turno tarde , 3 enfermeros

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
                    print("pacient with wrong symptoms")

            elif (len(listPacients) > 0):                                                               #turno noche , 1 enfermero

                try:
                    pacientaux = listPacients.pop(0)
                    dummy = listNurses[0].diagnose(pacientaux)
                    if pacientaux.colour.value == 5:
                        listAtention.append(pacientaux)
                    else:
                        listWaiting.append(pacientaux)
                except Exception:
                    print("pacient with wrong symptoms")


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
                    try:
                        pacientaux = attend(listWaiting,0,len(listWaiting))
                    except InvalidPacient as IP:
                        listWaiting.remove(IP.pacient)
                        print(IP.mesage)
                    listWaiting.remove(pacientaux)
                    listAtention.append(pacientaux)
                    print("pacient cared of:",pacientaux.name, pacientaux.colour.name)
                    listConsul[j].empty_consul()

            time.sleep(1)
    except KeyboardInterrupt:
        print("\nPROGRAMA INTERRUMPIDO MANUALMENTE")
        running = False
    t1.join()


if __name__ == "__main__":
    main()
