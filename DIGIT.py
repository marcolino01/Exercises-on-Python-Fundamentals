"""def Digit():
    lista=[]
    for i in range(0,10000):
        s=str(i)
        while len(s) <4:
            s="0"+s
        lista.append(s)
    return lista
print(Digit())"""

def splitlist(sd):
    lista=[]
    for i in sd:
        lista.append(int(i))
    return lista
print(splitlist("353473"))
     
    
