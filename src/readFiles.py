import csv
from cPacient import cPacient
from cNurse import cNurse

def readPacients() -> list[cPacient]:
    pacients: list[cPacient] = []
    with open("DATA_PACIENT.csv") as file:
        reader = csv.reader(file)
        next(file)
        for row in reader:
            pacient0 = cPacient(row[0],row[1],row[2],row[3])
            pacients.append(pacient0)
    return pacients

def readNurses() -> list[cNurse]:
    nurses: list[cNurse] = []
    with open("DATA_NURSE.csv") as file:
        reader = csv.reader(file)
        next(file)
        for row in reader:
            nurse0 = cNurse(row[0],row[1],row[2],row[3])
            nurses.append(nurse0)

    return nurses

