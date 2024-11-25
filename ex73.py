#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados;
# B) Os ultimos 4 colocados da tabela;
# C) Uma lista com os times em ordem alfabética;
# D) Em que posição na tabela está o time do Corinthians
# Criando uma tupla com os 20 primeiros colocados (exemplo)
times = ("Palmeiras", "Flamengo", "Atlético-MG", "Fluminense", "Corinthians", "Internacional", "Athletico-PR", "São Paulo", "Grêmio", "Cruzeiro",
        "Botafogo", "América-MG", "Cuiabá", "Vasco", "Fortaleza", "Santos", "Bragantino", "Coritiba", "Goiás", "Bahia")

# A) Primeiros 5 colocados
primeiros_5 = times[:5]
print("Os 5 primeiros colocados são:", primeiros_5)

# B) Últimos 4 colocados
ultimos_4 = times[-4:]
print("Os últimos 4 colocados são:", ultimos_4)

# C) Times em ordem alfabética
times_alfabetica = sorted(times)
print("Os times em ordem alfabética são:", times_alfabetica)

# D) Posição do Corinthians
posicao_corinthians = times.index("Corinthians") + 1
print("O Corinthians está na posição:", posicao_corinthians)