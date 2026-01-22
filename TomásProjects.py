import random

historico = []

def criar_sigla(frase):
    palavras = frase.split()
    sigla = ""

    if len(palavras) >= 4:
        for p in palavras:
            sigla = sigla + p[0].upper()
    elif len(palavras) == 3:
        sigla = palavras[0][0:2].upper()
        sigla = sigla + palavras[1][0].upper()
        sigla = sigla + palavras[2][0].upper()
    elif len(palavras) == 2:
        sigla = palavras[0][0:2].upper()
        sigla = sigla + palavras[1][0:2].upper()
    else:
        sigla = palavras[0][0:3].upper()

    return sigla


def gerar_password():
    total = int(input("Quantas palavras (2 a 10)? "))

    if total < 2 or total > 10:
        print("Numero invalido")
        return

    palavras = []

    for i in range(1, total + 1):
        palavra = input("Escreve a palavra " + str(i) + ": ")
        palavras.append(palavra)

    base = ""
    for p in palavras:
        base = base + p[0].upper()

    numeros = "0123456789"
    password = base + random.choice(numeros)

    historico.append(password)
    if len(historico) > 5:
        historico.pop(0)

    print("Password criada:", password)


def quiz():
    pontos = 0

    print("QUIZ DE SIGLAS")

    print("1) O que significa GPSI?")
    print("a) Gestão de Programas e Sistemas Informáticos")
    print("b) Gestão e Programação de Sistemas Informáticos")
    r = input("Resposta: ")
    if r == "b":
        pontos = pontos + 1

    print("2) O que significa CPU?")
    print("a) Central Processing Unit")
    print("b) Computer Power Usage")
    r = input("Resposta: ")
    if r == "a":
        pontos = pontos + 1

    print("3) O que significa RAM?")
    print("a) Random Access Memory")
    print("b) Read Access Machine")
    r = input("Resposta: ")
    if r == "a":
        pontos = pontos + 1

    print("4) O que significa ROM?")
    print("a) Read Only Memory")
    print("b) Random Only Memory")
    r = input("Resposta: ")
    if r == "a":
        pontos = pontos + 1

    print("5) O que significa GPU?")
    print("a) General Power Unit")
    print("b) Graphics Processing Unit")
    r = input("Resposta: ")
    if r == "b":
        pontos = pontos + 1

    print("6) O que significa OS?")
    print("a) Operating System")
    print("b) Open Software")
    r = input("Resposta: ")
    if r == "a":
        pontos = pontos + 1

    print("7) O que significa LAN?")
    print("a) Local Area Network")
    print("b) Large Access Network")
    r = input("Resposta: ")
    if r == "a":
        pontos = pontos + 1

    print("8) O que significa WAN?")
    print("a) Web Access Node")
    print("b) Wide Area Network")
    r = input("Resposta: ")
    if r == "b":
        pontos = pontos + 1

    print("9) O que significa IDE?")
    print("a) Integrated Development Environment")
    print("b) Internet Data Engine")
    r = input("Resposta: ")
    if r == "a":
        pontos = pontos + 1

    print("10) O que significa SQL?")
    print("a) Structured Query Language")
    print("b) System Question Logic")
    r = input("Resposta: ")
    if r == "a":
        pontos = pontos + 1

    print("11) O que significa HTML?")
    print("a) HyperText Markup Language")
    print("b) High Text Machine Language")
    r = input("Resposta: ")
    if r == "a":
        pontos = pontos + 1

    print("12) O que significa HTTP?")
    print("a) HyperText Transfer Protocol")
    print("b) High Transmission Text Program")
    r = input("Resposta: ")
    if r == "a":
        pontos = pontos + 1

    print("13) O que significa USB?")
    print("a) Universal Serial Bus")
    print("b) United System Board")
    r = input("Resposta: ")
    if r == "a":
        pontos = pontos + 1

    print("14) O que significa IP?")
    print("a) Internet Protocol")
    print("b) Internal Program")
    r = input("Resposta: ")
    if r == "a":
        pontos = pontos + 1

    print("15) O que significa AI?")
    print("a) Artificial Intelligence")
    print("b) Automatic Internet")
    r = input("Resposta: ")
    if r == "a":
        pontos = pontos + 1

    print("Pontuacao final:", pontos, "/ 15")


while True:
    print("=== MENU ===")
    print("1 - Criar sigla")
    print("2 - Gerar password")
    print("3 - Quiz")
    print("4 - Ver historico")
    print("0 - Sair")

    opcao = input("Escolhe uma opcao: ")

    if opcao == "1":
        frase = input("Escreve uma frase: ")
        print("Sigla:", criar_sigla(frase))

    elif opcao == "2":
        gerar_password()

    elif opcao == "3":
        quiz()

    elif opcao == "4":
        print("Historico:")
        if len(historico) == 0:
            print("Vazio")
        else:
            for pw in historico:
                print("-", pw)

    elif opcao == "0":
        print("A sair...")
        break

    else:
        print("Opcao invalida")
