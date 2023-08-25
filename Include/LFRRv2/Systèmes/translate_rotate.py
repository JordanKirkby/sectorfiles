# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

# -------------------------------------------
# traitement fichier texte
# -------------------------------------------
f=open("coordonneesdegreminsec.txt","r")
text=f.readlines()
L=[]
for i in text:
    L.append(i)

# ----------------------------------------------------------------------
# lecture de tout un bloc et decoupage en liste de blocs
# ----------------------------------------------------------------------

def test(L):
    chiffres=["0","1","2","3","4","5","6","7","8","9"]
    Lutil=[]
    Linter=[]
    Linter2=[]
    for i in range(len(L)):

        if len(L[i])<30 or L[i][1] not in chiffres and L[i][2] not in chiffres:

            if Linter2!=[]:

                Linter.append(Linter2)
                Lutil.append(Linter)
                Linter=[L[i]]
                Linter2=[]
            else:
                Linter.append(L[i])
        else:
            Linter2.append(L[i])
    Linter.append(Linter2)
    Lutil.append(Linter)
    return(Lutil)
                
# ---------------------------------------------------------------------
# traitement
# ---------------------------------------------------------------------
def traitement(L):
    chiffres=["0","1","2","3","4","5","6","7","8","9"]
    L2=[L[i] for i in range(len(L))]

# ---------------------------------------------------------------------
# signage de la liste
# ---------------------------------------------------------------------

    Lsignes=[]
    for i in range(len(L2)):
        Lsignes.append(["",""])
        for j in L2[i]:
            if j=="E":
                Lsignes[i][1]="+"
            if j=="W":
                Lsignes[i][1]="-"
            if j=="N":
                Lsignes[i][0]="+"
            if j=="S":
                Lsignes[i][0]="-"

# ---------------------------------------------------------------------
# Conversion de coordonnees
# ---------------------------------------------------------------------

    Ltraitement=[]
    for i in range(len(L2)):
        Ltraitement.append([L2[i][1:14],L2[i][16:29]])
        compteur=0
        degrelat=""
        minutelat=""
        secondelat=""
        degrelong=""
        minutelong=""
        secondelong=""
        for j in range(len(Ltraitement[i][0])):
            if compteur==0:
                if str(Ltraitement[i][0][j]) in chiffres:
                    degrelat+=str(Ltraitement[i][0][j])
                    degrelong+=str(Ltraitement[i][1][j])
                else:
                    compteur+=1
            elif compteur==1:
                if str(Ltraitement[i][0][j]) in chiffres:
                    minutelat+=str(Ltraitement[i][0][j])
                    minutelong+=str(Ltraitement[i][1][j])
                else:
                    compteur+=1
            elif compteur>=2:
                if str(Ltraitement[i][0][j]) in chiffres or str(Ltraitement[i][0][j])==".":
                    secondelat+=str(Ltraitement[i][0][j])
                    secondelong+=str(Ltraitement[i][1][j])
                else:
                    compteur+=1
        Ltraitement[i][1]=str(int(degrelong)+int(minutelong)/60+float(secondelong)/3600)
        Ltraitement[i][0]=str(int(degrelat)+int(minutelat)/60+float(secondelat)/3600)
    
    for i in range(len(Ltraitement)):
        if Lsignes[i][0]=="-":
            Ltraitement[i][0]=-float(Ltraitement[i][0])
        elif Lsignes[i][0]=="+":
            Ltraitement[i][0]=+float(Ltraitement[i][0])
        if Lsignes[i][1]=='-':
            Ltraitement[i][1]=-float(Ltraitement[i][1])
        elif Lsignes[i][1]=="+":
            Ltraitement[i][1]=+float(Ltraitement[i][1])
    return(Ltraitement)

# ---------------------------------------------------------------------
# recherche de point median
# ---------------------------------------------------------------------
def decale(L):
    latmoy=0
    longmoy=0
    for i in L:
        latmoy+=i[0]
        longmoy+=i[1]
    latmoy=latmoy/len(L)
    longmoy=longmoy/len(L)
    print("indiquer la coordonnée vers laquelle vous voulez déplacer le contenu du dossier")
    newcoord=[input()]
    newcoord=traitement(newcoord)
    latnew=newcoord[0][0]
    longnew=newcoord[0][1]
    longdiff=longnew-longmoy
    latdiff=latnew-latmoy
    return(latdiff,longdiff)

# --------------------------------------------------------------
# reconversion inverse
# --------------------------------------------------------------

def scan(coordonnees):
    compteur=0
    retour=[]
    for i in coordonnees:
        if i!="." and i!=";":
            compteur+=1
        else:
            retour.append(compteur)
            compteur=0
    return(retour)

# -------------------------------------------
# ecriture en format traitable
# -------------------------------------------
def conversion(L):
    texte=''
    Linter=[]
    L2=[]
    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j]!=",":
                texte+=L[i][j]
            else:
                Linter.append(texte)
                texte=""
            if j==len(L[i])-1:
                Linter.append(texte)
                L2.append(Linter)
                texte=""
                Linter=[]
    L2=[L2[i] for i in range(1,len(L2))]
    
    # -------------------------------------------
    # Recuperation des signes pour differentier N/S et E/W (et faire les calculs en positif)
    # -------------------------------------------
    
    Lsignes=[]
    for i in range(len(L2)):
        Lsignes.append([])
        for j in range(len(L2[i])):
            if float(L2[i][j])<0:
                Lsignes[i].append("-")
                L2[i][j]=L2[i][j][1:-1]
            else:
                Lsignes[i].append("+")
    # -------------------------------------------
    # Calculs de conversion de coordonnées du format décimal vers le format degres minutes secondes
    # -------------------------------------------
    

    L3=[]
    for i in range(len(L2)):
    # latitudes (N/S)
        Ltemp=[float(L2[i][0]),float(L2[i][1])]
        texte=''
        degres=int(Ltemp[0])
        if degres==0:
            minutes=int(Ltemp[0]*60)
            if minutes==0:
                secondes=round(Ltemp[0]*3600,3)
            else:
                secondes=round((Ltemp[0]*60%minutes)*60,3)
        else:
            minutes=int((Ltemp[0]%degres)*60)
            if minutes==0:
                secondes=round((Ltemp[0]%degres)*3600,3)
            else:
                secondes=round(((Ltemp[0]%degres)*60%minutes)*60,3)
                
        if Lsignes[i][0]=="+":
            texte+='N'+"".join("0"*(3-len(str(degres))))+str(degres)+"."+str(minutes)+"."+str(secondes)+";"
        if Lsignes[i][0]=="-":
            texte+='S'+"".join("0"*(3-len(str(degres))))+str(degres)+"."+str(minutes)+"."+str(secondes)+";"
            
    # Longitude (E/W)
        Ltemp=[float(L2[i][0]),float(L2[i][1])]
        degres=int(Ltemp[1])
        if degres==0:
            minutes=int(Ltemp[1]*60)
            if minutes==0:
                secondes=round(Ltemp[1]*3600,3)
            else:
                secondes=round((Ltemp[1]*60%minutes)*60,3)
        else:
            minutes=int((Ltemp[1]%degres)*60)
            if minutes==0:
                secondes=round((Ltemp[1]%degres)*3600,3)
            else:
                secondes=round(((Ltemp[1]%degres)*60%minutes)*60,3)
                
        if Lsignes[i][1]=="+":
            texte+='E'+"".join("0"*(3-len(str(degres))))+str(degres)+"."+str(minutes)+"."+str(secondes)+";"
        if Lsignes[i][1]=="-":
            texte+='W'+"".join("0"*(3-len(str(degres))))+str(degres)+"."+str(minutes)+"."+str(secondes)+";"
        L3.append(texte)
    
    for i in range(len(L3)):
        listecorrection=scan(L3[i])
        listetemoin=[4,2,2,3,4,2,2,3]
        listebilan=[listetemoin[i]-listecorrection[i] for i in range(len(listetemoin))]
        for j in range(len(listebilan)):
            if listebilan[j]!=0:
                if j==1:
                    L3[i]=L3[i][0:5]+"".join("0"*listebilan[j])+L3[i][5:-1]+";"
                if j==2:
                    L3[i]=L3[i][0:8]+"".join("0"*listebilan[j])+L3[i][8:-1]+";"
                if j==3:
                    L3[i]=L3[i][0:12]+"".join("0"*listebilan[j])+L3[i][12:-1]+";"
                if j==5:
                    L3[i]=L3[i][0:20]+"".join("0"*listebilan[j])+L3[i][20:-1]+";"
                if j==6:
                    L3[i]=L3[i][0:23]+"".join("0"*listebilan[j])+L3[i][23:-1]+";"
                if j==7:
                    L3[i]=L3[i][0:27]+"".join("0"*listebilan[j])+L3[i][27:-1]+";"
    Lsortie=[]
    for i in range(len(L3)):
        Lsortie.append(L3[i])
    return(Lsortie)

Lutil=test(L)
listemoyennee=[]
for i in range(len(Lutil)):
    listemoyennee+=Lutil[i][-1]
Ltraitement=traitement(listemoyennee)
latdiff,longdiff=decale(Ltraitement)
for i  in range(len(Lutil)):
    Linter=Lutil[i][-1]
    Lutil[i][-1]=traitement(Linter)
    for j in range(len(Lutil[i][-1])):
        Lutil[i][-1][j][0]=str(float(Lutil[i][-1][j][0])+latdiff)
        Lutil[i][-1][j][1]=str(float(Lutil[i][-1][j][1])+longdiff)

Lsortie=[]
for i in Lutil:
    for j in i:
        if type(j)==str:
            Lsortie.append(j)
        if type(j)==list:
            for k in range(len(j)):
                Lsortie+=conversion(["bla"]+[(j[k][0]+','+j[k][1])])
    
    
f2=open("Translation.txt","w")
for i in range(len(Lsortie)):
    f2.write(Lsortie[i])
    f2.write("\n")
f2.close()