# -*- coding: utf-8 -*-

op1 = input("Digite o primeiro operador: ")
op2 = input("Digite o segundo operador: ")
operacao = input("Digite a operação: ")

resultado = None
if operacao == "+":
    resultado = float(op1) + float(op2)
elif operacao == "-":
    resultado = float(op1) - float(op2)
elif operacao == "*":
    resultado = float(op1) * float(op2)
elif operacao == "/":
    resultado = float(op1) / float(op2)
else:
    print("Operação inválida!")

if resultado:
    print("Resultado: {0}".format(resultado))