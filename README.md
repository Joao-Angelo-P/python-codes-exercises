# python-codes-exercises
Treino mais aprofundando de Python. Carregar códigos Python

## Interactive shell with python file
- Create virtaul environment
```
python3 -m venv .venv
```
- Activated virtaul environment (Linux)
```
source .venv/bin/activate
```
- Deactivated virtaul environment
```
deactivate
```
- Example: **(Should not forget to run in virtual environment activated)**
```
python3 -i ex.py
```
- Run script "ex3.py" for extract data from file(text data)
```
python3 -i ex3.py
>>> arq = 'file_example.txt'
>>> __load__file(arq)
['oi', 'oi2', 'oi3', 'oi4', 'oi5', 'oi6']
```
- No exercício 6(ex6.py), pequena demostração do porquê não usar lista vazia no segmento __init__ de classes/objetos. O mais correto é adicionar um 'default' de 'None' e declarar a lista num 'if'.
