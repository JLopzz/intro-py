print("Calculo de descuentos de Ley")
nombre = raw_input("\n1) Ingrese el nombre de Empleado:\t")
dui = raw_input("\n2) Ingrese el DUI del Empleado:\t")
nit = raw_input("\n3) Ingrese el NIT del Empleado:\t")
sueldo = float(raw_input("\n4) Ingrese su Sueldo Neto:\t"))
extras = raw_input("\n5) Tiene bonos el Empleado? (S/N)\t")
bono = 0
if extras == "S" or extras == 's' : bono = float(raw_input("Ingrese el monto del bono:\t")) 
total = sueldo + bono
afp = total * 0.0725
isss = total * 0.03
neto = total - ( afp + isss )
renta = neto * 0.1
descTotal = afp + isss + renta
liquido = neto - renta
print("\n************Planilla generada************")
print("Nombre:\t" + nombre)
print("DUI:\t" + dui)
print("NIT\t" + nit)
print("\n\tSueldo\tBonos\tAFP\tISSS\tRENTA\tLiquido")
print("\t"+str(round(sueldo,2))+"\t"+str(round(bono,2))+"\t"+str(round(afp,2))+"\t"+str(round(isss,2))+"\t"+str(round(renta,2))+"\t"+str(round(liquido,2)) )
print("\nDescuento Total:\t$" + str(round(descTotal,2)))
print("Pago total a recibir:\t$" + str(round(liquido,2)))