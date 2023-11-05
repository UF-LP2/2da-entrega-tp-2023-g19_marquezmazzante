from library.cPacient import cPacient

def who_shall_I_Take_Care_of(lista_pac: list[cPacient],init: int,end: int) -> cPacient:
    if (len(lista_pac) == 0):
        raise Exception("lista vacia")

    if (end - init == 0):                                       ##tengo un solo paciente en la lista
        return lista_pac[init-1]

    elif (end - init == 1):                                     ##tengo dos pacientes en la lista
        coef1 = lista_pac[init-1].colour.value / lista_pac[init-1].timeremaining()
        coef2 = lista_pac[end-1].colour.value / lista_pac[end-1].timeremaining()
        if (coef1 >= coef2):
            return lista_pac[init-1]
        else:
            return lista_pac[end-1]

    else:                                                       ##tengo mas de 2 pacientes en la lista
        half = (end - init) // 2 + init
        pac_aux1 = who_shall_I_Take_Care_of(lista_pac, init, half)
        pac_aux2 = who_shall_I_Take_Care_of(lista_pac, half + 1, end)
        coef1 = pac_aux1.colour.value / pac_aux1.timeremaining()
        coef2 = pac_aux2.colour.value / pac_aux2.timeremaining()
        if (coef1 >= coef2):
            return pac_aux1
        else:
            return pac_aux2