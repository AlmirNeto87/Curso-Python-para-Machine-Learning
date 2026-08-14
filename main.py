
def categorias(nota): 
    if nota <= 1:
        return "Ruim"
    elif 2 <= nota <= 3:
        return "Mediana"
    elif 4 <= nota <= 5:
        return "Boa"


notas_rock = [5, 1, 4, 0, 2, 5, 2, 1, 0, 5, 5, 3, 5, 2, 5, 5, 3, 5, 4, 4]
notas_pop = [3, 2, 5, 1, 2, 1, 4, 1, 5, 0, 4, 2, 1, 2, 5, 2, 4, 4, 0, 1]

classificacao_rock = list(map(categorias, notas_rock))
classificacao_pop = list(map(categorias, notas_pop))

musica_ruim_rock = list(filter(lambda x: x == "Ruim", classificacao_rock))
musica_ruim_pop = list(filter(lambda x: x == "Ruim", classificacao_pop))
musica_mediana_rock = list(filter(lambda x: x == "Mediana", classificacao_rock))
musica_mediana_pop = list(filter(lambda x: x == "Mediana", classificacao_pop))
musica_boa_rock = list(filter(lambda x: x == "Boa", classificacao_rock))
musica_boa_pop = list(filter(lambda x: x == "Boa", classificacao_pop))

musica_ruim_rock = len(musica_ruim_rock)
musica_ruim_pop = len(musica_ruim_pop)
musica_mediana_rock = len(musica_mediana_rock)
musica_mediana_pop = len(musica_mediana_pop) 
musica_boa_rock = len(musica_boa_rock)
musica_boa_pop = len(musica_boa_pop)

classificacao_rock_mediana = list(map(lambda x: x == "Mediana", classificacao_rock))
print(classificacao_rock_mediana)
if any(classificacao_rock_mediana):
    print("Há músicas medianas em rock.")
else:
    print("Não há músicas medianas em rock.")

classificacao_pop_boa = list(map(lambda x: x == "Boa", classificacao_pop))

if all(classificacao_pop_boa):
    print("Todas as músicas de pop são boas.")
else:
    print(" Nem todas as músicas de pop são boas.") 


print("Classificação das notas de rock:", classificacao_rock)
print("Classificação das notas de pop:", classificacao_pop)
print("Músicas ruins de rock:", musica_ruim_rock)
print("Músicas ruins de pop:", musica_ruim_pop)
print("Músicas medianas de rock:", musica_mediana_rock)
print("Músicas medianas de pop:", musica_mediana_pop)
print("Músicas boas de rock:", musica_boa_rock)
print("Músicas boas de pop:", musica_boa_pop)

print(sorted([musica_boa_rock, musica_boa_pop])) 