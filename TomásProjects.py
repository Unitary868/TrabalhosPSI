# ============================
# Gerador de SIGLAS FORTES
# ============================

# Palavras fracas que não entram na sigla
palavras_fracas = ["de", "do", "da", "dos", "das", "e"]

# Ler a frase (string)
frase = input("Introduz uma frase: ")

# Separar a frase em palavras
palavras = frase.split()

# String vazia para a sigla
sigla = ""

# Construção da sigla
for palavra in palavras:
    # Converter a palavra para minúsculas para comparar
    palavra_minuscula = palavra.lower()

    # Verificar se NÃO é palavra fraca
    if palavra_minuscula not in palavras_fracas:
        sigla += palavra[0]   # primeira letra da palavra

# Converter a sigla para maiúsculas
sigla = sigla.upper()

# Mostrar o resultado
print("Sigla forte:", sigla)