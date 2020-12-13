def aguiAnual(years):
  if years > 0 and years < 3 : return 0.5
  elif years > 3 and years < 10 : return 0.6333
  elif years > 10 : return 0.7

def aguiMensual(meses):
  if meses > 0 and meses < 12:
    res = ( 0.5 / 12 ) * meses
    return res
  elif meses > 12 and meses < 36: return 0.5
  elif meses > 36 and meses < 120: return 0.6333
  elif meses > 120: return 0.7

def aguiDiario(dias):
  por = 0.5 / ( 12 * 30 )
  res = por * dias
  return res

print("Calculo de descuentos de Ley")
nombre = raw_input("\n1) Ingrese el nombre de Empleado:\t")
dui = raw_input("\n2) Ingrese el DUI del Empleado:\t\t")
nit = raw_input("\n3) Ingrese el NIT del Empleado:\t\t")
sueldo = float(raw_input("\n4) Ingrese su Sueldo Neto:\t\t"))
tiempo = raw_input("\n5) Seleccione la unidad de tiempo en la cual ha trabajado: \n\t(A 'anhos'|M 'meses'|D 'dias')")
time = 0
aguinaldo = 0.0
cant = ""
if tiempo == "A" or tiempo == 'a':
  time = int(raw_input("Ingrese la cantidad de anhos que ha trabajado: "))
  porAgui = aguiAnual(time)
  aguinaldo = sueldo * porAgui
  cant = "anhos"
elif tiempo == "M" or tiempo == 'm':
  time = int(raw_input("Ingrese la cantidad de meses que ha trabajado: "))
  porAgui = aguiMensual(time)
  aguinaldo = sueldo * porAgui
  cant = "meses"
elif tiempo == "D" or tiempo == 'd':
  time = int(raw_input("Ingrese la cantidad de dias que ha trabajado: "))
  porAgui = aguiDiario(time)
  aguinaldo = sueldo * porAgui
  cant = "dias"
else: print("Opcion incorrecta, intente nuevamente")

print("\n************Pago de Aguinaldo************")
print("Nombre:\t" + nombre)
print("DUI:\t" + dui)
print("NIT\t" + nit)
print("cantidad de " + cant + " laborados: " + str(time))

print("\nSueldo Total:\t$" + str(round(sueldo,2)))
print("Aguinaldo total a recibir:\t$" + str(round(aguinaldo,2)))