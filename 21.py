from random import *

def mazo():
    return sample([(x,y) for x in ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"] for y in["picas","corazones","treboles","diamantes"]],52)

def valor_carta(carta):
	if carta[0] == "A":
		return 1
	elif carta[0] in ["J","Q","K"]:
		return 10
	else:
		return int(carta[0])

def valor_mano(mano):
	if mano == []:
		return 0
	return valor_carta(mano[0]) + valor_mano(mano[1:])


def jugar(mazo,manoJugador,manoCasa):
	print valor_mano(manoCasa)
	print manoCasa
	print valor_mano(manoJugador)
	print manoJugador
	if mazo!=[] and valor_mano(manoJugador)<= 21 and valor_mano(manoCasa)<= 21:
		if(manoJugador == []):
			return jugar(mazo[4:],manoJugador + mazo[:2], manoCasa + mazo[2:4])	
		return jugar(mazo[2:],manoJugador + [mazo[0]], manoCasa + [mazo[1]])


jugar(mazo(),[],[])
