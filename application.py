import pandas as pd
from pathlib import Path

pd.set_option("display.max_rows", None)


# print(coluna_idplay_origin)

lca_verify= ...
df_verify = []
cel_colum_origin = ...
cel_colum_verify = ...
index = 0
jindex = 0
numero_ocorrencias = 0
lista_id_verificado = []
total_linhas_csv = 0
verif_index = 0
quantidade_de_linhas = ...
coluna_arquivo_xlsx = ...
coluna_arquivo_csv = ...

def comparador():
    
    lca_verify = input("Local do arquivo: ")
    
    while True:
    
        
        jindex = 0
    
        cel_colum_origin = df.iloc[index, coluna_arquivo_xlsx]
    
        if cel_colum_origin in lista_id_verificado:
            continue
    
        for parte in pd.read_csv(lca_verify, sep=";", chunksize=500_000):
            total_linhas_csv += len(parte)
        
            while True:
            
                cel_colum_verify = int(parte.iloc[jindex, coluna_arquivo_csv])
        
                if cel_colum_origin == cel_colum_verify:
                    numero_ocorrencias += 1
                    lista_id_verificado.append(cel_colum_origin)
        
                jindex += 1
                verif_index += 1;
                if jindex == 500_000 or verif_index == total_linhas_csv:
                    jindex = 0
                    break
        
            print(f"Foram verificadas: {total_linhas_csv}")
     
        print(f"\n\nTotal de linhas verificadas: {total_linhas_csv}")
        print(f"Numero de ocorrencias do id: {cel_colum_origin} no arquivo 1 = {numero_ocorrencias}\n\n")
    
        index+=1
        total_linhas_csv = 0
        numero_ocorrencias = 0
        verif_index = 0
  
        if index == len(df):
            break
    

data_arquivo = ...   
tipo_arquivo = ...

print("_______________ | Comparador | _______________\n\n")
print("[1] ID Movel com CSV")
print("[2] ID Fixa com CSV")
print("[0] Sair do programa")

while True:
    try:
        opc_menu = int(input("\nDigite a opção: "))
        break
    except ValueError:
        print("Valor invalido")
        
if opc_menu == 1:
    tipo_arquivo = "Movel"
    
    while True:
        try:
            lca_origin = Path(input("Local do arquivo origem: "))
            coluna_arquivo_xlsx = int(input("Digite a coluna do Excel que você deseja verificar: "))
            coluna_arquivo_csv = int(input("Digite a coluna do CSV que você deseja comparar: "))
            df = pd.read_excel(lca_origin)
            data_arquivo = input("\nEscreva o mês a varificar: ")
            break
        except ValueError:
            print("Digitou valores incorretos: ")
            continue

    comparador()    
    
    
    
elif opc_menu == 2:
    tipo_arquivo = "Fixa"
    
    while True:
        try:
            lca_origin = Path(input("Local do arquivo origem: "))
            coluna_arquivo_xlsx = int(input("Digite a coluna do Excel que você deseja verificar: "))
            coluna_arquivo_csv = int(input("Digite a coluna do CSV que você deseja comparar: "))
            df = pd.read_excel(lca_origin)
            data_arquivo = input("\nEscreva o mês a varificar: ")
            break
        except ValueError:
            print("Digitou valores incorretos: ")
            continue
    
    comparador()    
    
else:
    raise SystemExit("\n\nSaindo do programa. . .")