def analisador_lexico(arquivo):
    alfabeto = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_()[]{}:,.<>=+-*/%&|^!~?;\"'\\#\t\n")

    for token in arquivo:
        if token not in alfabeto:
            return False, token
    return True, None

def arquivo(arq):
    print("Tentando abrir o arquivo:", arq)
    with open(arq, 'r') as doc:
        arquivo = doc.read()
    return arquivo

def main():
    nome = input("Digite o nome do arquivo a ser analisado: ")
    parametro = arquivo(nome)

    passou, simbolo = analisador_lexico(parametro)

    if passou:
        print("Sucesso: A entrada está correta.")
    else:
        print(f"Falha: O símbolo '{simbolo}' não está registrado no alfabeto.")

if __name__ == "__main__":
    main()