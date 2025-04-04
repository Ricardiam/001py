a = int(input("Ingresa un número: "))  # Solicita un número al usuario
if a > 5:
    print("El número ingresado es mayor a 5, no se ejecutará el bucle.")
else:
    while a <= 5:
        print(a)  # Imprime el valor actual
        a = a - 1  # Incrementa en 1
        