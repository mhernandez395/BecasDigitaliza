'''
******************************************************************

Calculadora
Beca Cisco Digitaliza
Autor: Marvin Hernandez Lopez
Descripcion: Calculadora con funcionalidades aritmeticas basicas.

******************************************************************
'''
def suma(num1,num2):
    return num1 + num2

def resta(num1,num2):
    return num1 - num2

def multiplicacion(num1,num2):
    return num1 * num2

def division(num1,num2):
    try:
        r=num1 / num2
    except ZeroDivisionError:
        r="Error al dividir por 0"
    return r

def exponencial(num1,num2):
    return num1 ** num2

resultado="si"
while resultado!="no":
    print ("""Operaciones:
    Menu
    1) Suma
    2) Resta
    3) Multiplicacion
    4) Division
    5) Exponencial
    6) Salir""")



    while True:
            try:
                opcion=int(input("Selecciona una opcion: "))
                if opcion >= 0 and opcion < 7:
                    break
                else:
                    print("Selecciona una opcion del menu")
            except ValueError:
                print("Opcion incorrecta")

    if opcion == 6:
        print("Saliendo")
        resultado="no"
    else:

        while True:
            try:
                x=int(input("Ingrese el primer numero: "))
                y=int(input("Ingrese el segundo numero: "))
                break
            except ValueError:
                print("Oops!  Introdusca numeros validos.  Intentelo de nuevo...")

        if opcion==1:
            print("La suma es: ", suma(x,y))
        elif opcion==2:
            print("la resta es: ", resta(x,y))
        elif opcion==3:
            print("la multiplicacion es: ", multiplicacion(x,y))
        elif opcion==4:
            print("la division es: ", division(x,y))
        elif opcion==5:
            print("la exponencial es: ",exponencial(x,y))

        resultado=input("Desea realizar un nuevo calculo 'si' o 'no': ")
