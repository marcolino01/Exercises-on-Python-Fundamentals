l1=[]
def novuota(l):
    for i in l:
        if len(i)>0:
            l1.append(i)
    return(l1)


l=["uno","due","","","tre"," ","fine"]
print(novuota(l))