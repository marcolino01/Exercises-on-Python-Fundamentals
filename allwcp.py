# !!!! SONO TUTTE OPERAZIONI SU LISTE !!!
# Il problema. Cosa fare?
# 1) contare quanti calciatori hanno giocato per l'Italia
# 2) contare quanti calciatori hanno giocato per il Brasile
# 3) contare quanti calciatori hanno giocato per l'Argentina
# 4) Indicare quali calciatori hanno giocato sia per il Brasile, sia per l'Italia
# 5) Indicare quali calciatori hanno giocato sia per l'Argentina, sia per l'Italia
# 6) Trovare qual'è il calciatore più giovane che ha partecipato alla coppa del mondo
# 7) Trovare qual'è il calciatore più anziano che ha partecipato alla coppa del mondo
# 8) Trovare quale calciatore ha partecipato a più edizioni della coppa del mondo
# 9) Trovare quale squadra di calcio ha fornito più calciatori per la coppa del mondo
#    Organizzare per nazione. Cioè quale squadra italiana ha fornito più calciatori per la coppa del mondo e quanti, quale squadra francese, ...

# Cosa fare?

import json

filejson = open("all-world-cup-players.json","r",)
worldcup = json.load(filejson)
filejson.close()


Italiani = []

for v in worldcup:
    if v["Team"] in ["Italy","ITA"]:
        Italiani.append(v["FullName"])
ItalianiFracichi=set(Italiani) 
print("I calciatori italiani sono:",len(ItalianiFracichi))

Brasiliani = []

for v in worldcup:
    if v["Team"] in ["Brazil","BRA",]:
        Brasiliani.append(v["FullName"])
BrasilianiDeRio=set(Brasiliani)
print("I calciatori brasiliani sono:",len(BrasilianiDeRio))

def ContaCalciatori(elenco, squadra):
    calciatorisquadra = []
    for c in elenco:
        if c["Team"] in squadra:
            calciatorisquadra.append(c["FullName"])
    calciatorisquadraveri=set(calciatorisquadra)
    return len(calciatorisquadraveri)

print("i calciatori italiani sono:", ContaCalciatori(worldcup,["ITA","Italy"]))
print("i calciatori brasiliani sono:", ContaCalciatori(worldcup,["BRA","Brazil"]))
print("i calciatori argentini", ContaCalciatori(worldcup,["ARG","Argentina"]))

#per fare l'elenco degli oriundi uso il comando intersection
#devo creare un'altra funzione senza len per stampare direttamente il nome
def ContaCalciatori2(elenco, squadra):
    calciatorisquadra = []
    for c in elenco:
        if c["Team"] in squadra:
            calciatorisquadra.append(c["FullName"])
    calciatorisquadraveri=set(calciatorisquadra)
    return calciatorisquadraveri

calciatoriItaliani = ContaCalciatori2(worldcup,["ITA","Italy"])
calciatoriBrasiliani = ContaCalciatori2(worldcup,["BRA","Brazil"])
calciatoriArgentini = ContaCalciatori2(worldcup,["ARG","Argentina"])
print("i calciatori oriundi che hanno giacato sia per l'italia che per il brasile sono:",calciatoriItaliani.intersection(calciatoriBrasiliani))
print("i calciatori oriundi che hanno giocato sia per l'italia che per l'argentina sono:",calciatoriItaliani.intersection(calciatoriArgentini))



#per le date di nascita mi creo una lista di tutte le date di nascita e le ordino con "sorted"
età=[]
for v in worldcup:
    if v["DateOfBirth"]:
        età.append(v["DateOfBirth"])
print("le date di nascita del piu giovane e del piu anziano del:",max(età),min(età))
##vedere come stampare il nome de sti morti

#piu partecipazione ai mondiali


def Contanomi(elenco, giocatore):
    nomiripetuti = []
    for c in elenco:
        if c["FullName"] in giocatore:
            nomiripetuti.append(c["FullName"])
    return len(nomiripetuti) 

print(Contanomi(worldcup,["Gianluigi Buffon"]))











