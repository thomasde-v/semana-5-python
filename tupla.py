tupla = (1,2,3,4,5)

#primeiro indiceda tupla
print (tupla[0])

for lista in tupla:
  print ("tupla: ", lista)

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)



# Criando a tupla com as UFs e seus respectivos DDDs
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
    "Sergipe": 79,
    "Tocantins": 63
}

# Listando todas as UFs com DDDs
for estado, ddd in uf_com_ddds.items():
    print(f"{estado} (DDD {ddd})")


