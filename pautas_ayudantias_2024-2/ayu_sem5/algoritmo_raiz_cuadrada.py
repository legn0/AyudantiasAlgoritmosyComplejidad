
def raiz(q,p):
    def raizAux(low, high, q, p):
        r = (high+low)/2
        if q < (r-p)**2 :
            return raizAux(low, r, q, p)
        elif q > (r+p)**2:
            return raizAux(r, high, q, p)
        else:
            return r
    
    return raizAux(0, q, q, p)

