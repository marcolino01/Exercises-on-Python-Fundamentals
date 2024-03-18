import json
from datetime import datetime


#per leggere un file json
filejson= open("all-world-cup-players.json","r")
worldcup= json.load(filejson)
filejson.close

print(len(worldcup))
print(worldcup[8000])
print(worldcup[8000]['DateOfBirth'])



Italy = 0
Brazil = 0
Argentina = 0

for v in worldcup:
    if v["Team"] == "Italy":
        Italy+=1
    elif v["Team"] == "Brazil":
        Brazil+=1
    elif v["Team"] == "Argentina":
        Argentina+=1
print("Italiani:",Italy,"Brasile:",Brazil,"Argentina:",Argentina)

Oriundo=0
for v in worldcup:
    if v["Team"]=="Italy" and v["Team"]=="Brazil":
        Oriundo+=1
print("i giocatori che hanno giocato sia per il brasile che per l'italia sono:",Oriundo)

Oriundo2=0
for v in worldcup:
    if v["Team"]=="Italy" and v["Team"]=="Argentina":
        Oriundo2+=1
print("i giocatori che hanno giocato sia per l'italia che per l'argentina sono:",Oriundo2)

giovane_data_di_nascita = datetime.now()
giovane_giocatore = None

