from cmath import pi

r1=int(input("inserisci valore di r1:"))
r2=int(input("inserisci valore di r2:"))
r3=int(input("inserisci valore di r3:"))
h=int(input("inserisci valore di h:"))
s1=pi*(r1**2)
s2=pi*(r2**2)
s3=pi*(r3**2)
V=1/6*h*(s1+4*s2+s3)
l=V/1000
print("la tua botte puo contere ",l," litri")