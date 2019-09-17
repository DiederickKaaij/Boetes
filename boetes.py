def hoogteBoete(snelheid):
    
    if snelheid < 55:
        return "OK"
    elif snelheid > 80:
        return "Rijbewijs ingenomen"
    else:
        snelheid -= 50
        boete = int(snelheid / 5)
        boete = boete * 10
        return boete
        