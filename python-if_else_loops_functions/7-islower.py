#!/usr/bin/python3
def islower(c):
    # Vérifie si c est compris entre a et z
    if ord('a') <= ord(c) <= ord('z'):
        return True
    else:
        return False
