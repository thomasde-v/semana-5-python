# Tupla com os estados e seus DDDs
uf_com_ddds = {
    "Acre": 68, 
    "Alagoas": 82,
    "Amapá": 96,
    "Amazonas": 92,
    "Bahia": 71,
    "Ceará": 85,
    "Distrito Federal": 61,
    "Espírito Santo": 27,
    "Goiás": 62,
    "Maranhão": 98,
    "Mato Grosso": 65,
    "Mato Grosso do Sul": 67,
    "Minas Gerais": 31,
    "Pará": 91,
    "Paraíba": 83,
    "Paraná": 41,
    "Pernambuco": 81,
    "Piauí": 86,
    "Rio de Janeiro": 21,
    "Rio Grande do Norte": 84,
    "Rio Grande do Sul": 51,
    "Rondônia": 69,
    "Roraima": 95,
    "Santa Catarina": 48,
    "São Paulo": 11,
    "Tocantins": 63
}


estado_pesquisado = input("Digite o nome do estado (ex: São Paulo): ")
if estado_pesquisado in uf_com_ddds:
    print(f"O DDD do estado {estado_pesquisado} é {uf_com_ddds[estado_pesquisado]}")
else:
    print("Estado não encontrado na lista.")

def adicionar_estado(estado, ddd):
    global uf_com_ddds
    uf_com_ddds += ((estado, ddd),)

# Exemplo de uso da função:
novo_estado = input("Digite o nome do novo estado: ")
novo_ddd = int(input("Digite o DDD do novo estado: "))

adicionar_estado(novo_estado, novo_ddd)
print(f"Estado {novo_estado} adicionado com sucesso!")
