# Importa el módulo random para generar números aleatorios
import random  

# Define la tolerancia del 5% para las resistencias, usamos uniform para general el numero aleatorio en un rango 
tolerancia_resistencias = random.uniform(-0.05, 0.05)  

#funcion para ver si el numero es real
def es_numero_real(numero):
    #verificamos si el numero es negativo
    if numero[0] == '-':
        #tomamos el valor digitado desde el 2 caracter, osea despues del -
        numero = numero[1:]
        #se busca el primer punto decimal, y lo reemplazamos por una cadena vacia, el 1 es para solo reemplazar el primer punto (.) y evitar errores, para luego poderlo pasar por el isdigit y no tenga errores
    return numero.replace('.', '', 1).isdigit()

# Función para calcular la resistencia total del circuito
def calcular_resistencia_total(resistencias):
    return sum(resistencias) # sum se usa para sumar todos los elementos de la lista resistencias 

# Función para calcular la corriente del circuito usando la ley de Ohm
def calcular_corriente(voltaje, resistencia_total):
    return voltaje / resistencia_total  

#esta funcion coge la resistencia y le asigna su tolerancia
def simular_tolerancias(valor):
    variacion = valor * tolerancia_resistencias  # Simula la tolerancia de las resistencias aplicando un valor aleatorio
    return valor + variacion  # Devuelve el valor simulado de la resistencia

# aca definimos el valor de la corriente para convetir todo en su escala
def interpretar_valor_corriente(valor):
    # Función para interpretar y formatear el valor de la corriente en diferentes unidades (Amperios, miliAmperios, etc.)
    if valor >= 1e3:
        return f"{valor/1e3:.2f} KiloAmperios"
    elif valor >= 1:
        return f"{valor:.2f} Amperios"
    elif valor >= 1e-3:
        return f"{valor*1e3:.2f} miliAmperios"
    elif valor >= 1e-6:
        return f"{valor*1e6:.2f} microAmperios"
    elif valor >= 1e-9:
        return f"{valor*1e9:.2f} nanoAmperios"

# Función para interpretar y convertir el valor de la resistencia a Ohmios
def interpretar_valor_resistencia(valor):
    
    #si viene un numero acompañado de  K o k en la variable nos lo multiplica por  1000 
    # y que no debe haber un - en la primera posicion
    if valor[-1] == 'K' or valor[-1] == 'k' and valor[0] != "-" :
        #convierto el valor en float, todo lo que esta antes de la posicion -1
        valor=float(valor[:-1])
        #si valor es diferente de 0 me retorna el valor multiplicado por 1000
        if valor != 0:
            return valor * 1000
        #si es 0 me retorna el None 
        else:
            return None
        
    #si viene un numero acompañado de  M en la variable nos lo multiplica por  1000000
    # y que no debe haber un - en la primera posicion
    elif valor[-1] == 'M'and valor[0] != "-" :
        #convierto el valor en float, todo lo que esta antes de la posicion -1
        valor=float(valor[:-1])
        #si valor es diferente de 0 me retorna el valor multiplicado por 1000000
        if valor != 0:
            return valor * 1000000
        #si es 0 me retorna el None 
        else:
            return None
        
    #si el valor es igual a 0 me mande un None
    elif valor == "0":
        return None
    
    #si el valor es un numero lo tome como un float
    elif valor.isdigit():
        return float(valor)
     
    # de lo contrario si viene un valor diferente me mande none 
    else:
        return None  

def formatear_valor_resistencia(valor):
    # Función para formatear el valor de la resistencia en diferentes unidades (Ohmios, Kiloohmios, etc.)
    if valor >= 1e6:
        return f"{valor/1e6:.2f} Megaohmios"
    elif valor >= 1e3:
        return f"{valor/1e3:.2f} Kiloohmios"
    elif valor >= 1:
        return f"{valor:.2f} Ohmios"
    elif valor >= 1e-6:
        return f"{valor*1e6:.2f} microohmios"
    elif valor >= 1e-3:
        return f"{valor*1e3:.2f} miliOhmios"
# Función para construir un circuito interactivo
def construir_circuito():
    # Inicializa la representación visual del circuito
    circuito = ""  
    # Lista para almacenar los valores de resistencia
    resistencias = [] 
    while True:
        
        # Solicita el voltaje de la fuente
        voltaje_fuente = input("Ingrese el valor de la fuente de voltaje (en voltios): ")
        # si voltaje es igual a 0 sale un mensaje y te retorna a la pregunta nuevamente, para que digites un valor valido
        if voltaje_fuente== "0":
            print("\n-------Ingresa un valor valido (diferente de 0 para la fuente)-------\n")
            #paso el valor digitado en voltaje_fuente  por la funcion es_numero_real
            #si cumple con las condiciones osea , si es un numero real me retorna un True
            #por detras y sigue con lo que esta adentro del condicional
        elif es_numero_real(voltaje_fuente):
            #como ya sabemos que es un valor , lo convierto  en un float
            voltaje_fuente=float(voltaje_fuente)
             
            
            # Imprime el voltaje de la fuente inicial
            print(f"\n(V{voltaje_fuente}) -> ")  
            break
            
        else:
            print("\n-------Error: ¡Debes ingresar un número válido!-------\n")
        
        
    #Creo un ciclo
    while True:
        #Hago un Menu para el programa
        print("\n*********** Seleccione una opción: **********")
        print("1. Agregar resistencia en serie.")
        print("2. Agregar resistencia en paralelo.")
        print("3. Cerrar circuito.")
        # Solicita al usuario que digite opción
        opcion = input("Seleccione una opción: ")  
        
        #Creo un codicional por la opcion digiada es la 1 ( Agregar resistencia en serie.)
        if opcion == '1':  
            #creo un ciclo para cuando el usuario el usuario digite un valor incorrecto de la resistencia
            while True:
                valor_resistencia = input("Ingrese el valor de la resistencia en serie (con sufijo K para kiloohmios o M para megaohmios): ")
                #asigno a valor_resistencia la respuesta de ejecutar 
                #la funcion interpretar_valor_resistencia  con lo que digito el usuario
                valor_resistencia = interpretar_valor_resistencia(valor_resistencia) # Convierte el valor a Ohmios
                # si es valor no es None sale del bucle o ciclo y entra al menu nuevamente
                if valor_resistencia is not None:
                    break  # Sale del bucle si el valor es válido
                # de lo contrario si es None me sale un mensaje para que digite un valor valido de la resistencia
                else:
                    print("\n-------Valor de resistencia no válido. Por favor, ingrese un valor válido.-------\n")
            #a circuito le sumo este string para seguir con el plano del circuitos que se muestra en pantalla
            circuito += f"|-RS{valor_resistencia}-| -> "  
            
            # Imprime el circuito actualizado
            print(f"\n(V{voltaje_fuente}) -> {circuito}") 
            # Agrega el valor de resistencia a la lista 
            resistencias.append(valor_resistencia)  

        elif opcion == '2':  # Si elige agregar resistencia en paralelo
            while True:
                valor_resistencia1 = input("Ingrese el valor de la primera resistencia en paralelo (con sufijo K para kiloohmios o M para megaohmios): ")
                valor_resistencia1 = interpretar_valor_resistencia(valor_resistencia1)
                if valor_resistencia1 is not None:
                    break
                else:
                    print("\n-------Valor de la primera resistencia no válido. Por favor, ingrese un valor válido.-------\n")

            while True:
                valor_resistencia2 = input("Ingrese el valor de la segunda resistencia en paralelo (con sufijo K para kiloohmios o M para megaohmios): ")
                valor_resistencia2 = interpretar_valor_resistencia(valor_resistencia2)
                if valor_resistencia2 is not None:
                    break
                else:
                    print("\n-------Valor de la segunda resistencia no válido. Por favor, ingrese un valor válido.-------\n")

            circuito += f"|-RP{valor_resistencia1}/{valor_resistencia2}-| "
            print(f"\n(V{voltaje_fuente}) -> {circuito}")
            #hacemos la formula para calcular al resistencia en paralelo
            resistencia_Paralelo=(1/((1/valor_resistencia1)+(1/valor_resistencia2)))
            #se agrega a resistencias el valor calculado de Resistencia_Paralelo
            resistencias.extend([resistencia_Paralelo])

        elif opcion == '3':  # Si elige cerrar el circuito
            if resistencias:
                # Simula las tolerancias de las resistencias y calcula la resistencia total y la corriente
                # con el for recorremos una por una las resistencias 
                # y se hace la simulacion de las tolerancia y se le da su nuevo valor
                resistencias_con_tolerancia = [simular_tolerancias(valor) for valor in resistencias]
                resistencia_total = calcular_resistencia_total(resistencias_con_tolerancia)
                corriente = calcular_corriente(voltaje_fuente, resistencia_total)
                corriente_formateada = interpretar_valor_corriente(corriente)
                print(resistencias)
                # Imprime el circuito final, la tolerancia, la corriente y la resistencia total formateada
                print(f"\n(V{voltaje_fuente}) -> {circuito} -> ----(GND)")
                print(f"\nTolerancia de las resistencias: {(tolerancia_resistencias*100):.2f}%")
                print(f"Corriente Resultante: {corriente_formateada}")
                print(f"Resistencia Total: {formatear_valor_resistencia(resistencia_total)}")
                break  # Sale del bucle
            else:
                print("\n-------Debes seleccionar al menos una resistencia--------\n")

        else:
            print("\n-------Opción no válida. Por favor, seleccione una opción válida.-------\n")

construir_circuito()  # Llama a la función para comenzar la construcción del circuito#
