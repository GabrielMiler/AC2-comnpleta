#Input
ano = int(input("Informe o ano: "))

#Conta
anocerto = (ano % 4 == 0 and ano %  100 != 0 or ano % 400 == 0)

#Variavél
reposta = "O ano informado é bissexto" if  anocerto else " O ano informado não é bissexto"

#Prints
print(reposta)
