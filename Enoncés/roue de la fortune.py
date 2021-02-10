#%%exo 1

liste=[1,2,'a','b',5]
M=[['a','b'],['c','d']]

#%% definition de L

L=[1,2,3,4,5,'toto']


#%%roue de la fortune 1 (entrer les termes de la liste sans crochets ni virgule car input)

liste=list(input("entrez la liste "))
x=int(input("entrez la valeur à chercher x "))
r=int(input("entrez le rang de la liste à tester "))
liste[r]==x
while int(liste[r])!=x:
    print("raté !")
    r=int(input("entrez un nouveau rang "))
    print(type(liste[r]))
    print(type(x))
    liste[r]==x
print(r)
print("bravo !")
#%%roue de la fortune 2

liste=list(input("entrez la liste"))
x=int(input("entrez la valeur à chercher x "))
r=int(input("entrez le rang de la liste à tester "))
liste[r]==x
if liste[r]!=x:
    while liste[r]!=x:
        if r < len(liste):
            print("raté !")
            r=r+1
            liste[r]==x
        else r > len(liste):
            print("raté !")
            r=r-1
            liste[r]==x
else liste[r]=x:
    print(r)
    print("bravo !")
    
#%%roue de la fortune def 1

def exo1(x,L):
    k=0
    while k<len(L) and L[k]!=x:
        k=k+1
        if k==len(L):
            return(False)
        else:
            return(True)
            

#%%roue de la fortune def 2

def exo2(x,L):
    k=0
    while k<len(L):
        if L[k]==x:
            return(True)
        else:
            k=k+1
            return(False)
            
#%%roue de la fortune def 3

def exo3(x,L):
    for k in range(len(L)):
        if L[k]==x:
            return(True)
        else:
            return(False)
    
#%% afficher tous les termes d'une liste (élément par élément ou indice par indice)

L=[1,2,3,4,5,'toto']

for k in range(0,len(L)):
    print (L[k])


for k in range(len(L)):
    print (L[k])


for x in L:
    print (x)

























