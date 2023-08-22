
#algoritimo para calcular equações de 2 grau

coeficienteA = float(input("DIGITE O COEFICIENTE A : "))
coeficienteB = float(input("DIGITE O COEFICIENTE B : "))
coeficienteC = float(input("DIGITE O COEFICIENTE C : "))
delta = coeficienteB ** 2-4 * coeficienteA * coeficienteC
raizdedelta = delta ** 0.5
x1 = (- coeficienteB + raizdedelta) / (2 * coeficienteA)
x2 = (- coeficienteB - raizdedelta) / (2 * coeficienteA)
print(" Delta:{}\n Raiz de Delta:{}\n X1:{}\n X2:{}".format(delta, raizdedelta, x1, x2))







ano = int(input("ano:"))
bissexto = ano % 4 == 0 and \
(ano % 100 != 0 or ano % 400 ==0)
print ("é bissexto: " , bissexto)



