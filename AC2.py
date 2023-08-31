#1.
valor_hora = float(input("Digite o valor ganho por hora de trabalho: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas neste mês: "))
pagamento = valor_hora * horas_trabalhadas
print("Você trabalhou por",horas_trabalhadas,"horas.")
print("O valor da hora trabalhada é de R$",valor_hora)
print("O pagamento que deve ser recebido é de: R$",pagamento)



#2.
n1 = int(input('1o Número inteiro: '))
n2 = int(input('2o Número inteiro: '))
n3 = float(input('Número real: '))

print ('Soma:', ((2*n1) * (n2/2)))
print ('Produto:', (3 * n1) + n3)
print ('Cubo:', n3**3)



#3.
def calcular_resultados(num1, num2, num3):
    resultado1 = (2 * num1) * (0.5 * num2)
    resultado2 = (3 * num1) + num3
    resultado3 = num3 ** 3

    return resultado1, resultado2, resultado3

num1 = 10
num2 = 20
num3 = 7

resultado1, resultado2, resultado3 = calcular_resultados(num1, num2, num3)

print(f"O produto do dobro do primeiro com metade do segundo é: {resultado1}")
print(f"A soma do triplo do primeiro com o terceiro é: {resultado2}")
print(f"O terceiro elevado ao cubo é: {resultado3}")




#4.
ano = int(input("ano:"))
bissexto = ano % 4 == 0 and \
(ano % 100 != 0 or ano % 400 ==0)
print ("é bissexto: " , bissexto)



