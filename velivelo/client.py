def pseudoClientConforme(pseudo : str) -> bool:
    if pseudo == "":
        raise ValueError("pseudo ne peut pas une chaine vide")
    if not (3 <= len(pseudo) <= 10):
        return False
    if not pseudo[0].isupper():
        return False
    if not pseudo.isalnum():
        return False
    return True
