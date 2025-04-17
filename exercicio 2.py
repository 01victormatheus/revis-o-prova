num=int(input("digite um número a partir de 1"))
divisao=num % 2

if num >0:
    if divisao ==0:
        print("este numero é par positivo")
    else:
        print("este número é impar positivo")
else:
    if divisao ==0:
        print("este numero é par negativo")
    else:
        print("este número é impar negativo")


