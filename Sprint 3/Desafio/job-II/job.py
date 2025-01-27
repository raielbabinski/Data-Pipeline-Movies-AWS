import pandas as pd
import matplotlib.pyplot as plt

PATH_RESPOSTA = "/share/respostas.txt"

def main():
    df = pd.read_csv("/share/csv_limpo.csv")
    
    q1(df.copy())
    q2(df.copy())
    q3(df.copy())
    q4(df.copy())
    q5(df.copy())

def q1(df:pd.DataFrame):
    # Agrupa as colunas por Artist.
    gb = df.groupby(df['Artist'])
    df_artistas = gb.size().to_frame("qtd")
    
    # Cria qtd usado pra calcular média.
    qtd = max(df_artistas["qtd"])
    
    # Cria lista com as artistas. 
    df_artistas = df_artistas.loc[df_artistas['qtd'] == max(df_artistas["qtd"])]
    artistas_dict = df_artistas.to_dict()
    artistas = list(artistas_dict['qtd'].keys())

    # Cria o dataframe com os valores médos do faturamento.
    df_fat = df.groupby('Artist')['Actual gross'].sum() / qtd

    # Filtra por artista.
    df_fat = df_fat.loc[df_fat.index.isin(artistas)]
    # Filtra por faturamento.
    df_fat = df_fat[df_fat == df_fat.max()]

    # Escreve a resposta no resposta.txt.
    artista = next(iter(df_fat.to_dict().keys()))

    with open(PATH_RESPOSTA, 'a'):
        file = open(PATH_RESPOSTA, 'a')
        file.writelines(f"Q1:\n\n--- {artista}\n\n")


def q2(df:pd.DataFrame):
    # Dataframe com turnês de um ano.
    df = df.loc[df["Start Year"] == df["End Year"]]
    # Seleciona maior "Avarege gross".
    resposta =  df.loc[df['Average gross'] == df['Average gross'].max()]
    # Escreve  a resposta no "resposta.txt".
    with open(PATH_RESPOSTA, 'a'):
        file = open(PATH_RESPOSTA, 'a')
        file.writelines(f"Q2:\n\n--- {resposta['Tour title'].to_string()[5::]}\n\n")


def q3(df:pd.DataFrame):
    # Agrupa artistas e soma a coluna "Adjusted gross".
    df_artist = df.groupby("Artist", as_index=False)["Adjusted gross (in 2022 dollars)"].sum()
    
    # Cria uma nova coluna para quantidade de Turnês e ordena o df.
    df_artist["Shows"] = df.groupby("Artist")['Shows'].sum().to_list()
    df_artist = df_artist.sort_values(
                                [ "Shows", "Adjusted gross (in 2022 dollars)"],
                                ascending= [True, False]
    )
    
    # Armazena o nome das artistas.
    artist = df_artist["Artist"].head(3).to_list()
    tours = df.loc[df["Artist"].isin(artist)][["Tour title", "Artist"]].to_dict()
   
    resposta =f"""Q3:
          
--- Artista:{tours["Artist"][6]}  Tour:{tours["Tour title"][6]}
--- Artista:{tours["Artist"][12]}   Tour:{tours["Tour title"][12]}
--- Artista:{tours["Artist"][18]}        Tour:{tours["Tour title"][18]}

"""

    with open(PATH_RESPOSTA, 'a'):
        file = open(PATH_RESPOSTA, 'a')
        file.writelines(resposta)
        
def q4(df:pd.DataFrame):
    # Agrupa as colunas por Artist.
    gb = df.groupby(df['Artist'])
    df_artistas = gb.size().to_frame("qtd")

    # Cria lista com as artistas. 
    df_artistas = df_artistas.loc[df_artistas['qtd'] == max(df_artistas["qtd"])]
    artistas_dict = df_artistas.to_dict()
    artistas = list(artistas_dict['qtd'].keys())

    # Cria o dataframe que é o somatório do faturamento bruto.
    df_fat = df.groupby('Artist')['Actual gross'].sum()

    # Filtra por artistas
    df_fat = df_fat.loc[df_fat.index.isin(artistas)]
    # Filtra por faturamento.
    df_fat = df_fat[df_fat == df_fat.max()]

    artista = next(iter(df_fat.to_dict().keys()))  
    
    # Cria as listas com o lucro e as tours da artista
    df_tours = df[["Artist", "Tour title", "Actual gross", "Start Year"]]
    df_tours = df_tours.loc[df_tours["Artist"] == artista]
    gross = df_tours["Actual gross"].to_list()
    years = df_tours["Start Year"].to_list()

    # Cria o gráfico.
    plt.plot(years, gross, marker="o", linestyle=":", color="orange", label="Faturamento")

    # Coloca Labels e deixa o gráfico legível.
    plt.title("Faturamento por Ano das Turnês", fontsize=14)
    plt.xlabel("Ano de Início das Turnês", fontsize=12)
    plt.ylabel("Faturamento Bruto - Centenas de Milhões(USD)", fontsize=12)
    plt.xticks(years)  
    plt.legend()
    plt.grid(True, linestyle="-", alpha=0.7)

    # Salva gráfico como png.
    plt.tight_layout()
    plt.savefig("/share/Q4.png", dpi=300)

def q5(df:pd.DataFrame):
    # Filtra os 5 artistas com mais shows
    df = df[["Artist", "Shows"]].groupby("Artist", as_index=False)
    df = df.sum().sort_values(by="Shows", ascending=False).head(5)
    
    artist = df["Artist"]
    shows = df["Shows"]

    plt.bar(artist[::-1], shows[::-1], color="purple", alpha=0.8)

    # Personaliza o gráfico
    plt.title("Quantidade Total de Shows por Artista", fontsize=14)
    plt.xlabel("Artista", fontsize=12)
    plt.ylabel("Quantidade de Shows", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Muda a escala
    plt.ylim(250, max(shows) + 20)

    # Adiciona os valores encima das barras.
    for index, value in enumerate(shows[::-1]):
        plt.text(index, value + 2, str(value), ha="center", fontsize=10)

    # Salva o gráfico como PNG
    plt.savefig("/share/Q5.png", dpi=300)

if __name__ == "__main__":
    main()
