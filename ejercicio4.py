print("Calculo del tiempo de desplazamiento")
print("Se necesita saber la velocidad a la que se mueve y la distancia que recorrera!")
speed = float(raw_input("Ingrese la Velocidad en Metros sobre Segundos (m/s): "))
dist = float(raw_input("Ingrese la Distancia a recorrer en Metros (m): "))
time = dist / speed
print("\nEl tiempo que se demorara en llegar a su destino es de: " + str(time) + " Segundos")