def horn(coef, x):
    n = len(coef)
    b = coef[0]

    for i in range(1,n):
        b = coef[i] + x * b
    return b

