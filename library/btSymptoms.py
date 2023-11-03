import binarytree
from library.my_library import MyNode
def btsymptoms()->binarytree:

    bled=MyNode(90, "bled")                                 #1
    blackout=MyNode(40, "blackout")                         #2
    damaged_organs=MyNode(70, "damaged organs")             #3
    changing_behaviour=MyNode(30, "changing behaviour")     #4
    drooling=MyNode(41, "drooling")                         #5
    bloody_vomit=MyNode(50, "bloody vomit")                 #6
    abdominal_cramps=MyNode(25, "abdominal cramps")         #7
    neck_pain=MyNode(31, "neck pain")                       #8
    nausea=MyNode(20, "nausea")                             #9
    tachycardia=MyNode(42, "tachycardia")                   #10
    tearing_eyes=MyNode(26, "tearing eyes")                 #11
    facial_swelling=MyNode(35, "facial swelling")           #12
    eye_redness=MyNode(15, "eye redness")                   #13

    muscular_weakness=MyNode(32, "muscular weakness")       #14
    loss_of_balance=MyNode(36, "loss of balance")           #15
    headache=MyNode(16, "headache")                         #16
    chest_pain=MyNode(33, "chest pain")                     #17
    dizziness=MyNode(21, "dizziness")                       #18
    hearing_loss=MyNode(34, "hearing loss")                 #19
    pallor=MyNode(22, "pallor")                             #20
    daze=MyNode(23, "daze") ##aturdimiento                  #21
    sweat=MyNode(24, "sweat")                               #22
    hallucinations=MyNode(51, "hallucinations")             #23

    itch=MyNode(19, "itch")                                 #24
    clogged_ear=MyNode(29, "clogged ear")                   #25
    dental_sensibility=MyNode(10, "dental sensibility")     #26
    gum_bleeding=MyNode(27, "gum bleeding")                 #27
    oral_pain=MyNode(11, "oral pain")                       #28
    mild_pain=MyNode(28, "mild pain")                       #29
    traumatisms=MyNode(29, "traumatisms")                   #30
    sprain=MyNode(39, "sprain")                             #31

    no_urgency=MyNode(9, "no urgency")                      #32

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