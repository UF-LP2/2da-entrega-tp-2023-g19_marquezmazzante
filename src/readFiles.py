import csv
from library.cPacient import cPacient
from library.cNurse import cNurse
from src.eSymptoms import esymptom
import os


def readPacients() -> list[cPacient]:
    #pacients = queue.Queue()
    pacients: list[cPacient] = []
    current_directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_directory,"DATA_PACIENT.csv")

    with open(file_path) as file:
        reader = csv.reader(file)
        symptoms: list[esymptom]
        next(file)
        for row in reader:
            symptoms0 = row[4]
            symptomsaux: list[str] = symptoms0.split()
            symptoms = [esymptom(int(symptom))for symptom in symptomsaux]
            pacient0 = cPacient(row[0],row[1],row[2],row[3],symptoms)
            pacients.append(pacient0)
            #pacients.put(pacient0)
    return pacients

def readNurses() -> list[cNurse]:
    nurses: list[cNurse] = []
    current_directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_directory,"DATA_NURSE.csv")

    with open(file_path) as file:
        reader = csv.reader(file)
        next(file)
        for row in reader:
            nurse0 = cNurse(row[0],row[1],row[2],row[3])
            nurses.append(nurse0)
    return nurses