def suma (a, b):
    (a + b)

def resta (a, b):
    (a - b)

def multiplicacion (a, b):
    (a * b)

def division (a, b):
   if b==0:
       return "Error: Division por CERO"
   return a / b 

def menu(): 
    print("Welcome, this is the calculator")
    print("1. Sumar(+)")
    print("2. Restar(-)")
    print("3. multiplicar(*)")
    print("4. Dividir(/)")
    print("5. Salir")


if __name__ == "__MAIN__":
    while True:
        menu()
        opcion = input("Elije un numero para hacer la operacion que quieres: ")

        if opcion == "1":
            a = float(input("Digita el primer numero: "))
            b =float(input("Digita el segundo numero:  "))
            print (f"La suma es: {suma(a, b)}")

        elif opcion == "2":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print(f"La resta es: {resta(a, b)}")
        elif opcion == "3":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print(f"La multiplicación es: {multiplicacion(a, b)}")
        elif opcion == "4":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print(f"La división es: {division(a, b)}")
        elif opcion == "5":
            print("Gracias por usar la calculadora.")
            break
        else:
            print("Opción no válida, por favor elige una opción entre 1 y 5.")

