#Parcial 1 - Marina Rocio Nunez Heredia

# Funcion swap
# La funcion "swap" recibe dos parametros e intercambia el valor del uno por el otro. 
def swap(a, b):
    aux = a
    a = b 
    b = aux 

    return (a,b)


# Funcion que implementa el método de la secante.
# Funcion rsecante: función que aproxima a la raiz:
#    Parametros de entrada:
#		- fun : funcion a trabajar.
#		- x0 : punto inicial primero.
#		- x1 : punto inicial segundo
#		- err : tolerancia deseada de error.
#		- mit : maximo de iteraciones.
#	Salida: tupla con el historial de puntos medios y de los respectivos.


def rsecante(fun,x0,x1,err,mit):
    
    f_x0 = fun(x0)
    f_x1 = fun(x1)
    hx = []
    hf = []

    for _ in range(mit): 
        if abs(f_x0) < abs(f_x1):
            swap(x0,x1)

        s = (x1 - x0) / (f_x1 - f_x0)              # Cociente incremental.
        x1 = x0 
        f_x1 = f_x0
        x0 = x0 - (f_x0 * s)
        f_x0 = fun(x0)

        hx.append(x0)                             # Valor de punto medio.
        hf.append(f_x0)                           # Valor de la funcion.

        if abs (f_x0) < err:                      # El ciclo se corta si tengo un valor menor de f(x).
            break

    return (hx, hf)

# Funcion de prueba
def fun_prueba(x):
    fun_p = ((x-2)*(x+2))
    return fun_p

print(rsecante(fun_prueba,1,3,1e-6,100))

