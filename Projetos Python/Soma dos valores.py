#criando um codigo que soma seus valores colocado

qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor para somar:"))

while (valor > 0.0):
    soma = soma + valor
    qtd = qtd + 1
    print(soma)
    valor = float(input("Digite um valor para somar:"))
    

#O codigo pegara os valores ate ele ser menor que 0, ao ser menor que zero o codigo para e mostra a soma, quantidade de números digitados e a media dos valores
media = soma / qtd
print("\n Total da soma:", soma)
print("\n Quantidade de valores digitados:", qtd)
print("\n Media dos valores:", media)