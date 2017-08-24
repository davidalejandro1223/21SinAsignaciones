from random import *

def mazo():
    return sample([(x,y) for x in ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"] for y in["picas","corazones","treboles","diamantes"]],52)

def valor_carta(carta, paso):
    if carta[0] == "A":
        if paso:
            return 1
        else:
            return 11
    elif carta[0] in ["J","Q","K"]:
        return 10
    else:
        return int(carta[0])

def valor_mano(mano, paso):
	if mano == []:
		return 0
	return valor_carta(mano[0], paso) + valor_mano(mano[1:], paso)

def verC_a(carta):
    if(carta[0] == "A"):
        return True

def verM_a(mano):
    if(verC_a(mano[0:])):
        return True
    else:
        return verM_a



def jugar(mazo,manoJugador,manoCasa,plantoJug,paso):
	print valor_mano(manoCasa, paso)
	print manoCasa
	print valor_mano(manoJugador, paso)
	print manoJugador
	if mazo!=[] and valor_mano(manoJugador, paso)<= 21 and valor_mano(manoCasa, paso)<= 21:
		if(manoJugador == []):
			return jugar(mazo[4:],manoJugador + mazo[:2], manoCasa + mazo[2:4], False, paso)
		if(plantoJug == False):
			if(input("Pide carta?")==1):
				return jugar(mazo[1:],manoJugador + [mazo[0]], manoCasa, False, paso)
			else:
				if(valor_mano(manoCasa, paso)<18):
					return jugar(mazo[1:],manoJugador, manoCasa + [mazo[0]], True, paso)
				else:
					if(valor_mano(manoCasa, paso) >=valor_mano(manoJugador, paso)):
						print "Gano la casa"
					else:
						print "Gano el jugador"
		else:
			if(valor_mano(manoCasa, paso)<18):
				return jugar(mazo[1:],manoJugador, manoCasa + [mazo[0]], True, False)
			else:
				if(valor_mano(manoCasa, paso)>=valor_mano(manoJugador, paso)):
				    print "Gano la casa"
				else:
				    print "Gano el jugador"
	#elif (verM_a(manoJugador)):
	    #jugar(mazo, manoJugador, manoCasa, plantoJug, True)
        #elif (verM_a(manoCasa)):
            #jugar(mazo, manoJugador, manoCasa, plantoJug, True)
	elif(valor_mano(manoCasa, paso)>=18  or valor_mano(manoJugador, paso)>21):
	    if((valor_mano(manoCasa, paso)>=valor_mano(manoJugador, paso) and valor_mano(manoCasa, paso)<=21) or valor_mano(manoJugador, paso)>21):
	        print "Gano la casa"
	    else:
	        print "Gano el jugador"




jugar(mazo(),[],[],False,False)
