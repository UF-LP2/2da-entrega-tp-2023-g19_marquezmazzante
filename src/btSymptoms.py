import binarytree
from my_library import MyNode
def btsymptoms()->binarytree:

    bled=MyNode(90, "bled")
    blackout=MyNode(40, "blackout")
    damaged_organs=MyNode(70, "damaged organs")
    changing_behaviour=MyNode(30, "changing behaviour")
    drooling=MyNode(41, "drooling")
    bloody_vomit=MyNode(50, "bloody vomit")
    abdominal_cramps=MyNode(25, "abdominal cramps")
    neck_pain=MyNode(31, "neck pain")
    nausea=MyNode(20, "nausea")
    tachycardia=MyNode(42, "tachycardia")
    tearing_eyes=MyNode(26, "tearing eyes")
    facial_swelling=MyNode(35, "facial swelling")
    eye_redness=MyNode(15, "eye redness")

    muscular_weakness=MyNode(32, "muscular weakness")
    loss_of_balance=MyNode(36, "loss of balance")
    headache=MyNode(16, "headache")
    chest_pain=MyNode(33, "chest pain")
    dizziness=MyNode(21, "dizziness")
    hearing_loss=MyNode(34, "hearing loss")
    pallor=MyNode(22, "pallor")
    daze=MyNode(23, "daze") ##aturdimiento
    sweat=MyNode(24, "sweat")
    hallucinations=MyNode(51, "hallucinations")

    itch=MyNode(19, "itch")
    clogged_ear=MyNode(29, "clogged ear")
    dental_sensibility=MyNode(10, "dental sensibility")
    gum_bleeding=MyNode(27, "gum bleeding")
    oral_pain=MyNode(11, "oral pain")
    mild_pain=MyNode(28, "mild pain")
    traumatisms=MyNode(29, "traumatisms")
    sprain=MyNode(39, "sprain")

    no_urgency=MyNode(9, "no urgency")

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