
uf_com_ddds = (
    ("Acre", 68),
    ("Alagoas", 82),
    ("Amapá", 96),
    ("Tocantins", 63),
    ("Amazonas", 92),
    ("Bahia", 71),
    ("Ceará", 85),
    ("Maranhão", 98),
    ("Paraíba", 83),
    ("Pernambuco", 81),
    ("Piauí", 86),
    ("Rio Grande do Norte", 84),
    ("Sergipe", 79),
    ("Espírito Santo", 27),
    ("Minas Gerais", 31),
    ("Rio de Janeiro", 21),
    ("São Paulo", 11),
    ("Paraná", 41),
    ("Rio Grande do Sul", 51),
    ("Santa Catarina", 48)
)



def adicionar_estado(estado, ddd):
    global uf_com_ddds
    uf_com_ddds += ((estado, ddd),)

def remover_estado(estado):
    global uf_com_ddds
    uf_com_ddds = tuple(item for item in uf_com_ddds if item[0] != estado)

def listar_estados():
    print("Estados e seus DDDs:")
    for estado, ddd in uf_com_ddds:
        print(f"{estado}: {ddd}")

while True:
    print("\nOpções:")
    print("1. Adicionar estado")
    print("2. Remover estado")
    print("3. Listar estados")
    print("4. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        novo_estado = input("Digite o nome do novo estado: ")
        novo_ddd = int(input("Digite o DDD do novo estado: "))
        adicionar_estado(novo_estado, novo_ddd)
        print(f"Estado {novo_estado} adicionado com sucesso!")
    elif opcao == "2":
        estado_remover = input("Digite o nome do estado a ser removido: ")
        remover_estado(estado_remover)
        print(f"Estado {estado_remover} removido com sucesso!")
    elif opcao == "3":
        listar_estados()
    elif opcao == "4":
        print("Encerrando o programa. Até mais!")
        break
    else:
        print("Opção inválida. Digite um número de 1 a 4.")

# Agora o programa permite adicionar, remover e listar estados.
