from ejercicio_2 import busqueda_ceros
from ejercicio_3 import polinomio_Horner


import matplotlib.pyplot as plt


x = [(i/100)-2 for i in range (600)]                        # Determino intervalo: [-2, 4] con intervalos divididos por 0.01

y = [polinomio_Horner(xi)[0] for xi in x ]                  # Evaluo la funcion horner en esos x.

hx,hf = rnewton(polinomio_Horner,-2,1e-6,15)                # Obtengo los puntos dados por el Metodo de Newton. 
plt.plot (x, y, label = "Funcion f(x) = (((x)*x+1)*x-5)")   # Defino los x, y del gráfico.
plt.plot(hx,hf,'*')                                         

plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title ("Grafico de f(X) = x**3 + x - 5")
plt.legend()                                                # Leer
plt.show()                                                  # Mostrar