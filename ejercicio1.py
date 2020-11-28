#Guardamos en una variable la cantidad de notas que ingresaremos
grades = raw_input("Ingrese cuantas calificaciones desea ingresar al sistema: ")
notas = []
#hacemos un loop para guardar cada nota dentro de un arreglo
for x in range(int(grades)):
  print("Ingrese la nota " + str(x+1) + ":")
  notas.append(int(raw_input("=>")))
promedio = 0.0
#Cada nota la vamos sumando
for x in notas:
  promedio += x
#Se calcula promedio para las notas
promedio = promedio / len(notas)

print("La nota promedio es de: " + str(promedio))