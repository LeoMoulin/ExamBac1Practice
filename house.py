def peutaller(piece1, piece2, portes, eviter):

    if (piece1 in eviter):
        return False

    if (piece1 == piece2):
        return True
    
    eviter.append(piece1)

    possib = [x for x in portes if x[0] == piece1]

    for i in range(0, len(possib)):
        if (peutaller(possib[i][1], piece2, portes, eviter)):
            return True

    return False

def chemin(piece1, piece2, portes, eviter):
    if (piece1 in eviter):
        return None

    if (piece1 == piece2):
        return piece1

    possib = [x for x in portes if x[0] == piece1]
    eviter.append(piece1)
    
    if (piece1 == piece2):
        return piece1
    
    best = None

    for i in range(0, len(possib)):   
        add = chemin(possib[i][1], piece2, portes, eviter)

        if (add != None):
            new = piece1 + " " + add
        else : new = None

        if best == None:
            best = new
        
    return best

def cheminpluscourt(piece1, piece2, portes, eviter):
    if (piece1 in eviter):
        return None

    if (piece1 == piece2):
        return piece1

    possib = [x for x in portes if x[0] == piece1]
    eviter.append(piece1)
    
    if (piece1 == piece2):
        return piece1
    
    best = None

    for i in range(0, len(possib)):   
        add = cheminpluscourt(possib[i][1], piece2, portes, eviter)

        if (add != None):
            new = piece1 + " " + add
        else : new = None

        if best == None:
            best = new
        elif(best != None and new != None): 
            if (len(new) < len(best)):
                best = new
    
    return best
