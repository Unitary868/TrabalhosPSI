print("=== MENU ===")
print("1 - Criar sigla")
print("2 - Quiz de siglas GPSI")

opcao = input("Escolhe uma opção: ")

if opcao == "1":
    frase = input("Escreve uma frase: ")

    palavras = frase.split()
    sigla = ""

    if len(palavras) >= 4:
        for p in palavras:
            sigla += p[0].upper()

    elif len(palavras) == 3:
        sigla += palavras[0][0:2].upper()
        sigla += palavras[1][0].upper()
        sigla += palavras[2][0].upper()

    elif len(palavras) == 2:
        sigla += palavras[0][0:2].upper()
        sigla += palavras[1][0:2].upper()

    else:
        sigla = palavras[0][0:3].upper()

    print("Sigla criada:", sigla)

elif opcao == "2":
    pontos = 0

    print("QUIZ – SIGLAS DO CURSO GPSI")

    print("1) O que significa GPSI?")
    print("a) Gestão de Programas e Sistemas Informáticos")
    print("b) Gestão e Programação de Sistemas Informáticos")
    r = input("Resposta: ")
    if r == "b":
        print("Correto")
        pontos += 1
    else:
        print("Errado (correta: b)")

    print("2) O que significa CPU?")
    print("a) Central Processing Unit")
    print("b) Computer Power Usage")
    r = input("Resposta: ")
    if r == "a":
        print("Correto")
        pontos += 1
    else:
        print("Errado (correta: a)")

    print("3) O que significa RAM?")
    print("a) Random Access Memory")
    print("b) Read Access Machine")
    r = input("Resposta: ")
    if r == "a":
        print("Correto")
        pontos += 1
    else:
        print("Errado (correta: a)")

    print("4) O que significa ROM?")
    print("a) Read Only Memory")
    print("b) Random Only Memory")
    r = input("Resposta: ")
    if r == "a":
        print("Correto")
        pontos += 1
    else:
        print("Errado (correta: a)")

    print("5) O que significa GPU?")
    print("a) General Power Unit")
    print("b) Graphics Processing Unit")
    r = input("Resposta: ")
    if r == "b":
        print("Correto")
        pontos += 1
    else:
        print("Errado (correta: b)")

    print("6) O que significa OS?")
    print("a) Operating System")
    print("b) Open Software")
    r = input("Resposta: ")
    if r == "a":
        print("Correto")
        pontos += 1
    else:
        print("Errado (correta: a)")

    print("7) O que significa LAN?")
    print("a) Local Area Network")
    print("b) Large Access Network")
    r = input("Resposta: ")
    if r == "a":
        print("Correto")
        pontos += 1
    else:
        print("Errado (correta: a)")

    print("8) O que significa WAN?")
    print("a) Web Access Node")
    print("b) Wide Area Network")
    r = input("Resposta: ")
    if r == "b":
        print("Correto")
        pontos += 1
    else:
        print("Errado (correta: b)")

    print("9) O que significa IDE?")
    print("a) Integrated Development Environment")
    print("b) Internet Data Engine")
    r = input("Resposta: ")
    if r == "a":
        print("Correto")
        pontos += 1
    else:
        print("Errado (correta: a)")

    print("10) O que significa SQL?")
    print("a) Structured Query Language")
    print("b) System Question Logic")
    r = input("Resposta: ")
    if r == "a":
        print("Correto")
        pontos += 1
    else:
        print("Errado (correta: a)")

    print("Pontuação final:", pontos, "/ 10")

else:
    print("Opção inválida")
