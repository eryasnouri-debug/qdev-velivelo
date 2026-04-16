from enum import Enum

class Verdict(Enum):
    SANS_DEPASSEMENT = 0
    AVEC_DEPASSEMENT = 1
    AMENDE = 2

def horsForfait(dureeLocation : int, tempsRestant : int) -> Verdict:
    if dureeLocation <= 0:
        raise ValueError("duree de la location doit etre superieure a 0")
    if dureeLocation > 240:
        return Verdict.AMENDE
    if dureeLocation <= tempsRestant:
        return Verdict.SANS_DEPASSEMENT
    
    return Verdict.AVEC_DEPASSEMENT
