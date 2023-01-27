def parallel(r):
    size = len(r)

    if (size >= 2 ):
        RT = 0
        for a in r:
            RT = (1/a) + RT

        Answer = 1/RT
        print("{0:.3f}".format(Answer))

    else: print ("error")

parallel([330, 1000, 2200])

def potential_divider(j,r):
    r_size = len(r)

    if (r_size > 0):
        Total_R = 0
        for a in r:
            Total_R = a + Total_R

        for a in r:
            VR = (j * a) / Total_R
            print(VR)


potential_divider (9, [3000, 1000])








    




