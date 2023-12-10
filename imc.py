# Resolução de IMC em Python 


peso = float(input("Digite o seu peso em Kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Peso ideal (Parabéns)")
elif 24.9 <= imc < 29.9:
    print("Levemente acima do peso")
elif 29.9 <= imc < 34.9:
    print("Obesidade grau I")
elif 34.9 <= imc < 39.9:
    print("Obesidade grau II (severa)")
else:
    print("IMC obesidade grau III (móbida)")