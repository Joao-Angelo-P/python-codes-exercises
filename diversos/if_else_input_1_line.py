print(f'{nome} | {sobrenome}') if (bool(nome:=input()), bool(sobrenome:=input())) == (True, True) else print('Digitou nada') # uma linha para receber input criar um bloco de condicional e imprimir
print('teste') if False else [[1 if not True else 2] for i in range(1) if True][0][0] # if_else aninhado e um if_else dentro de um listcomp
