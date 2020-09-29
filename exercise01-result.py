listaRegistro = []
mensaje = print("Bienvenido, ya puede agregar registros")
print(" ")
respuesta = input("¿Desea agregar un registro? (Si/No): ")
print(" ")
costoTotal = 0

while respuesta == "Si":
    cliente = input("nombre del cliente: ")
    producto = input("producto: ")
    costo = float(input("costo ($0.00): "))
    print(" ")
    costoTotal += costo
    print("El costo total de los productos vendidos es: " + str(costoTotal))
    print(" ")
    respuesta = input("¿Desea agregar un registro? (Si/No): ")
    print(" ")
    
    
    # punto de programa
    # registro = {"cliente": cliente, "producto": producto, "costo": costo}
    registro = dict(cliente=cliente, producto=producto, costo=costo)
    # como agrego un elemento nuevo a una lista?
    listaRegistro.append(registro)
    
    # dejar de ocupar la variable registro
    # registro = None
if respuesta == "No":
    for registro in listaRegistro:
        print(registro)
    print(" ")
    print("El costo total es: " + str(costoTotal))