from src.readFiles import readNurses
from src.readFiles import readPacients
from datetime import datetime

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








if __name__ == "__main__":
    main_divide_and_conquer()
