from ejercicio_1 import rsecante

# Metodo de newton
# Algoritmo del Metodo de Newton: permite encontrar aproximaciones de los ceros de una funcion. 
def rnewton(fun,x0,err,mit):
	hx = []
	hf = []
	f,df = fun(x0)

	for _ in range(mit):
		if df == 0:
			print("La derivada en el punto es nula.")
			break

		xn = x0 - f/df
		f, df = fun(xn)

		hx.append(xn)
		hf.append(f)

		if abs(xn-x0)/abs(xn) < err or abs(f)<err:
			break

		x0 = xn
	return hx, hf


#	Funcion busqueda_ceros: dada una funcion, dos puntos iniciales, una cota de error y un numero maximo de iteraciones
#	Imprime en pantalla los ceros encontrados por el metodo de Newton y por el Metodo de la Secante.
#	Devuelve la mejor aproximacion encontrada.

def busqueda_ceros(fun, x0, x1, err, mit):
    
    f = lambda x: fun(x)[0] 

    # Método de la secante:
    hxrs, hfrs = rsecante(f, x0, x1, err, mit)
    
    # Método de Newton:
    hxrn, hfrn = rnewton(fun, x0, err, mit)

    # Cantidad de iteraciones
    iter_hxrs = len(hxrs)
    iter_hxrn = len(hxrn)
    
    # Ceros encontrados
    cero_s = hxrs[-1]
    cero_n = hxrn[-1]

    print("....Algoritmo Del Método de la Secante....")
    print("Cantidad de iteraciones:  ", iter_hxrs)
    print("El cero encontrado es: " , cero_s)
    
    print("....Algoritmo Del Método de Newton....")
    print("Cantidad de iteraciones:  ", iter_hxrn)
    print("El cero encontrado es: " , cero_n)
    
    if abs(hfrn[-1]) < abs (hfrs[-1]):
        return cero_n
    else:
        return cero_s

