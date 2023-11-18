from library.cPacient import cPacient,InvalidPacient

def attend(lista_pac: list[cPacient],init: int,end: int) -> cPacient:
    if (len(lista_pac) == 0):
        return None

    if (end - init == 0):                                       ##tengo un solo paciente en la lista
        return lista_pac[init-1]

    elif (end - init == 1):                                     ##tengo dos pacientes en la lista
        timeremaining1 = lista_pac[init-1].timeremaining()
        timeremaining2 = lista_pac[end-1].timeremaining()

        if(timeremaining1 <= 0):
            raise InvalidPacient(lista_pac[init-1])
        if(timeremaining2 <= 0):
            raise InvalidPacient(lista_pac[end-1])


        coef1 = lista_pac[init-1].colour.value / timeremaining1
        coef2 = lista_pac[end-1].colour.value / timeremaining2
        if (coef1 >= coef2):
            return lista_pac[init-1]
        else:
            return lista_pac[end-1]

    else:                                                       ##tengo mas de 2 pacientes en la lista
        half = (end - init) // 2 + init
        pac_aux1 = attend(lista_pac, init, half)
        pac_aux2 = attend(lista_pac, half + 1, end)
        coef1 = pac_aux1.colour.value / pac_aux1.timeremaining()
        coef2 = pac_aux2.colour.value / pac_aux2.timeremaining()
        if (coef1 >= coef2):
            return pac_aux1
        else:
            return pac_aux2