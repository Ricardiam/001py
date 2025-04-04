"""usuario ingrese numero y sea tamaño de la lista y acabe con ese numero"""
tamanio_de_lista = int(input("ingrese numero: "))
lista = []
contador = 0
while  len(lista)<tamanio_de_lista :
  num_user = int(input("ingrese numero: "))
  lista.append(num_user)
print(lista)

