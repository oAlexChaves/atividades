atividade = str(input("seja bem vindo ao programa da atividade! \n selecione um numero entre 1 á 11 e veja a questão:"))

if atividade == ("1"):
    print("olá mundo")

elif atividade == ("2"):
    a = float(input("adicione um numero: "))
    print("O número informado foi: ", a)

elif atividade == ("3"):
    b = float(input("adicione um numero: "))
    c = float(input("adicione outro numero: "))
    print("a soma deles é:", b + c)

elif atividade == ("4"):
    d = float(input("digite a nota do primeiro bimestre: "))
    e = float(input("digite a nota do segundo bimestre: "))
    f = float(input("digite a nota do terceiro bimestre: "))
    g = float(input("digite a nota do quarto bimestre: "))
    media = ((d + e + f + g)/4)
    print (media)

elif atividade == ("5"):
    h = float(input("qual a distancia em metros:"))
    print (h*100,"cm" )

elif atividade == ("6"):
    j = float(input("qual é o raio do circulo: "))
    area = (j**2*3.14)
    print ("{}".format(area))

elif atividade == ("7"):
    k = float(input("qual o lado do quadrado: "))
    quadrado = k**2
    quadradox2 = quadrado*2
    print (quadrado)
    print (quadradox2)

elif atividade == ("8"):
    vh = float(input("quanto você ganha por hora? "))
    hm = int(input("quantas horas você trabalha por mês? "))
    print ("você ganha ao mês:", vh*hm, "R$")

elif atividade == ("9"):
    l = int(input("digite um numero, positivo ou negativo: "))
    if l > 0:
        print("seu numero é postivo:")
    elif l==0:
        print("seu numero é nulo")
    else:
        print("seu numero é negativo")

elif atividade == ("10"):
    m = str(input("digite (F) se você se identifica com o genero feminino ou (M) se com o genêro masculino: ").upper())
    if m == 'F':
        print("você se identifica com o sexo feminino")
    elif m == 'M':
        print("voce se identifica com o sexo masculino")
    else:
        print("você não selecionou um sexo valido")

elif atividade == ("11"):
    n = str(input("digite uma letra: ").lower())
    if n == 'a' or n == 'b' or n =='i' or n == 'o' or n == 'u':
        print("essa letra é uma vogal")
    else:
        print("essa letra é uma consoante ")

else:
    print("não foi digitado um numero valido reset o programa e selecione um numero valido")