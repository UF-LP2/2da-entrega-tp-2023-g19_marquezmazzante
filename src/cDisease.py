from cColour import cColour
class cDisease:
    def __init__(self, symptom = None, colour = None):
        if symptom is None:
            self.symptom = ""
        else:
            self.symptom: str =symptom
        if colour is None:
            self.colour = cColour(1)
        else:
            self.colour: cColour =colour

        if (self.colour.value == 5):
            self.max_time = 0
        elif(self.colour.value == 4):
            self.max_time = 10
        elif(self.colour.value == 3):
            self.max_time = 60
        elif(self.colour.value == 2):
            self.max_time = 120
        elif(self.colour.value == 1):
            self.max_time = 240