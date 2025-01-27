import pandas as pd
import regex as re

def limpa_df(df:pd.DataFrame) -> pd.DataFrame:
    """
        Esta função limpa o csv: 
        concert_tours_by_women.csv.
    """    

    df.drop_duplicates(inplace=True)

    # Retira Peak, All Time Peak, Ref.
    df.drop(['Peak', 'All Time Peak', 'Ref.'], 
            axis=1, inplace=True
    )

    # Transforma as colunas Actual gross,
    # Adjusted gross e Average gross em float.
    df['Actual gross'] = df['Actual gross'].str.replace(r"[^\d]", "", regex=True).astype(float)
    df['Adjusted gross (in 2022 dollars)'] = df['Adjusted gross (in 2022 dollars)'].str.replace(r"[^\d]", "", regex=True).astype(float)
    df['Average gross'] = df['Average gross'].str.replace(r"[^\d]", "", regex=True).astype(float)
    
    # Cria as colunas Start Year\End Year
    df['Start Year'] = df['Year(s)'].str[0:4].astype(int)
    df['End Year'] = df['Year(s)'].str[-4::1].astype(int)
    df.drop(['Year(s)'] , axis=1, inplace=True)

    return df

if __name__ == "__main__":
    df = pd.read_csv("concert_tours_by_women.csv")
    df = limpa_df(df)
    df.to_csv("/share/csv_limpo.csv",index=False)