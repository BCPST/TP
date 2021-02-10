def appartient(x,L):
    k=0
    while k<len(L) and L[k]!=x:
        k=k+1
    if k==len(L):
        return(False)
    else:
        return(True)
        
def appartient2(x,L):
    n=len(L):
    for k in range(n):
        if L[k]==x:
            return(True)
    return(False)