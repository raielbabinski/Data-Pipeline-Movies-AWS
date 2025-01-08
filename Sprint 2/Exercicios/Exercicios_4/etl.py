from functools import reduce

with open('actors.csv') as actors:
    '''
        Abre o arquivo .csv, cria uma lista, 
        onde cada linha (registro) é uma nova
        lista de elementos.
    '''
    actors = open('actors.csv')
    list_actors = list(map(lambda actor: actor.strip().split(','), actors))


def etapa_1 (actors):
    '''
        Apresente o ator/atriz com maior número
        de filmes e a respectiva quantidade. 
        A quantidade de filmes encontra-se na coluna 
        Number of movies do arquivo.
    '''
    # Ordena o dataset pela coluna Number of Movies.
    actor = sorted(actors[1:len(actors)], key = lambda movies : int(movies[2]), reverse=True)
    
    with open('etapa-1.txt', 'a') as file:
        file = open('etapa-1.txt', 'a')
        file.writelines(f'O ator(a) com maior quantidade de filmes produzidos foi {actor[0][0]} com {actor[0][2]} filmes\n')


def etapa_2(actors):
    '''
        Apresente a média de receita de 
        bilheteria bruta dos principais 
        filmes, considerando todos os atores. 
        Estamos falando aqui da média da coluna Gross.
    '''
    # Soma todos os elementos da coluna Gross.
    gross_sum = reduce(lambda sum, actor : float(actor[5]) + sum, actors[1:len(actors)], 0)
    media = gross_sum/(len(actors)-1)
    media = round(media, 2)
    
    with open('etapa-2.txt', 'a') as file:
        file = open('etapa-2.txt', 'a')
        file.writelines(f'A receita média de bilheteria dos principais filmes é de {media}\n')


def etapa_3(actors):
    '''
        Apresente o ator/atriz com a maior 
        média de receita de bilheteria bruta 
        por filme do conjunto de dados. Considere 
        a coluna Average per Movie para fins de cálculo.
    '''
    # Ordena o dataset pela coluna Average per Movie.
    actor = sorted(actors[1:len(actors)], key = lambda movies : float(movies[3]), reverse=True)
    
    with open('etapa-3.txt', 'a') as file:
        file = open('etapa-3.txt', 'a')
        file.writelines(f'O ator(a) com maior média de receita por filme é {actor[0][0]}\n')


def etapa_4(actors):
    '''
        A coluna #1 Movie contém o filme de maior 
        bilheteria em que o ator atuou. Realize a 
        contagem de aparições destes filmes no dataset, 
        listando-os ordenados pela quantidade de 
        vezes em que estão presentes. Considere a 
        ordem decrescente e, em segundo nível, o 
        nome do filme.

        Ao escrever no arquivo, considere o padrão de saída:

        (sequência) - O filme (nome do filme) aparece (quantidade) vez(es) no dataset, 
        
        adicionando um resultado a cada linha.
    '''
    # Ordena o dataset pelos nomes dos filmes.
    movies_sorted = sorted(actors[1:len(actors)], key = lambda movies : movies[4])
    
    count_movie = []
    count = 1
    # Percore o dataset, realisando a contagem e o agrupamento dos filmes.
    for i in range(len(movies_sorted)-1):
        if movies_sorted[i][4] != movies_sorted[i+1][4]:
            count_movie.append([movies_sorted[i][4], count])
            count = 1
        else:
            count += 1
    
    # Ordena a nova lista cont_movie, pela quantidade.
    count_movie = sorted(count_movie, key= lambda amt : amt[1], reverse=True)
    
    with open('etapa-4.txt', 'a') as file:
        file = open('etapa-4.txt', 'a')
        i=1
        for movie in count_movie: 
            file.writelines(f'({i}) - O filme {movie[0]} aparece {movie[1]} vez(es) no dataset\n')
            i += 1


def etapa_5(actors):
    '''
        Apresente a lista dos atores ordenada 
        pela receita bruta de bilheteria de 
        seus filmes (coluna Total Gross), em
        ordem decrescente. Ao escrever no
        arquivo, considere o padrão de saída
        (nome do ator) - (receita total bruta),
        adicionando um resultado a cada linha
    '''
    # Ordena o dataset pela coluna Total Gross
    actor = sorted(actors[1:len(actors)], key = lambda movies : movies[1], reverse=True)
    
    with open('etapa-5.txt', 'a') as file:
        file = open('etapa-5.txt', 'a')
        for a in actor: 
            file.writelines(f'{a[0]} - {a[1]}\n')


if __name__ == "__main__":    
    etapa_1(list_actors)
    etapa_2(list_actors)
    etapa_3(list_actors)
    etapa_4(list_actors)
    etapa_5(list_actors)
