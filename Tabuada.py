# Criação das variáveis para atribuir os valores
num = int(input("Digite um número:"))
multi = 0
'''
Utilizei o while para gerar um lista até o multi parar de ser menor ou igual a 10
No print utilizamos o 'f' dentro do print e antes das "" para mostrarmos o valor da variável
dentro das {}. 
'''
while multi <= 10:
    print(f"{num} x {multi} =", num * multi)
    multi = multi + 1