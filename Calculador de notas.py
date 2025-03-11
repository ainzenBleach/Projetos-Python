#Uso de operadores de condição (if, else e elif)
nota1 = float(input("Informe o valor da primeira nota entre 1 a 10:"))
nota2 = float(input("Informe o valor da segunda  nota entre 1 a 10:"))

media = (nota1 + nota2)/2

if media > 7.0:
    print("Você passou com %.1f pontos, parabéns!!!!" %media)
elif media > 5.0:
    print("Você passou por um triz com %.1f pontos, tome cuidado e estude!!!!" %media)
else:
    print("Você reprovou com %.1f pontos, estude e boa sorte na proxima" %media)