
def main():
    opt = 0
    conjuntos = {#Conjuntos Predefinidos y A;macen de Conjuntos
        #Conjunto Universo
        "Universo": ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9"]
        }

    while(opt != 3): #Menu Principal
        print("Opciones: ")
        print("1. Construir Conjunto")
        print("2. Operar Conjunto")
        print("3. Salir")

        while True: #Validar Opción
            opt = input("Ingrese una opción: ")
            try :
                opt = int(opt)
                break
            except ValueError:
                print("Opción no válida")
                continue


        if opt == 1: #Construir Conjunto
            conjuntos.update(construir_conjunto(conjuntos))
            
            
            
        elif opt == 2:#Menu Secundario (Operar Conjunto)
            print("Operar Conjunto")
            

            print("Operaciones: ")
            print("1. Complemento")
            print("2. Unión")
            print("3. Intersección")
            print("4. Diferencia")
            print("5. Diferencia Simétrica")
            print("6. Cancelar")

            while True: #Validar Opción
                operacion = input("Ingrese la operación: ")
                try :
                    operacion = int(operacion)
                    break
                except ValueError:
                    print("Opción no válida")
                    continue

            print ("Conjuntos Disponibles: ")#Mostrar Conjuntos Disponibles
            for key in conjuntos:
                print(key)
            
            if operacion == 1:
                print("Complemento")
                while True: #Validar si el Conjunto Existe
                    conjunto1 = input("Ingrese el conjunto a operar: ").lower()
                    if conjunto1 in conjuntos:
                        break
                    else:
                        print("Conjunto no existe")
                        continue
                print("Conjunto", conjunto1, ":", conjuntos[conjunto1])
                print("Complemento:", complemento(conjuntos["Universo"], conjuntos[conjunto1])) #Mostrar Complemento

            elif operacion == 2:
                print("Unión")
                while True:#Validar si el Conjunto Existe
                    conjunto1 = input("Ingrese el primer conjunto a operar: ").lower()
                    if conjunto1 in conjuntos:
                        break
                    else:
                        print("Conjunto no existe")
                        continue
                while True:#Validar si el Conjunto Existe
                    conjunto2 = input("Ingrese el segundo conjunto a operar: ").lower()
                    if conjunto2 in conjuntos:
                        break
                    else:
                        print("Conjunto no existe")
                        continue
                print("Conjunto", conjunto1, ":", conjuntos[conjunto1])
                print("Conjunto", conjunto2, ":", conjuntos[conjunto2])
                print("Unión:", union(conjuntos[conjunto1], conjuntos[conjunto2])) #Mostrar Unión

            elif operacion == 3:
                print("Intersección")
                while True:#Validar si el Conjunto Existe
                    conjunto1 = input("Ingrese el primer conjunto a operar: ").lower()
                    if conjunto1 in conjuntos:
                        break
                    else:
                        print("Conjunto no existe")
                        continue
                while True:#Validar si el Conjunto Existe
                    conjunto2 = input("Ingrese el segundo conjunto a operar: ").lower()
                    if conjunto2 in conjuntos:
                        break
                    else:
                        print("Conjunto no existe")
                        continue
                print("Conjunto", conjunto1, ":", conjuntos[conjunto1])
                print("Conjunto", conjunto2, ":", conjuntos[conjunto2])
                print("Intersección:", interseccion(conjuntos[conjunto1], conjuntos[conjunto2])) #Mostrar Intersección

            elif operacion == 4:
                print("Diferencia")
                while True:#Validar si el Conjunto Existe
                    conjunto1 = input("Ingrese el primer conjunto a operar: ").lower()
                    if conjunto1 in conjuntos:
                        break
                    else:
                        print("Conjunto no existe")
                        continue
                while True:#Validar si el Conjunto Existe
                    conjunto2 = input("Ingrese el segundo conjunto a operar: ").lower()
                    if conjunto2 in conjuntos:
                        break
                    else:
                        print("Conjunto no existe")
                        continue
                print("Conjunto", conjunto1, ":", conjuntos[conjunto1])
                print("Conjunto", conjunto2, ":", conjuntos[conjunto2])
                print("Diferencia:", diferencia(conjuntos[conjunto1], conjuntos[conjunto2])) #Mostrar Diferencia

            elif operacion == 5:
                print("Diferencia Simétrica")
                while True:#Validar si el Conjunto Existe
                    conjunto1 = input("Ingrese el primer conjunto a operar: ").lower()
                    if conjunto1 in conjuntos:
                        break
                    else:
                        print("Conjunto no existe")
                        continue
                while True:#Validar si el Conjunto Existe
                    conjunto2 = input("Ingrese el segundo conjunto a operar: ").lower()
                    if conjunto2 in conjuntos:
                        break
                    else:
                        print("Conjunto no existe")
                        continue
                print("Conjunto", conjunto1, ":", conjuntos[conjunto1])
                print("Conjunto", conjunto2, ":", conjuntos[conjunto2])
                print("Diferencia Simétrica:", diferencia_simetrica(conjuntos[conjunto1], conjuntos[conjunto2])) #Mostrar Diferencia Simétrica
            elif operacion == 6: #Cancelar
                print("Cancelar")

                continue


        elif opt == 3: #Salir
            print("Saliendo...")
        else:
            print("Opción no válida")
        

def construir_conjunto(conjunto): #Construir Conjunto
    print("Construir Nuevo Conjunto")
    Conjunto = []
    while True: #Validar Nombre si el Nombre no Existe
        Nombre = input("Ingrese el nombre del conjunto: ")
        if Nombre in conjunto:
            print("Conjunto ya existe")
        else:
            break

    print("Ingrese los elementos del conjunto: ")
    while True: #Ingresar Elementos
        Elemento = input("Elemento [Enter para salir]: ")
        if Elemento == "": #Salir si presiona Enter
            print("Conjunto", Nombre, ":", Conjunto)
            print("Conjunto Finalizado")
            break

        if Elemento in Conjunto: #Validar si el Elemento no Esta Repetido
            print("Elemento ya existe")

        if Elemento in conjunto["Universo"]: #Validar si el Elemento esta en el Universo
            Conjunto.append(Elemento)
        else:
            print("Elemento Fuera del Universo")
    return {Nombre.lower(): Conjunto}

    
def complemento(universo, conjunto):
    return [elemento for elemento in universo if elemento not in conjunto] #Complemento

def union(conjunto1, conjunto2):
    return conjunto1 + [elemento for elemento in conjunto2 if elemento not in conjunto1] #Unión

def interseccion(conjunto1, conjunto2):
    return [elemento for elemento in conjunto1 if elemento in conjunto2] #Intersección

def diferencia(conjunto1, conjunto2):
    return [elemento for elemento in conjunto1 if elemento not in conjunto2]    #Diferencia 

def diferencia_simetrica(conjunto1, conjunto2):
    return diferencia(conjunto1, conjunto2) + diferencia(conjunto2, conjunto1) #Diferencia Simétrica


main()