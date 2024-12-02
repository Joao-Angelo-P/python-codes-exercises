#!/usr/bin/python3
# *args
# uma função para elevar os numeros ao quadrado, mas se for float é para multiplicar por 100
# depois elevar ao quadrado e dividir por 10
# observação: estou contando floats com 1 casa decimal, ex: 1.1

def f_2(*args):

    l = [
         i**2
         if type(i) is not float
         else pow(i, 2)
         for i in args
         ]

	print(l)

f_2() # executa o programa
# pode tirar a condição mas python pode errar a potencia por ser numero quebrado
