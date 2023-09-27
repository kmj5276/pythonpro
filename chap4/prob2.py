import random
counter =int(0)
hhp = random.randrange(50,100)
mhp = random.randrange(50,100)
print("hero HP: ", hhp,"monster HP: ", mhp)
while hhp > 0 and mhp > 0 :
 hatk = random.randrange(-10,20)
 matk = random.randrange(-10,20)
 if(matk > 0) :
    hhp -= matk
 if(hatk > 0) :
    mhp -= hatk
 print("hero(HP:", hhp,", aatck: ", hatk,") " , end=' ')
 if(hatk > 0) :
    print("succes ", end=' ')
 elif(hatk <= 0) :  
    print("fail ", end= ' ')
 print("<-> monster(HP:", mhp,", aatck: ", matk,") " , end=' ')
 if(matk > 0) :
    print("succes")
 elif(matk <= 0) :
    print("fail")
 counter += 1
print("---------------------------------------------------------")
print("Total phase: ", counter, ",")
if(hhp <= 0) :
    print("Monster Win!!!!")
elif(mhp <= 0) :
    print("Hero Win!!!!")
