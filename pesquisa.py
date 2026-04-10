# PROJETO: Pesquisa de Satisfação - TudoWeb
# Estrutura de repetição FOR e estruturas de decisão

# Inicializamos os contadores para as respostas
count_excelente = 0
count_ruim = 0

# Definimos o número de entrevistados.

num_entrevistados = 50

print("--- Sistema de Pesquisa TudoWeb ---")
print(f"Total de entrevistados a serem ouvidos: {num_entrevistados}")

# Estrutura de Repetição FOR

for i in range(1, num_entrevistados + 1):
    print(f"\nEntrevistado nº {i}")
    
    # Coleta de dados
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ") # Entradade idade

    # Coleta da opinião com o menu
    print("Por favor, avalie nosso atendimento:")
    print("1: EXCELENTE")
    print("2: BOM")
    print("3: RUIM")
    
    opiniao = input("Sua resposta (1, 2 ou 3): ")

    # Estruturas de Decisão para verificar a opinião
    if opiniao == "1":
        count_excelente += 1 # Soma 1 ao contador de excelente
    elif opiniao == "3":
        count_ruim += 1 # Soma 1 ao contador de ruim
  

# Fim da coleta, exibição dos resultados
print("\n" + "="*40)
print("       RELATÓRIO FINAL DA PESQUISA")
print("="*40)
print(f"a) Quantidade de respostas 'EXCELENTE': {count_excelente}")
print(f"b) Quantidade de respostas 'RUIM':      {count_ruim}")
print("="*40)
print("Obrigado pela participação pesquisa finalizada com sucesso!")
