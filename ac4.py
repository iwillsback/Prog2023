#1.

(num) = int(input ("\nDigite um numero inteiro para saber se é primo: "))
cont = 0
div = []

for i in range(num):

    if num%(i+1) == 0:

        cont += 1
        div.append(i+1)

    else:

        cont


if cont == 2:

    print ("O numero é primo divisivel por ",div)

else:

    print ("O numero não é primo pois é divisivel por ",div)


#2.

valor_da_divida = float(input(" dívida: "))
parcelas = 1
juros = 0
print("|Dívida|Juros|Numero de Parcelas|Valor da Parcela|")


while True:
    juros = (5 / 3) * parcelas + 5
    if parcelas == 1:
        juros = 0

    valor_do_juros = valor_da_divida * (juros / 100)
    valor_total = valor_da_divida + valor_do_juros
    valor_da_parcela = valor_total / parcelas
    print(
        f"|R$ {valor_total:.2f}\t"
        f"|R$ {valor_do_juros:.2f}\t"
        f"|{parcelas}\t\t\t"
        f"|R$ {valor_da_parcela:.2f}"
    )
    if parcelas == 1:
        parcelas -= 1
    parcelas += 3
    if parcelas > 12:
        break


#3.

numero = 0
intervalo = [0, 0, 0, 0]
while (numero >= 0):
    numero = int(input("Digite um número: "))
if (numero >= 0):
 if (numero <= 25):
    intervalo[0] = intervalo[0] + 1
 elif (numero <= 51):
    intervalo[1] = intervalo[1] + 1
 elif (numero <= 75):
    intervalo[2] = intervalo[2] + 1
 elif (numero <= 100):
    intervalo[3] = intervalo[3] + 1
print("Números no intervalo [0-25]:", intervalo[0])
print("Números no intervalo [26-50]:", intervalo[1])
print("Números no intervalo [51-75]:", intervalo[2])
print("Números no intervalo [76-100]:", intervalo[3])





