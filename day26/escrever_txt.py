def escrever_arquivo(nome_arquivo, conteudo):

    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(conteudo)

    print(f"O conteúdo foi salvo no arquivo: {nome_arquivo}.")

def ler_arquivo(nome_arquivo):

    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
        print(f"Conteúdo do arquivo: {conteudo}.")
    except FileNotFoundError:
        print("O arquivo não foi encontrado, tente novamente.")

def main(nome_arquivo, conteudo):

    escrever_arquivo(nome_arquivo, conteudo)

    ler_arquivo(nome_arquivo)

if __name__ == "__main__":
    arquivo = "exemplo.txt"
    texto = "modificando..."

main(arquivo, texto)