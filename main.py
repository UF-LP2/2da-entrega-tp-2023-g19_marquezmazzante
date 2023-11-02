#from src.attention import who_shall_I_Take_Care_of
#from src.diagnose import diagnose
#from src.cNurse import cNurse
#from src.cPacient import cPacient
#from src.cColour import cColour
from src.readFiles import readPacients
from src.readFiles import readNurses
import queue
NConsulMax = 10

def main_divide_and_conquer() -> None:
    listNurses = readNurses()
    queuePacients = readPacients()



if __name__ == "__main__":
    main_divide_and_conquer()
