idade = 18
def check_age(idade):
  if idade < 13:
    print("Criança")
  elif idade < 18:
    return "Adolescente"
  elif idade < 60:
    return "Adulto"
  else:
    return "Idoso"

check_age(10)