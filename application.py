import pandas as pd
from pathlib import Path



pd.set_option("display.max_rows", None)

lca_origin = Path.home() / "Downloads" / "arquivo.xlsx"
df = pd.read_excel(lca_origin)
coluna_idplay_origin = df.iloc[:, 19]
# print(coluna_idplay_origin)

lca_verify= ...
df_verify = ...
coluna_idplay_verify = ...
cel_colum_origin = ...
cel_colum_verify = ...
index = 0
jindex = 0
numero_ocorrencias = 0
lista_id_verificado = []

lca_verify = input("Local do arquivo: ")
quantidade_de_linhas = ...

while True:
    jindex = 0
    
    df_verifcation = pd.read_excel(lca_verify)
    quantidade_de_linhas = len(df_verifcation.iloc[:,1])
    cel_colum_origin = df.iloc[index , 19]
    
    if cel_colum_origin not in lista_id_verificado:
        lista_id_verificado.append(cel_colum_verify)
    else:
        continue  
            
    while True:
        cel_colum_verify = df_verifcation.iloc[jindex, 0]
        
        if cel_colum_origin == cel_colum_verify:
            numero_ocorrencias += 1
            
        jindex += 1
        
        if jindex == quantidade_de_linhas:
            break
        
    print(f"Numero de ocorrencias do id {cel_colum_origin} no arquivo 01 = {numero_ocorrencias}" )
    
    index +=1
        
    if index == 1000000:
        break
        
print("programa parou")