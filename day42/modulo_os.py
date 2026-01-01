import os

diretorio = "./day42"
arquivos_pasta = os.listdir(diretorio)
        
for pastas in arquivos_pasta:
    caminho_completo = os.path.join(diretorio, pastas)
    if os.path.isdir(caminho_completo):
        print(f"Pasta que esta sendo verificada {pastas}")
        print(os.listdir(caminho_completo))


for arquivos in arquivos_pasta:
    caminho_completo = os.path.join(diretorio, arquivos)
    if os.path.isfile(caminho_completo):
       print(f"Verificando os arquivos na pasta {arquivos_pasta}")
       print(arquivos)
