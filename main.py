import random

# ------- DADOS (listas = arrays) -------
numeros = []
nomes = []
idades = []
notas = []
pontos = []

# FALTAS por tipo
faltas_j = []   # justificadas
faltas_i = []   # injustificadas
faltas_d = []   # disciplinares

presencas = []  # cada item é uma lista: ["2026-02-08:P", "2026-02-09:F:I"]  (I/J/D)


# ------- METER ALUNOS (29) + IDADES -------
idade_especial_num = [2, 4, 6, 7, 9, 12, 13, 17, 18, 21, 24, 26, 27]
idade_especial_val = [16, 17, 16, 17, 16, 16, 16, 16, 16, 17, 17, 16, 16]

seed_nomes = [
    "Abel Miranda",
    "Alexandre Recha",
    "Bernardo",
    "Carlos Silva",
    "Carlos Tavares",
    "chioma",
    "Daniel Correia",
    "David",
    "Diego Freitas",
    "Dinis",
    "Diogo Fernandes",
    "Gonçalo",
    "Guilherme",
    "Heloísa",
    "João Pedro",
    "Juliana",
    "Lucas Andrade",
    "Lucas Santos",
    "Luis",
    "Martim Botelho",
    "Martim Nereu",
    "Miguel",
    "Mohamad Ahmed",
    "Rafael Machiné",
    "Rodrigo Cardoso",
    "Ryan Tavares",
    "Taumaturgo",
    "Tomás",
    "Vinícius",
]

for i in range(len(seed_nomes)):
    num = i + 1
    nome = seed_nomes[i]

    idade = 15
    for j in range(len(idade_especial_num)):
        if idade_especial_num[j] == num:
            idade = idade_especial_val[j]

    numeros.append(num)
    nomes.append(nome)
    idades.append(idade)
    notas.append("")
    pontos.append(0)

    faltas_j.append(0)
    faltas_i.append(0)
    faltas_d.append(0)

    presencas.append([])


# ------- FUNÇÕES -------
def procurar_indice_por_numero(num):
    for i in range(len(numeros)):
        if numeros[i] == num:
            return i
    return -1


def faltas_total(i):
    return faltas_j[i] + faltas_i[i] + faltas_d[i]


# ------- INPUTS SEGUROS (sem crash) -------
def ler_int(msg):
    txt = input(msg).strip()
    if txt == "" or txt.isdigit() == False:
        return None
    return int(txt)


def ler_int_ou_vazio(msg):
    txt = input(msg).strip()
    if txt == "":
        return ""
    if txt.isdigit() == False:
        return None
    return int(txt)


def ler_float_nota_ou_vazio(msg):
    txt = input(msg).strip()
    if txt == "":
        return ""
    # aceitar 12,5 ou 12.5
    txt2 = txt.replace(",", ".")
    ok = True
    pontos_count = 0
    for ch in txt2:
        if ch == ".":
            pontos_count += 1
        elif ch.isdigit() == False:
            ok = False
    if ok == False or pontos_count > 1:
        return None
    return txt  # guardamos como string original


def listar_alunos():
    if len(numeros) == 0:
        print("Sem alunos.")
        return

    print("\nNº | Nome | Idade | Nota | F.J | F.I | F.D | Total | Pontos")
    for i in range(len(numeros)):
        print(
            str(numeros[i]).rjust(2),
            "|",
            nomes[i],
            "|",
            idades[i],
            "|",
            (notas[i] if notas[i] != "" else "-"),
            "|",
            str(faltas_j[i]).rjust(2),
            "|",
            str(faltas_i[i]).rjust(2),
            "|",
            str(faltas_d[i]).rjust(2),
            "|",
            str(faltas_total(i)).rjust(2),
            "|",
            pontos[i]
        )


def adicionar_aluno():
    num = ler_int("Nº (apenas números): ")
    if num is None:
        print("Número inválido.")
        return

    if procurar_indice_por_numero(num) != -1:
        print("Já existe esse número.")
        return

    nome = input("Nome: ").strip()
    if nome == "":
        print("Nome vazio.")
        return

    idade = ler_int("Idade (número): ")
    if idade is None:
        print("Idade inválida.")
        return

    nota = ler_float_nota_ou_vazio("Nota (ou vazio): ")
    if nota is None:
        print("Nota inválida.")
        return

    numeros.append(num)
    nomes.append(nome)
    idades.append(idade)
    notas.append(nota)
    pontos.append(0)

    faltas_j.append(0)
    faltas_i.append(0)
    faltas_d.append(0)

    presencas.append([])

    print("Aluno adicionado.")


def atualizar_aluno():
    num = ler_int("Nº do aluno a atualizar: ")
    if num is None:
        print("Número inválido.")
        return

    i = procurar_indice_por_numero(num)
    if i == -1:
        print("Não existe esse aluno.")
        return

    print("Deixa vazio para manter igual.")
    novo_nome = input("Novo nome: ").strip()
    nova_idade = ler_int_ou_vazio("Nova idade: ")
    nova_nota = ler_float_nota_ou_vazio("Nova nota: ")

    if novo_nome != "":
        nomes[i] = novo_nome

    if nova_idade is None:
        print("Idade inválida.")
        return
    if nova_idade != "":
        idades[i] = nova_idade

    if nova_nota is None:
        print("Nota inválida.")
        return
    if nova_nota != "":
        notas[i] = nova_nota

    print("Aluno atualizado.")


def remover_aluno():
    num = ler_int("Nº do aluno a remover: ")
    if num is None:
        print("Número inválido.")
        return

    i = procurar_indice_por_numero(num)
    if i == -1:
        print("Não existe esse aluno.")
        return

    conf = input("Confirmas? (s/n): ").strip()
    if conf.lower() != "s":
        print("Cancelado.")
        return

    numeros.pop(i)
    nomes.pop(i)
    idades.pop(i)
    notas.pop(i)
    pontos.pop(i)

    faltas_j.pop(i)
    faltas_i.pop(i)
    faltas_d.pop(i)

    presencas.pop(i)

    print("Aluno removido.")


def pontos_aluno():
    num = ler_int("Nº do aluno: ")
    if num is None:
        print("Número inválido.")
        return

    i = procurar_indice_por_numero(num)
    if i == -1:
        print("Não existe.")
        return

    txt = input("Quantos pontos? (ex: 1 ou -1): ").strip()
    if txt == "":
        print("Vazio.")
        return

    # validar inteiro com sinal
    if txt[0] == "-":
        if txt[1:].isdigit() == False:
            print("Valor inválido.")
            return
    else:
        if txt.isdigit() == False:
            print("Valor inválido.")
            return

    delta = int(txt)
    pontos[i] = pontos[i] + delta
    print("Pontos atualizados:", pontos[i])


# --------- PRESENÇAS + FALTAS POR TIPO ----------
def marcar_presenca():
    num = ler_int("Nº do aluno: ")
    if num is None:
        print("Número inválido.")
        return

    i = procurar_indice_por_numero(num)
    if i == -1:
        print("Não existe.")
        return

    data = input("Data (YYYY-MM-DD): ").strip()
    if data == "":
        print("Data vazia.")
        return

    estado = input("P ou F (ou vazio para limpar): ").strip().upper()
    if estado != "P" and estado != "F" and estado != "":
        print("Estado inválido. Usa P, F ou vazio.")
        return

    tipo = ""  # I/J/D
    if estado == "F":
        print("Tipo de falta:")
        print("I - Injustificada")
        print("J - Justificada")
        print("D - Disciplinar")
        tipo = input("Escolhe (I/J/D): ").strip().upper()
        if tipo != "I" and tipo != "J" and tipo != "D":
            print("Tipo inválido. Use I, J ou D.")
            return

    # procurar se já existe essa data
    idx_data = -1
    for k in range(len(presencas[i])):
        if presencas[i][k].startswith(data + ":"):
            idx_data = k

    # descobrir o registo anterior (para ajustar contadores)
    anterior_estado = ""
    anterior_tipo = ""
    if idx_data != -1:
        partes = presencas[i][idx_data].split(":")
        # "data:P" ou "data:F:I"
        if len(partes) >= 2:
            anterior_estado = partes[1]
        if len(partes) >= 3:
            anterior_tipo = partes[2]

    # 1) retirar efeito do anterior, se era F
    if anterior_estado == "F":
        if anterior_tipo == "J" and faltas_j[i] > 0:
            faltas_j[i] = faltas_j[i] - 1
        if anterior_tipo == "I" and faltas_i[i] > 0:
            faltas_i[i] = faltas_i[i] - 1
        if anterior_tipo == "D" and faltas_d[i] > 0:
            faltas_d[i] = faltas_d[i] - 1

    # 2) aplicar novo estado (ou limpar)
    if estado == "":
        if idx_data != -1:
            presencas[i].pop(idx_data)
        print("Registo limpo.")
        return

    if estado == "P":
        reg = data + ":P"
    else:
        reg = data + ":F:" + tipo

    if idx_data == -1:
        presencas[i].append(reg)
    else:
        presencas[i][idx_data] = reg

    # 3) aplicar efeito do novo, se for F
    if estado == "F":
        if tipo == "J":
            faltas_j[i] = faltas_j[i] + 1
        if tipo == "I":
            faltas_i[i] = faltas_i[i] + 1
        if tipo == "D":
            faltas_d[i] = faltas_d[i] + 1

    print("Presença marcada.")


def ver_presencas():
    num = ler_int("Nº do aluno: ")
    if num is None:
        print("Número inválido.")
        return

    i = procurar_indice_por_numero(num)
    if i == -1:
        print("Não existe.")
        return

    print("\nPresenças de", nomes[i])
    if len(presencas[i]) == 0:
        print("(sem registos)")
        return

    for k in range(len(presencas[i])):
        print("-", presencas[i][k])


# ------- PLANTA (MELHORADA) -------
def plano_lugares_2_por_mesa():
    rows = ler_int("Linhas (mesas): ")
    if rows is None or rows <= 0:
        print("Valor inválido.")
        return

    cols = ler_int("Colunas (mesas): ")
    if cols is None or cols <= 0:
        print("Valor inválido.")
        return

    lista = []
    for i in range(len(nomes)):
        lista.append(nomes[i])

    random.shuffle(lista)

    largura = 14

    print("\n================== QUADRO (FRENTE) ==================\n")

    i = 0
    for r in range(rows):
        linha1 = ""
        linha2 = ""

        for c in range(cols):
            if i < len(lista):
                a1 = lista[i]
                i += 1
            else:
                a1 = ""

            if i < len(lista):
                a2 = lista[i]
                i += 1
            else:
                a2 = ""

            a1 = a1[:largura]
            a2 = a2[:largura]

            while len(a1) < largura:
                a1 = a1 + " "
            while len(a2) < largura:
                a2 = a2 + " "

            linha1 = linha1 + "[" + a1 + "] "
            linha2 = linha2 + "[" + a2 + "] "

        print(linha1)
        print(linha2)
        print("")

    print("Legenda: cada mesa tem 2 lugares (linha de cima + linha de baixo).")


# ------- RELATÓRIO DA TURMA (MELHORADO) -------
def relatorio_turma():
    total = len(numeros)
    if total == 0:
        print("Sem alunos.")
        return

    # somas
    soma_idades = 0
    soma_pontos = 0
    soma_fj = 0
    soma_fi = 0
    soma_fd = 0

    # notas (só contam as preenchidas)
    soma_notas = 0.0
    conta_notas = 0
    min_nota = 9999.0
    max_nota = -9999.0

    # distribuição de idades (sem dicionários: 2 listas paralelas)
    idades_val = []
    idades_qtd = []

    for i in range(total):
        soma_idades = soma_idades + idades[i]
        soma_pontos = soma_pontos + pontos[i]
        soma_fj = soma_fj + faltas_j[i]
        soma_fi = soma_fi + faltas_i[i]
        soma_fd = soma_fd + faltas_d[i]

        # distribuição idades
        achou = False
        for k in range(len(idades_val)):
            if idades_val[k] == idades[i]:
                idades_qtd[k] = idades_qtd[k] + 1
                achou = True
        if achou == False:
            idades_val.append(idades[i])
            idades_qtd.append(1)

        # notas
        if notas[i] != "":
            n = float(notas[i].replace(",", "."))
            soma_notas = soma_notas + n
            conta_notas = conta_notas + 1
            if n < min_nota:
                min_nota = n
            if n > max_nota:
                max_nota = n

    media_idade = soma_idades / total
    media_pontos = soma_pontos / total

    faltas_totais = soma_fj + soma_fi + soma_fd
    media_faltas = faltas_totais / total

    # percentagens de faltas por tipo
    perc_j = 0
    perc_i = 0
    perc_d = 0
    if faltas_totais > 0:
        perc_j = (soma_fj * 100) / faltas_totais
        perc_i = (soma_fi * 100) / faltas_totais
        perc_d = (soma_fd * 100) / faltas_totais

    # risco: injustificadas >= 5 OU disciplinares >= 1 OU nota < 9.5 (se existir)
    risco = 0
    for i in range(total):
        em_risco = False

        if faltas_i[i] >= 5:
            em_risco = True
        if faltas_d[i] >= 1:
            em_risco = True

        if notas[i] != "":
            n = float(notas[i].replace(",", "."))
            if n < 9.5:
                em_risco = True

        if em_risco == True:
            risco = risco + 1

    print("\n=========== RELATÓRIO DA TURMA ===========")
    print("Total de alunos:", total)
    print("Média de idades:", round(media_idade, 2))
    print("Distribuição de idades:")

    # ordenar idades_val (selection sort)
    for a in range(len(idades_val)):
        pos_min = a
        for b in range(a + 1, len(idades_val)):
            if idades_val[b] < idades_val[pos_min]:
                pos_min = b
        tmp = idades_val[a]
        idades_val[a] = idades_val[pos_min]
        idades_val[pos_min] = tmp

        tmp = idades_qtd[a]
        idades_qtd[a] = idades_qtd[pos_min]
        idades_qtd[pos_min] = tmp

    for k in range(len(idades_val)):
        print("-", idades_val[k], "anos:", idades_qtd[k])

    print("\nPontos totais:", soma_pontos, "| Média pontos/aluno:", round(media_pontos, 2))

    print("\nFaltas totais:", faltas_totais, "| Média faltas/aluno:", round(media_faltas, 2))
    print("  - Justificadas:", soma_fj, f"({round(perc_j, 1)}%)")
    print("  - Injustificadas:", soma_fi, f"({round(perc_i, 1)}%)")
    print("  - Disciplinares:", soma_fd, f"({round(perc_d, 1)}%)")

    if conta_notas > 0:
        media_nota = soma_notas / conta_notas
        print("\nNotas registadas:", conta_notas, "/", total)
        print("Média notas:", round(media_nota, 2), "| Min:", round(min_nota, 2), "| Max:", round(max_nota, 2))
    else:
        print("\nNotas registadas: 0")

    print("\nAlunos em risco:", risco, "/", total)

    # -------- TOPS MELHORADOS (com desempate por número) --------
    print("\nTop 5 faltas totais:")
    usados = []
    for t in range(5):
        best_i = -1
        best_val = -1
        for i in range(total):
            ja = False
            for u in range(len(usados)):
                if usados[u] == i:
                    ja = True
            if ja == False:
                v = faltas_total(i)
                if v > best_val:
                    best_val = v
                    best_i = i
                elif v == best_val and best_i != -1:
                    if numeros[i] < numeros[best_i]:
                        best_i = i

        if best_i != -1:
            usados.append(best_i)
            print(
                "-", "Nº", numeros[best_i], nomes[best_i],
                "| Total:", best_val,
                "| J:", faltas_j[best_i],
                "I:", faltas_i[best_i],
                "D:", faltas_d[best_i]
            )

    print("\nTop 5 faltas INJUSTIFICADAS:")
    usados = []
    for t in range(5):
        best_i = -1
        best_val = -1
        for i in range(total):
            ja = False
            for u in range(len(usados)):
                if usados[u] == i:
                    ja = True
            if ja == False:
                v = faltas_i[i]
                if v > best_val:
                    best_val = v
                    best_i = i
                elif v == best_val and best_i != -1:
                    if numeros[i] < numeros[best_i]:
                        best_i = i

        if best_i != -1:
            usados.append(best_i)
            print("-", "Nº", numeros[best_i], nomes[best_i], "=>", best_val)

    print("\nTop 5 pontos:")
    usados = []
    for t in range(5):
        best_i = -1
        best_val = -999999
        for i in range(total):
            ja = False
            for u in range(len(usados)):
                if usados[u] == i:
                    ja = True
            if ja == False:
                v = pontos[i]
                if v > best_val:
                    best_val = v
                    best_i = i
                elif v == best_val and best_i != -1:
                    if numeros[i] < numeros[best_i]:
                        best_i = i

        if best_i != -1:
            usados.append(best_i)
            print("-", "Nº", numeros[best_i], nomes[best_i], "=>", best_val)

    if conta_notas > 0:
        print("\nTop 5 notas:")
        usados = []
        for t in range(5):
            best_i = -1
            best_val = -1.0
            for i in range(total):
                ja = False
                for u in range(len(usados)):
                    if usados[u] == i:
                        ja = True
                if ja == False and notas[i] != "":
                    v = float(notas[i].replace(",", "."))
                    if v > best_val:
                        best_val = v
                        best_i = i
                    elif v == best_val and best_i != -1:
                        if numeros[i] < numeros[best_i]:
                            best_i = i

            if best_i != -1:
                usados.append(best_i)
                print("-", "Nº", numeros[best_i], nomes[best_i], "=>", round(best_val, 2))

    print("=========================================")


# ------- MENU -------
while True:
    print("\n--- Gestor de Turma (MATÉRIA) ---")
    print("1 - Listar alunos")
    print("2 - Adicionar aluno")
    print("3 - Atualizar aluno")
    print("4 - Remover aluno")
    print("5 - Alterar pontos (+/-)")
    print("6 - Marcar presença (P/F + tipo de falta)")
    print("7 - Ver presenças de um aluno")
    print("8 - Planta da sala (2 por mesa)")
    print("9 - Relatório da turma")
    print("0 - Sair")

    op = input("Opção: ").strip()

    if op == "1":
        listar_alunos()
    elif op == "2":
        adicionar_aluno()
    elif op == "3":
        atualizar_aluno()
    elif op == "4":
        remover_aluno()
    elif op == "5":
        pontos_aluno()
    elif op == "6":
        marcar_presenca()
    elif op == "7":
        ver_presencas()
    elif op == "8":
        plano_lugares_2_por_mesa()
    elif op == "9":
        relatorio_turma()
    elif op == "0":
        print("Adeus.")
        break
    else:
        print("Opção inválida.")
