passWord = "nueva contra"
cont = True
while cont == True:
  newPass = raw_input("Ingrese el password para continuar: ")
  if newPass == passWord :
    print("\nBienvenido al Sistema, puede continuar...\n")
    break
  res = raw_input("\nPassword incorrecto, desea continuar? (S[si] / N[no])")
  if res == "S" or res == "s": continue
  else: cont = False