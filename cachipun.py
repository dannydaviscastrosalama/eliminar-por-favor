import random as rd

def maquina():
    jugada = rd.randrange(0,3)
    if jugada == 0:
        return "piedra"
    if jugada == 1:
        return "papel"
    if jugada ==2:
        return "tijera"
    if jugada ==3:
        return "papel 3"
    if jugada ==4:
        return "tijera 4"
    if jugada ==5:
        return "tijera afgit"
 