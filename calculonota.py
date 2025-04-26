# Cadastro de Alunos de Algoritmos de Programação, Projetos e Computação

# Lista para armazenar todos os alunos
lista_alunos = []

# Pergunta quantos alunos serão cadastrados
quantidade_alunos = int(input("Quantos alunos deseja cadastrar? "))

# Cadastro de cada aluno
for i in range(quantidade_alunos):
    print(f"\nDigite os dados do {i+1}° aluno:")
    nome_aluno = input("Nome: ")
    nota_teorica_1 = float(input("Nota da prova teórica 1 (T1): "))
    nota_teorica_2 = float(input("Nota da prova teórica 2 (T2): "))
    nota_projeto_1 = float(input("Nota do projeto 1 (P1): "))
    nota_projeto_2 = float(input("Nota do projeto 2 (P2): "))

    # Cálculo das médias
    media_teorica = 0.4 * nota_teorica_1 + 0.6 * nota_teorica_2
    media_pratica = (nota_projeto_1 + nota_projeto_2) / 2

    if media_teorica > 5.0 and media_pratica > 5.0:
        media_final = 0.3 * media_pratica + 0.7 * media_teorica
    else:
        media_final = min(media_teorica, media_pratica)

    # Cadastro completo do aluno
    dados_aluno = [nome_aluno, [nota_teorica_1, nota_teorica_2], [nota_projeto_1, nota_projeto_2], [media_teorica, media_pratica], media_final]
    lista_alunos.append(dados_aluno)

# Função para exibir o menu
def exibir_menu():
    print("\n--- MENU ---")
    print("1. Exibir boletim de todos os alunos")
    print("2. Consultar aluno pelo nome")
    print("3. Mostrar aluno com maior média final")
    print("4. Mostrar aluno com menor média final")
    print("5. Mostrar percentual de alunos com média final superior a 5.0")
    print("0. Sair")

# Primeira exibição do menu
exibir_menu()
opcao_menu = input("Escolha uma opção: ")

# Laço principal enquanto a opção for diferente de "0"
while opcao_menu != "0":
    if opcao_menu == "1":
        print("\n--- Boletim de Alunos ---")
        for aluno in lista_alunos:
            print(f"Nome: {aluno[0]}")
            print(f"Média Teórica (MT): {aluno[3][0]:.2f}")
            print(f"Média Prática (MP): {aluno[3][1]:.2f}")
            print(f"Média Final (MF): {aluno[4]:.2f}")
            print("-" * 30)

    elif opcao_menu == "2":
        nome_pesquisado = input("Digite o nome do aluno para consultar: ")
        lista_resultado = [aluno for aluno in lista_alunos if aluno[0].lower() == nome_pesquisado.lower()]
        
        if len(lista_resultado) > 0:
            aluno = lista_resultado[0]
            print(f"\nNome: {aluno[0]}")
            print(f"Notas Teóricas: {aluno[1]}")
            print(f"Notas de Projetos: {aluno[2]}")
            print(f"Média Teórica (MT): {aluno[3][0]:.2f}")
            print(f"Média Prática (MP): {aluno[3][1]:.2f}")
            print(f"Média Final (MF): {aluno[4]:.2f}")
        else:
            print("Aluno não encontrado.")

    elif opcao_menu == "3":
        aluno_maior_media = max(lista_alunos, key=lambda x: x[4])
        print(f"Aluno com maior média final: {aluno_maior_media[0]} - MF: {aluno_maior_media[4]:.2f}")

    elif opcao_menu == "4":
        aluno_menor_media = min(lista_alunos, key=lambda x: x[4])
        print(f"Aluno com menor média final: {aluno_menor_media[0]} - MF: {aluno_menor_media[4]:.2f}")

    elif opcao_menu == "5":
        alunos_acima_5 = [aluno for aluno in lista_alunos if aluno[4] > 5.0]
        percentual_acima_5 = (len(alunos_acima_5) / len(lista_alunos)) * 100
        print(f"Percentual de alunos com média final acima de 5.0: {percentual_acima_5:.2f}%")

    else:
        print("Opção inválida. Tente novamente.")

    # Mostra o menu de novo
    exibir_menu()
    opcao_menu = input("Escolha uma opção: ")

print("Encerrando o programa.")
