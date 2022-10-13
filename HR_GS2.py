import numpy as np

def pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq):
    # print(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq)
    ab = ((x1-x2)**2 + (y1-y2)**2)**.5
    bc = ((x3-x2)**2 + (y3-y2)**2)**.5
    ac = ((x1-x3)**2 + (y1-y3)**2)**.5
    
    # ap = ((x1-xp)**2 + (y1-yp)**2)**.5
    # bp = ((x2-xp)**2 + (y2-yp)**2)**.5
    # cp = ((x3-xp)**2 + (y3-yp)**2)**.5

    # aq = ((x1-xq)**2 + (y1-yq)**2)**.5
    # bq = ((x2-xq)**2 + (y2-yq)**2)**.5
    # cq = ((x3-xq)**2 + (y3-yq)**2)**.5

    

    # abv = [x1 - x2, y1 - y2]
    # apv = [x1 - xp, y1 - yp]
    # aqv = [x1 - xq, y1 - yq]

    # bcv = [x2 - x3, y2 - y3]
    # bpv = [x2 - xp, y2 - yp]
    # bqv = [x2 - xq, y2 - yq]

    # cav = [x3 - x1, y3 - y1]
    # cpv = [x3 - xp, y3 - yp]
    # cqv = [x3 - xq, y3 - yq]



    abv = get_vector(x1,y1,x2,y2)
    apv = get_vector(x1,y1,xp,yp)
    aqv = get_vector(x1,y1,xq,yq)

    bcv = get_vector(x3,y3,x2,y2)
    bpv = get_vector(x2,y2,xp,yp)
    bqv = get_vector(x2,y2,xq,yq)

    cav = get_vector(x1,y1,x3,y3)
    cpv = get_vector(x2,y2,xp,yp)
    cqv = get_vector(x3,y3,xq,yq)

    abap = np.cross(abv, apv)
    bcbp = np.cross(bpv, bpv)
    acap = np.cross(cav, apv)

    abaq = np.cross(abv, aqv)
    bcbq = np.cross(bpv, bqv)
    acaq = np.cross(cav, aqv)

    p = q = False
    
    if (abap >= 0 and bcbp >= 0 and acap >= 0) or (abap < 0 and bcbp < 0 and acap < 0):
        p = True
    
    
    if (abaq >= 0 and bcbq >= 0 and acaq >= 0) or (abaq < 0 and bcbq < 0 and acaq < 0):
        q = True

    if ab + bc > ac and bc + ac > ab and ab + ac > bc:
        if p and not q:
            return 1
        elif q and not p:
            return 2
        elif q and p:
            return 3
        return 4
    return 0

def get_vector(x1, y1, x2, y2):
        return [x1 - x2, y1 - y2]

# print(pointsBelong(0,0,2,0,4,0,2,0,4,0))
# print(pointsBelong(2,2,7,2,5,4,4,3,7,4))
print(1 == pointsBelong(3,1,7,1,5,5,3,1,0,0))