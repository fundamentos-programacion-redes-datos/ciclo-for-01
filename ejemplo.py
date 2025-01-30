"""
    Ejemplo de uso del ciclo for

for variable in <colección-iterable>:
    // instrucción
    // instrucción

Ejemplo:
    Genere una solución que permita presentar la suma y 
    el promedio de los números del 1 al 10.

"""

print("Ejemplo de uso del ciclo for en Python\n") # es un mensaje en pantalla
# Declaración de variables
numero = 1   # Contador: controla el número hasta donde debe ejecutarse el bucle
suma = 0     # Acumulador: almacena la suma total de los números
promedio = 0 # Variable para calcular el promedio

# Proceso para calcular la suma usando un ciclo For
for numero in range(1, 11):  # El bucle recorre los valores del 1 al 10 
                            # (incremento por defecto es 1)
                            # la función range genera una lista con los siguientes
                            # valores [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; donde
                            # range es la función propia de python
                            # 1 es el valor de inicial para los valores de range
                            # 11 es el límte superior, no se incluye, en este
                            # caso el máximo valor es 10
    suma = suma + numero  # Se acumula el valor actual en la variable suma

# Calcular el promedio, se lo hace fuera del ciclo
promedio = suma / 10  # Se divide la suma total entre 10

# Presentar los resultados
print("La suma de los números del 1 al 10 es: %d" % suma)
print("El promedio de los números del 1 al 10 es: %.2f" % promedio)
