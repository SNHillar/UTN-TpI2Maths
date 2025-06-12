
#ingresar dni n veces
#generar conjuntos de digitos unicos
#calcular union, interseccion y diferencia
#contar frecuencia de cada digito
#suma total de digitos

from functions import solicitar_dni, union, interseccion, evaluar_afinidad_numerica_especial, dif_simetrica, contar_frecuencia, diferencias, obtener_input_años_nacimiento, procesar_años_nacimiento, calcular_edades_actuales, calcular_producto_cartesiano


def main():
    lista_dni = solicitar_dni()
    
    conjunto_union = union(lista_dni)
    print(f"Conjunto de dígitos únicos (Unión): {conjunto_union}")
    
    conjunto_interseccion = interseccion(lista_dni)
    print(f"Conjunto de dígitos comunes (Intersección): {conjunto_interseccion}")
    
    evaluar_afinidad_numerica_especial(conjunto_interseccion)

    conjunto_dif_simetrica = dif_simetrica(lista_dni)
    print(f"Diferencia simétrica: {conjunto_dif_simetrica}")
    
    conjunto_diferencias = diferencias(lista_dni)
    print(f"Diferencias: {conjunto_diferencias}")
    
    frecuencia = contar_frecuencia(lista_dni)
    print(f"Frecuencia de cada dígito: {frecuencia}")
    print("\n" + "="*60 + "\n") # Un separador visual para las secciones
    
    # Obtenemos la cantidad de integrantes de la lista de DNI que ya se solicitó
    cantidad_integrantes = len(lista_dni) 
    
    # 
    años_nacimiento_ingresados = obtener_input_años_nacimiento(cantidad_integrantes)
    
    # Llamamos a la función para procesar los años de nacimiento
    procesar_años_nacimiento(años_nacimiento_ingresados)
    
    #calculamos las edades actuales y el producto cartesiano
    print("\n--- Cálculo de Edades y Producto Cartesiano ---")
    # Llamamos a la función para calcular las edades actuales y el producto cartesiano
    # Asumimos que el año actual es 2025 para el cálculo de edades
    edades_actuales = calcular_edades_actuales(años_nacimiento_ingresados)
    producto_cartesiano = calcular_producto_cartesiano(edades_actuales, años_nacimiento_ingresados)
    print(f"Edades actuales: {edades_actuales}")
    print(f"Producto cartesiano entre edades y años de nacimiento: {producto_cartesiano}")
    
    
    

main()
# Este código solicita una cantidad de DNI, procesa los dígitos únicos y calcula la unión, intersección, diferencia simétrica y diferencias entre ellos.
