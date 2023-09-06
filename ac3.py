#1.

salario = float(input('Salário da pessoa: '))

if (salario <= 280):
    percentual = 20
elif (salario <= 700):
    percentual = 15
elif (salario <= 1500):
    percentual = 10
else:
    percentual = 5

    print('Salario original: R$ ', salario)
    print('Percentual: ',percentual,'%')

    percentual = percentual/100.0
    aumento = percentual * salario
    novo_salario = salario + aumento

    print('Aumento: R$ ',aumento)
    print('Novo salário: R$ ', novo_salario)


#2.

dia_semana = int(input('Digite um número de (1 a 7): '))

if dia_semana == 1:
    print('-> Segunda')

elif dia_semana == 2:
    print('-> Terça')

elif dia_semana == 3:
    print('-> Quarta')

elif dia_semana == 4:
    print('-> Quinta')

elif dia_semana == 5:
    print('-> Sexta')

elif dia_semana == 6:
    print('-> Sabado')

elif dia_semana == 7:
    print('-> Domingo')

else:
    print('Dia não encontrado.')



#3.

import math

print('Equaçao do 2o grau da forma: ax² + bx + c')

a = int( input('Coeficiente a: ') )

if(a==0):
        print('Se a=0, não é equação do segundo grau. Tchau')
else:
        b = int( input('Coeficiente b: ') )
        c = int( input('Coeficiente c: ') )
        delta = b*b - (4*a*c)

        if delta<0:
            print('Delta menor que 0. Raízes imaginárias.')
        elif delta==0:
            raiz = -b / (2*a)
            print('Delta=0 , raiz = ',raiz)
        else:
            raiz1 = (-b + math.sqrt(delta) ) / (2*a)
            raiz2 = (-b - math.sqrt(delta) ) / (2*a)
            print('Raizes: ',raiz1,' e ',raiz2)
