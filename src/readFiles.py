import csv
from cPacient import cPacient
from cNurse import cNurse
from eSymptoms import esymptom

def readPacients() -> list[cPacient]:
    pacients: list[cPacient] = []
    with open("DATA_PACIENT.csv") as file:
        reader = csv.reader(file)
        symptoms: list[esymptom]
        next(file)
        for row in reader:
            symptoms0 = row[4]
            symptomsaux: list[str] = symptoms0.split()
            i = 0
            for i in range(len(symptomsaux)):
                symptoms[i] = esymptom(int(symptomsaux[i]))
                i = i+1
            pacient0 = cPacient(row[0],row[1],row[2],row[3],symptoms)
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

if __name__ == "__main__":
    listita = readPacients()