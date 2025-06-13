def solicitar_dni():
    lista_dni = []
    cantidadDni = int(input("Ingrese la cantidad de DNI a procesar: "))

    for i in range (1, cantidadDni + 1):
        dni = input(f"Ingrese el DNI {i}: ")
        while not dni.isdigit() or len(dni) != 8:
            print("DNI inválido. Debe contener 8 dígitos.")
            dni = input(f"Ingrese el DNI {i} nuevamente: ")
        lista_dni.append(dni)
    return lista_dni


def union(lista_dni):
    conjunto_union = set()
    #recorremos la lista de DNI y agregamos los dígitos únicos a un conjunto
    for i in range(len(lista_dni)):
        conjunto_digitos = set(lista_dni[i])
        if i == 0:
            conjunto_union = conjunto_digitos
        else:
            conjunto_union.update(conjunto_digitos)
    #retornamos el conjunto de dígitos únicos
    return conjunto_union

def interseccion(lista_dni):
    conjunto_interseccion = set()
    #recorremos la lista de DNI y agregamos los dígitos únicos a un conjunto
    for i in range(len(lista_dni)):
        conjunto_digitos = set(lista_dni[i])
        if i == 0:
            conjunto_interseccion = conjunto_digitos
        else:
            conjunto_interseccion.intersection_update(conjunto_digitos)
    #retornamos el conjunto de dígitos únicos
    return conjunto_interseccion


def dif_simetrica(lista_dni):
    conjunto_dif_simetrica = set()
    #recorremos la lista de DNI y agregamos los dígitos únicos a un conjunto
    for i in range(len(lista_dni)):
        conjunto_digitos = set(lista_dni[i])
        if i == 0:
            conjunto_dif_simetrica = conjunto_digitos
        else:
            conjunto_dif_simetrica.symmetric_difference_update(conjunto_digitos)
    #retornamos el conjunto de dígitos únicos
    return conjunto_dif_simetrica

def diferencias(lista_dni):
    conjunto_diferencias = set()
    #recorremos la lista de DNI y agregamos los dígitos únicos a un conjunto
    for i in range(len(lista_dni)):
        conjunto_digitos = set(lista_dni[i])
        if i == 0:
            conjunto_diferencias = conjunto_digitos
        else:
            conjunto_diferencias.difference_update(conjunto_digitos)
    return conjunto_diferencias

def contar_frecuencia(lista_dni):
    frecuencia = {}
    for dni in lista_dni:
        for digito in dni:
            if digito in frecuencia:
                frecuencia[digito] += 1
            else:
                frecuencia[digito] = 1
    return frecuencia

# Se agrega funcion para expresion logica: Si la suma de los elementos de la interseccion de los conjuntos es par
# entonces hay una afinidad numérica especial
#     print("\n--- Evaluación de Expresión Lógica (Parte Matemática) ---")
""" 
Evalúa si la suma de los elementos de la intersección de los conjuntos es par.
Imprime un mensaje indicando el resultado de la condición lógica. 
"""
### inicio de funciones agregadas
def evaluar_afinidad_numerica_especial(conjunto_interseccion):
    suma_interseccion = sum(int(digito) for digito in conjunto_interseccion)
    print(f"suma de los elementos de la interseccion: {suma_interseccion}")
    
    #evaluamos condicion
    if suma_interseccion % 2 == 0:
        print("¡Hay una afinidad numérica especial en este grupo!")
    else:
        print("No hay una afinidad numérica especial en este grupo.")

def obtener_input_años_nacimiento(num_integrantes):
    años = []
    print("Ingreso de años de nacimiento")
    for i in range (1, num_integrantes + 1): #bucle para n integrantes si decidimos mantener que el usuario pueda agregar mas de 2
        año_valido_unico = False #bandera para no usar break y controlar el while
        while not año_valido_unico: # necesitamos repetir la solicitud de un año individual hasta que la entrada sea completamente válida
            try: #capturamos errores acá
                año_ingresado = int(input(f"ingrese año de nacimiento del integrante {i}:"))
                if not (1900 < año_ingresado < 2025):
                    print ("Por favor, ingresa un año razonable (entre 1901 y 2024). ")
                    continue # vuelve al inicio del while para pedir de nuevo
                if num_integrantes > 1 and año_ingresado in años:
                    print ("Este año de nacimiento ya fue ingresado")
                    continue
                años.append(año_ingresado)
                año_valido_unico = True # sale del while para este integrante
            except ValueError:
                print("Entrada Invalida, por favor ingresa un numero.")
    return años

def es_biciesto(año):
    #devuelve true si es bisiesto, false si no.
    return ( año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)



def procesar_años_nacimiento(años_lista):
    # contamos cuantos nacieron en años pares e impares
    print("\n--- Procesando Años de Nacimiento ---")
    años_pares = 0
    años_impares = 0
    todos_despues_de_2000 = True 
    biciesto_encontrado = False
    for año in años_lista:
        if año % 2 == 0:
            años_pares += 1
        else:
            años_impares += 1
        
        if año <= 2000:
            todos_despues_de_2000 = False # bandera


        if es_biciesto(año):
            biciesto_encontrado = True
    print(f"Cantidad de integrantes nacidos en año par: {años_pares}")
    print(f"Cantidad de integrantes nacidos en año impar: {años_impares}")


    if todos_despues_de_2000:
        print("Grupo Z")
    else:
        print("falso, no todos nacieron despues del 2000")
            
    if biciesto_encontrado:
        print("Tenemos un años especial")
        print("ninguno nació en año biciesto")
#### fin funciones agregadas

#agregando funcion para calcular las edades actuales
# Esta función calcula las edades actuales basándose en los años de nacimiento proporcionados.
def calcular_edades_actuales(años_nacimiento):
    edades = []
    for año in años_nacimiento:
        edad = 2025 - año  # Asumiendo que el año actual es 2025 (se puede hacer importando el módulo datetime)
        edades.append(edad)
    # Convertimos la lista de edades a un conjunto para obtener edades actuales
    return set(edades)

# Esta función calcula el producto cartesiano entre las edades y los años de nacimiento.
def calcular_producto_cartesiano(edades, años_nacimiento):
    producto_cartesiano = set()
    for edad in edades:
        for año in años_nacimiento:
            producto_cartesiano.add((edad, año))
    return producto_cartesiano
