fin = open("alice.txt","r")         #r letture per leggere file
linee = fin.readlines()               #w (write) scrittura cancella il contenuto precedente
fin.close()                       #a append modifica il file aggiungendo nuovo contenuto a quello presente
#legge tutte le righe compres l'end of line


l1=[]
for l in linee:
    l1.append(l.strip())    #taglia spazi endline          isupper stampa maiusc
linee=l1

lista=[]
for l in linee:
    lista.extend(l.split(" "))

for k in range(0,(len(lista)-1)):
    print(lista[k])

