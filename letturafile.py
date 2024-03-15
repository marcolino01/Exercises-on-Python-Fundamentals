# Leggere da un file (persone.txt) i nomi, cognomi e eta di un gruppo di persone. organizzarli
# in un dizionario la cui chiave è il cognome e il cui valore è una tupla
#contenente i tre valori letti.

text=open("persone.csv","r")
righe=text.readlines()
text.close()
lista1=[]
Nome=()
Cognome=()
Età=()

for n in righe:
    lista1.append(n.strip())

righe=lista1

lista1=[]


for n in righe:
    lista1.extend(n.split(","))

for n in range(0,len(lista1),3):
    print("nome:",lista1[n],"cognome:",lista1[n+1],"età:",lista1[n+2])

