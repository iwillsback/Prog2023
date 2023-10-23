#1

def imprimir_linhas(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

while True:
    n_str = input("valor de n:")
    if n_str.isdigit():
        n = int(n_str)
        imprimir_linhas(n)
        break

#2

def achaTamanho(x):
    a = str(x)
    if len(a) > 1:
        if a[0] == '0':
            return len(a) - 1
        else:
            return len(a)
    return len(a)


num = int(input("Digite um número: "))
print(achaTamanho(num))

#3

try:
    num1 = int(input("1 numero: "))
    num2 = int(input("2 numero: "))
    resultado = num1 / num2
except ValueError:
    print("Erro: Numero inteiro INVALIDO.")
except ZeroDivisionError:
    print("Erro: Nao pode dividir por ZERO.")
else:
    print(f"divisão de {num1} por {num2} é: {resultado:.2f}")
finally:
    print(resultado)
