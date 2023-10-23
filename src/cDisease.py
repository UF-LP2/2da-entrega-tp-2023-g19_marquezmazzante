from cColour import cColour
class cDisease:
    def __init__(self, symptom, colour, max_time, diseaseName, severity):
        self.symptom: str =symptom
        self.colour: cColour =colour
        self.max_time: int =max_time
        self.diseaseName: str =diseaseName
        self.severity: int =severity
