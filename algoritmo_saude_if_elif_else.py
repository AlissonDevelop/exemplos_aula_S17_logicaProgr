objetivo = input("Qual é o seu objetivo de saúde (perda de peso, ganho de massa, manter a saúde)? ")

if objetivo == "perda de peso":
    dieta = "Dieta baixa em calorias."
elif objetivo == "ganho de massa":
    dieta = "Alimentos ricos em proteínas."
elif objetivo == "manter a saúde":
    dieta = "Dieta balanceada."
else:
    dieta = "Objetivo desconhecido. Consulte um nutricionista."

print(dieta)