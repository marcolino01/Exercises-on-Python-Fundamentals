# Leggere da un file (persone.txt) i nomi, cognomi e eta di un gruppo di persone. 
#organizzarli in un dizionario la cui chiave è il cognome e il cui valore è una t-upla
#contenente i tre valori letti.

file=open("persone.csv","r")
ElencoPersone=file.readlines()
file.close()

print(ElencoPersone)

elencopersoneol=[]
for l in ElencoPersone:
    elencopersoneol.append(l.strip())

print(elencopersoneol)

persone=[]
for v in elencopersoneol:
   persone.append(v.split(","))

print("Nome:",persone[0],"Cognome:",persone[1],"Età",persone[2])


dizionario=dict

for v in elencopersoneol:
    persona=v.split(",")
    dizionario[persone[1]]=(persone[0],persone[1],persone[2])
print(dizionario)


for e in dizionario:
    print("key:",e ,"value:", dizionario)