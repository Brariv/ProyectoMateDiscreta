
def main():
    opt = 0
    conjuntos = {"Universo": ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9"]}

    while(opt != 3):
        print("Opciones: ")
        print("1. Construir Conjunto")
        print("2. Operar Conjunto")
        print("3. Salir")

        while True:
            opt = input("Ingrese una opción: ")
            try :
                opt = int(opt)
                break
            except ValueError:
                print("Opción no válida")
                continue


        if opt == 1:
            conjuntos.update(construir_conjunto(conjuntos["Universo"]))
            
            
            
        elif opt == 2:
            print("Operar Conjunto")
            print ("Conjuntos Disponibles: ")
            for key in conjuntos:
                print(key)

            print("Operaciones: ")
            print("1. Complemento")
            print("2. Unión")
            print("3. Intersección")
            print("4. Diferencia")
            print("5. Diferencia Simétrica")
            print("6. Cancelar")

            while True:
                operacion = input("Ingrese la operación: ")
                try :
                    operacion = int(operacion)
                    break
                except ValueError:
                    print("Opción no válida")
                    continue
            
            if operacion == 1:
                print("Complemento")
                conjunto = input("Ingrese el conjunto a operar: ")
                print("Conjunto", conjunto, ":", conjuntos[conjunto])
                print("Complemento:", complemento(conjuntos["Universo"], conjuntos[conjunto]))
            elif operacion == 2:
                print("Unión")
                conjunto1 = input("Ingrese el primer conjunto a operar: ")
                conjunto2 = input("Ingrese el segundo conjunto a operar: ")
                print("Conjunto", conjunto1, ":", conjuntos[conjunto1])
                print("Conjunto", conjunto2, ":", conjuntos[conjunto2])
                print("Unión:", union(conjuntos[conjunto1], conjuntos[conjunto2]))
            elif operacion == 3:
                print("Intersección")
                conjunto1 = input("Ingrese el primer conjunto a operar: ")
                conjunto2 = input("Ingrese el segundo conjunto a operar: ")
                print("Conjunto", conjunto1, ":", conjuntos[conjunto1])
                print("Conjunto", conjunto2, ":", conjuntos[conjunto2])
                print("Intersección:", interseccion(conjuntos[conjunto1], conjuntos[conjunto2]))
            elif operacion == 4:
                print("Diferencia")
                conjunto1 = input("Ingrese el primer conjunto a operar: ")
                conjunto2 = input("Ingrese el segundo conjunto a operar: ")
                print("Conjunto", conjunto1, ":", conjuntos[conjunto1])
                print("Conjunto", conjunto2, ":", conjuntos[conjunto2])
                print("Diferencia:", diferencia(conjuntos[conjunto1], conjuntos[conjunto2]))
            elif operacion == 5:
                print("Diferencia Simétrica")
                conjunto1 = input("Ingrese el primer conjunto a operar: ")
                conjunto2 = input("Ingrese el segundo conjunto a operar: ")
                print("Conjunto", conjunto1, ":", conjuntos[conjunto1])
                print("Conjunto", conjunto2, ":", conjuntos[conjunto2])
                print("Diferencia Simétrica:", diferencia_simetrica(conjuntos[conjunto1], conjuntos[conjunto2]))
            elif operacion == 6:
                print("Cancelar")

                continue


        elif opt == 3:
            print("Salir")
        else:
            print("Opción no válida")
        

def construir_conjunto(conjunto):
    print("Construir Nuevo Conjunto")
    Conjunto = []
    Nombre = input("Ingrese el nombre del conjunto: ")
    print("Ingrese los elementos del conjunto: ")
    while True:
        Elemento = input("Elemento [Enter para salir]: ")
        if Elemento == "":
            print("Conjunto", Nombre, ":", Conjunto)
            print("Conjunto Finalizado")
            break

        if Elemento in conjunto:
            Conjunto.append(Elemento)
        else:
            print("Elemento Fuera del Universo")
    return {Nombre: Conjunto}

    
def complemento(universo, conjunto):
    return [elemento for elemento in universo if elemento not in conjunto]

def union(conjunto1, conjunto2):
    return conjunto1 + [elemento for elemento in conjunto2 if elemento not in conjunto1]

def interseccion(conjunto1, conjunto2):
    return [elemento for elemento in conjunto1 if elemento in conjunto2]

def diferencia(conjunto1, conjunto2):
    return [elemento for elemento in conjunto1 if elemento not in conjunto2]

def diferencia_simetrica(conjunto1, conjunto2):
    return diferencia(conjunto1, conjunto2) + diferencia(conjunto2, conjunto1)


main()