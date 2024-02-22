import numbers


a=print
a="ciao come va"
#In una stanza entrano, uno dopo l'altro, 10 persone, rispettivamente:
#antonio, marco, andrea, luigi, tony, bruno, laura, anita, annarita, lucia
#le prime due vanno via dopo un pochino di tempo ma entrano altre tre persone
#john, alice, mary
#altre due vanno via, sempre in ordine di ingresso (primo entrato, primo a uscire)
#stampare l'elenco delle persone presenti
persone=["antonio","marco","andrea","luigi","tony","bruno","laura","anita","annarita","lucia"]
print(persone)

persone.pop(0)
persone.pop(0)
print(persone)

persone.append("john")
persone.append("alice")
persone.append("mary")
print(persone)

persone.pop(0)
persone.pop(0)
print(persone)

a=1000000
num=0
for i in range(1000001):
    print(i)
    num=num+i
print(num)
media=num/a
print(media)