def entiere(x):
    k=0
    if x>=0:
        while x>=0:
            x=x-1
            k=k+1
        return(k-1)
    else:
        while x<0:
            x=x+1
            k=k-1
        return(k)
        
def entiere2(x):
    k=0
    if x>=0:
        while x>=1:
            x=x-1
            k=k+1
        return(k)
    else:
        while x<0:
            x=x+1
            k=k-1
        return(k)