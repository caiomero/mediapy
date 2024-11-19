def media (num1, num2, num3):
    resultado = (num1 + num2 + num3) /3
    return resultado

num1 = float(input('digite o 1º numero:'))
num2 = float(input('digite o 2º numero:'))
num3 = float(input('digite o 3º numero:'))
total = media(num1, num2, num3)
print(f'sua media e {total:.2f}')