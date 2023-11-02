import csv
from src.cPacient import cPacient
from src.cNurse import cNurse
from src.eSymptoms import esymptom
import queue

def readPacients() -> queue:
    pacients = queue.Queue()
    with open("DATA_PACIENT.csv") as file:
        reader = csv.reader(file)
        symptoms: list[esymptom]
        next(file)
        for row in reader:
            symptoms0 = row[4]
            symptomsaux: list[str] = symptoms0.split()
            symptoms = [esymptom(int(symptom))for symptom in symptomsaux]
            pacient0 = cPacient(row[0],row[1],row[2],row[3],symptoms)
            pacients.put(pacient0)
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