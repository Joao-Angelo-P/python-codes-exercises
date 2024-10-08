# treinando "List Comprehension" ou listcomps
# quebra de linhas são ignoradas dentro de {}, [], ()



a = [
	x + 1
	for x in range(10)
] # [1, 2, 3, 4, 5, 6, , 7, 8, 9, 10]

b = {
	x + 1
	for x in range(10)
} # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

c = (
	x + 1
	for x in range(10)
) # precisa iterar o objeto. loop for: for i in c: print(i)

d = [
	(lambda x, y: x * y**2)(x, y)
for x in range(5)
							for y in range(10)                 ]


