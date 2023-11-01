import binarytree
from binarytree import Node
from cPacient import cPacient
from cColour import cColour
from cDisease import cDisease
from eSymptoms import esymptom
from eSymptoms import enumConverter
def btsymptoms()->binarytree:

    bled=Node(90, "bled")
    blackout=Node(40, "blackout")
    damaged_organs=Node(70, "damaged organs")
    changing_behaviour=Node(30, "changing behaviour")
    drooling=Node(41, "drooling")
    bloody_vomit=Node(50, "bloody vomit")
    abdominal_cramps=Node(25, "abdominal cramps")
    neck_pain=Node(31, "neck pain")
    nausea=Node(20, "nausea")
    tachycardia=Node(42, "tachycardia")
    tearing_eyes=Node(26, "tearing eyes")
    facial_swelling=Node(35, "facial swelling")
    eye_redness=Node(15, "eye redness")

    muscular_weakness=Node(32, "muscular weakness")
    loss_of_balance=Node(36, "loss of balance")
    headache=Node(16, "headache")
    chest_pain=Node(33, "chest pain")
    dizziness=Node(21, "dizziness")
    hearing_loss=Node(34, "hearing loss")
    pallor=Node(22, "pallor")
    daze=Node(23, "daze") ##aturdimiento
    sweat=Node(24, "sweat")
    hallucinations=Node(51, "hallucinations")

    itch=Node(19, "itch")
    clogged_ear=Node(29, "clogged ear")
    dental_sensibility=Node(10, "dental sensibility")
    gum_bleeding=Node(27, "gum bleeding")
    oral_pain=Node(11, "oral pain")
    mild_pain=Node(28, "mild pain")
    traumatisms=Node(29, "traumatisms")
    sprain=Node(39, "sprain")

    no_urgency=Node(9, "no urgency")

    ##hago un intento de binarytree mas desbalanceado q mi vida

    ##lado derecho (rojos y naranjas)
    blackout.right=drooling
    drooling.right=tachycardia
    drooling.left=neck_pain
    tachycardia.left=eye_redness
    tachycardia.right=damaged_organs
    damaged_organs.left=bloody_vomit
    damaged_organs.right=bled
    neck_pain.left=tearing_eyes
    neck_pain.right=facial_swelling
    tearing_eyes.left=nausea
    tearing_eyes.right=changing_behaviour
    facial_swelling.left=abdominal_cramps
    ##lado izq amarillos verdes y azules

    blackout.left=muscular_weakness
    muscular_weakness.left=pallor
    muscular_weakness.right=loss_of_balance
    pallor.left=itch
    pallor.right=chest_pain
    loss_of_balance.left=hearing_loss
    loss_of_balance.right=daze
    chest_pain.left=headache
    chest_pain.right=hallucinations
    daze.left=dizziness
    daze.right=sweat
    hearing_loss.left=clogged_ear
    hearing_loss.right=sprain
    itch.left=dental_sensibility
    itch.right=mild_pain
    mild_pain.left=gum_bleeding
    mild_pain.right=traumatisms
    dental_sensibility.left=no_urgency
    dental_sensibility.right=oral_pain

    return blackout

def search(symp : str, btree: binarytree) -> int:

    if(btree==None):
        return 0
    if(symp==btree.name):
        return btree.value

    aux = search(symp, btree.left)
    if aux==0:
        aux = search(symp, btree.right)
    return aux

def diagnose(pacient: cPacient):
    if paciente.symptoms[0] == esymptom(32) and len(paciente.symptoms) > 1:
        raise Exception("not valid pacient")

    assign = 0
    tree = btsymptoms()
    for i in range(len(pacient.symptoms)):
        assign = assign + search(enumConverter(pacient.symptoms[i].value), tree)

    if assign >= 90:
        pacient.colour = 1
    elif assign < 90 and assign >= 70:
        pacient.colour = 2
    elif assign < 70 and assign >= 50:
        pacient.colour = 3
    elif assign < 50 and assign >= 30:
        pacient.colour = 4
    elif assign < 30 and assign >= 10:
        pacient.colour = 5
    return pacient.colour



if __name__ == "__main__":

    verde = cColour(2)
    sintomitas: list[esymptom] = [esymptom(21),esymptom(22)]
    paciente = cPacient("alma", "marquez", 45296117, 1234, sintomitas)
    print(diagnose(paciente))
