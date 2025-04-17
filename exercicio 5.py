peso=float(input("digite seu peso"))
altura=float(input("digite sua altura"))
imc=peso/(altura*altura)
print(imc)

repetir="sim"
while repetir =="sim":
    if imc < 18.6:
        print("abaixo do peso")
    elif imc >=18.6 and imc <=24.9:
        print("peso ideal,parabéns")
    elif imc >= 25.0 and imc <=29.9:
        print("levemente acima do peso")
    elif imc >= 30.0 and imc <=34.9:
        print("obesidade grau 1")
    elif imc >= 35.0 and imc <=39.9 :
        print("obesidade grau 2,severa")
    elif imc >=40:
        print("obesidade grau 3,morbida")

    repetir = input("quer coninuar verificando?")