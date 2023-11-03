import time

from library.cPacient import cPacient
from library.eSymptoms import esymptom
from library.cColour import cColour
from library.attention import who_shall_I_Take_Care_of
from threading import Thread
from datetime import datetime

hora=datetime.now().hour
minutos= datetime.now().minute

def tiempito():
    global hora, minutos
    while True:
        if hora+1>=24: hora=0
        else: hora=hora+1
        if minutos+1>=60: minutos=0
        else: minutos=minutos+1
        print(hora, minutos)
        time.sleep(1)



if __name__ == "__main__":

    t1=Thread(target=tiempito(),)
    t1.start()
    verde = cColour(2)
    fiebre: list[esymptom] = [esymptom(21)]
     # caca: list[esymptom] = [esymptom(1), esymptom(31)]
     # nodespierta: list[esymptom] = [esymptom(7)]
     # naranja = cColour(4)
     #
    paciente = cPacient("alma", "marquez", 45296117, 1234, fiebre, verde)
    # pacientelolo = cPacient("lolo", "mazzante", 45296117, 1235, caca, verde)
    # pacientaylor = cPacient("taylor", "swift", 45296117, 1236, nodespierta, naranja)
    # pacientesims = cPacient("sims", "sims", 435534344, 43243)
    #
    # listapac = [paciente, pacientelolo, pacientaylor, pacientesims]
    # print(who_shall_I_Take_Care_of(listapac,0,len(listapac)).name)

    while(paciente.timeremaining() > 0):
        print (paciente.timeremaining())
        print (hora,minutos)

    print("termino")




    t1.join()

