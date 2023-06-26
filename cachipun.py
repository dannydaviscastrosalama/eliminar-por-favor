import random as rd

def maquina():
    jugada = rd.randrange(0,3)
    if jugada == 0:
        return "piedra"
    if jugada == 1:
        return "papel"
    if jugada ==2:
        return "tijera"
    