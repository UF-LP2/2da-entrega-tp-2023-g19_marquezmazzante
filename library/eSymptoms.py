from enum import Enum

class esymptom(Enum):
    bled=1
    blackout=2
    damaged_organs=3
    changing_behaviour=4
    drooling=5
    bloody_vomit=6
    abdominal_cramps=7
    neck_pain=8
    nausea=9
    tachycardia=10
    tearing_eyes=11
    facial_swelling=12
    eye_redness=13
    muscular_weakness=14
    loss_of_balance=15
    headache=16
    chest_pain=17
    dizziness=18
    hearing_loss=19
    pallor=20
    daze=21
    sweat=22
    hallucinations=23
    itch=24
    clogged_ear=25
    dental_sensibility=26
    gum_bleeding=27
    oral_pain=28
    mild_pain=29
    traumatisms=30
    sprain=31
    no_urgency=32


def enumConverter(aux: esymptom):
    if aux==1: return "bled"
    elif aux==2: return "blackout"
    elif aux==3: return "damaged organs"
    elif aux==4: return "changing behaviour"
    elif aux==5: return "drooling"
    elif aux==6: return "bloody vomit"
    elif aux==7: return "abdominal cramps"
    elif aux==8: return "neck pain"
    elif aux==9: return "nausea"
    elif aux==10: return "tachycardia"
    elif aux==11: return "tearing eyes"
    elif aux==12: return "facial swelling"
    elif aux==13: return "eye redness"
    elif aux==14: return "muscular weakness"
    elif aux==15: return "loss of balance"
    elif aux==16: return "headache"
    elif aux==17: return "chest pain"
    elif aux==18: return "dizziness"
    elif aux==19: return "hearing loss"
    elif aux==20: return "pallor"
    elif aux==21: return "daze"
    elif aux==22: return "sweat"
    elif aux==23: return "hallucinations"
    elif aux==24: return "itch"
    elif aux==25: return "clogged ear"
    elif aux==26: return "dental sensibility"
    elif aux==27: return "gum bleeding"
    elif aux==28: return "oral pain"
    elif aux==29: return "mild pain"
    elif aux==30: return "traumatisms"
    elif aux==31: return "sprain"
    elif aux==32: return "no urgency"



