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






    




