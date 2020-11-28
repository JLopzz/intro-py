print("Conversiones Disponibles:\n")
print("\t1. Convertir Libras a Kilos")
print("\t2. Convertir Kilos a Libras")
print("\t3. Convertir Euros a Dolares")
print("\t4. Convertir Dolares a Euros")
op = raw_input("Elija la operacion que desea realizar: ")
if op == str(1) :
  print("\nHa escogido la opcion 1.")
  print("\tConvertir Libras a Kilos")
  x = float(raw_input("Ingrese las libras a convertir: "))
  res = round(x * 0.453592, 2)
  print("\nSe han convertido " + str(x) + " libras en " +str(res) + " kilos")

elif op == str(2) :
  print("\nHa escogido la opcion 2.")
  print("\tConvertir Kilos a Libras")
  x = float(raw_input("Ingrese los kilos a convertir: "))
  res = round(x * 2.20462, 2)
  print("\nSe han convertido " + str(x) + " kilos en " +str(res) + " libras")

elif op == str(3) :
  print("\nHa escogido la opcion 3.")
  print("\tConvertir Euros a Dolares")
  x = float(raw_input("Ingrese los Euros a convertir: "))
  res = round(x * 1.2, 2)
  print("\nSe han convertido " + str(x) + " Euros en " +str(res) + " Dolares")

elif op == str(4) :
  print("\nHa escogido la opcion 4.")
  print("\tConvertir Dolares a Euros")
  x = float(raw_input("Ingrese los Dolares a convertir: "))
  res = round(x * 0.84, 2)
  print("\nSe han convertido " + str(x) + " Dolares en " +str(res) + " Euros")

else:
  print("Opcion Incorrecta")