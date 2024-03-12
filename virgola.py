num = " "
virgola = False
while True:
    a = input("Digita 0-9,+-/=: ")
    if len(a)>0:
        a = a[0]
    
    if len(a)==0:
        continue
    if a=="," :
            if virgola==False:
                virgola=True
                num = num+a
            else:
                continue
    else:
        if a not in ["0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9", ","]:
                print("il numero è", num)
                break
        else:
                num = num+a