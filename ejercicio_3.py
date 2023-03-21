from ejercicio_2 import busqueda_ceros
from aux_horner import horn
#	Funcion polinomio_Horner: dada una lista de coeficientes de un polinomio, un mayor grado,
#	un menor grado, y un valor de x.
#   Devuelve el polinomio evaluado en ese valor x por el metodo de Horner.

def polinomio_Horner(x):
    p1 = horn([1,0,1,-5],x)
    p2 = horn([3,0,1],x)

    return p1 , p2

print(f"El punto mas cercano a la raiz es: {busqueda_ceros(polinomio_Horner,10.0,-10.0,1e-6,15)}")
