#%% Tri sélection

#%% Question 1

def indice_min(l,i):
    imin=i
    n=len(l)
    for j in range(i+1,n):
        if l[j]<l[imin]:
            imin=j
    return(imin)

#%% Question 2

def echange(l,i,j):
    L=l[:]
    L[i],L[j]=L[j],L[i]
    return(L)
    
def echange2(l,i,j):
    L=l[:]
    L[i]=l[j]
    L[j]=l[i]
    return(L)

def echange3(l,i,j):
    i0=min(i,j)
    i1=max(i,j)
    L=l[0:i]+[l[i1]]+l[i0+1:i1]+[l[i0]]+l[i1+1:len(l)]
    return(L)

#Ou des versions qui modifient directement la liste de départ
def echange4(l,i,j):
    i0=min(i,j)
    i1=max(i,j)
    x,y=l.pop(i1),l.pop(i0)
    l.insert(i0,x)
    l.insert(i1,y)
    
def echange5(l,i,j):
    l[i],l[j]=l[j],l[i]
    
#%% Question 3

def tri_selection(l):
    L=l[:]
    n=len(L)
    for i in range(n-1):
        imin=indice_min(L,i)
        echange(L,i,imin)
    return(L)

#Ou une version qui modifie directement la liste de départ

def tri_selection2(l):
    for i in range(len(l)-1):
        echange5(l,i,indice_min(l,i))

def main(l):
    tri_selection2(l)
    return(l)
        
        
        