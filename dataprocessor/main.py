clientes = [
    {
        "id": 1,
        "nome": "João Silva",
        "email": "joao.silva@email.com",
        "idade": 34,
        "cidade": "Joinville",
        "data_cadastro": "2023-01-10",
    },
    {
        "id": 2,
        "nome": "Maria Souza",
        "email": "maria@email",
        "idade": 28,
        "cidade": "Florianopolis",
        "data_cadastro": "2023-02-15",
    },
    {
        "id": 3,
        "nome": "Carlos Pereira",
        "email": "carlos.pereira@email.com",
        "idade": -5,
        "cidade": "Curitiba",
        "data_cadastro": "2023-03-20",
    },
    {
        "id": 4,
        "nome": "Ana Lima",
        "email": "ana.lima@email.com",
        "idade": 45,
        "cidade": "Joinville",
        "data_cadastro": "2023-01-25",
    },
    {
        "id": 5,
        "nome": "Pedro Santos",
        "email": "",
        "idade": 38,
        "cidade": "Sao Paulo",
        "data_cadastro": "2023-02-30",
    },
]

print(f"DataProcessor iniciado — {len(clientes)} clientes carregados.")

## Aula 01
print("\n\n")
print("###   Aula 01")
print("## Desafio guiado:")
cidades = {}
for cliente in clientes:
    cidade = cliente.get("cidade", "N/A")
    if cidades.get(cidade):
        cidades[cidade] += 1
    else:
        cidades[cidade] = 1

for cidade in cidades:
    print(f"{str(cidade)}: {cidades[cidade]} clientes")

print("\n## Desafio extra:")
cidade_clientes = {}
for cliente in clientes:
    cidade = cliente.get("cidade", "N/A")
    if cidade_clientes.get(cidade):
        cidade_clientes[cidade]["contagem"] += 1
        (cidade_clientes[cidade]["clientes"]).append(cliente["nome"])

    else:
        cidade_clientes[cidade] = {
            "contagem": 1,
            "clientes": [cliente["nome"]],
        }

for cidade in cidade_clientes:
    print(
        cidade,
        f"{str(cidade)} ({cidade_clientes[cidade]['contagem']}): {', '.join(cidade_clientes[cidade]['clientes'])}",
    )

## Aula 02
print("\n\n\n")
print("###   Aula 02")

transacoes = [
    {
        "id": 1,
        "cliente_id": 1,
        "valor": 150.50,
        "categoria": "eletronicos",
        "data": "2023-05-10",
        "status": "aprovado",
    },
    {
        "id": 2,
        "cliente_id": 2,
        "valor": 200.00,
        "categoria": "roupas",
        "data": "2023-05-11",
        "status": "pendente",
    },
    {
        "id": 3,
        "cliente_id": 3,
        "valor": -50.00,
        "categoria": "alimentacao",
        "data": "2023-05-12",
        "status": "aprovado",
    },
    {
        "id": 4,
        "cliente_id": 1,
        "valor": 300.00,
        "categoria": "eletronicos",
        "data": "2023-05-13",
        "status": "recusado",
    },
    {
        "id": 5,
        "cliente_id": 10,
        "valor": 120.00,
        "categoria": "livros",
        "data": "2023-05-14",
        "status": "aprovado",
    },
]

from processador import media_idade, extremos_idade, contar_por_cidade

media = media_idade(clientes)
minimo, maximo = extremos_idade(clientes)

print(f"Clientes carregados: {len(clientes)}")
print(f"Média de idade: {media:.1f}")
print(f"Faixa de idade: {minimo} – {maximo}")
print()
print("Clientes por cidade:")
for cidade, total in contar_por_cidade(clientes).items():
    print(f"  {cidade}: {total}")

print("\n## Desafio guiado:")
print(f"Média de idade: {round(media, 1)}")
print(
    f"Mais novo: {(list(filter(lambda cliente: cliente['idade'] == minimo, clientes))[0]).get('nome')} ({minimo})"
)
print(
    f"Mais novo: {(list(filter(lambda cliente: cliente['idade'] == maximo, clientes))[0]).get('nome')} ({maximo})"
)

print("\n## Desafio extra:")
transacoes_validas = [
    transacao
    for transacao in transacoes
    if transacao["cliente_id"] in [cliente["id"] for cliente in clientes if cliente]
    and transacao["valor"] > 0
    and transacao["status"] == "aprovado"
]

cliente_valor = {}

for transacao in transacoes_validas:
    if cliente_valor.get(transacao["cliente_id"]):
        cliente_valor[transacao["cliente_id"]] += transacao["valor"]
    else:
        cliente_valor[transacao["cliente_id"]] = transacao["valor"]

mapa_nomes = {cliente["id"]: cliente["nome"] for cliente in clientes}

ranking_ordenado = sorted(cliente_valor.items(), key=lambda item: item[1], reverse=True)

for index, (cliente_id, valor) in enumerate(ranking_ordenado, 1):
    nome_cliente = mapa_nomes[cliente_id]
    print(f"{index}. {nome_cliente} — R$ {valor:.2f}")

print("\n## Exercícios")
print("# 01:")
vendas = [
    {"produto": "Notebook", "categoria": "Eletrônicos", "valor": 3000},
    {"produto": "Smartphone", "categoria": "Eletrônicos", "valor": 1500},
    {"produto": "Cadeira", "categoria": "Móveis", "valor": 500},
    {"produto": "Mesa", "categoria": "Móveis", "valor": 1200},
    {"produto": "Fone de Ouvido", "categoria": "Eletrônicos", "valor": 200},
    {"produto": "Monitor", "categoria": "Eletrônicos", "valor": 950},
    {"produto": "Teclado", "categoria": "Eletrônicos", "valor": 180},
    {"produto": "Sofá", "categoria": "Móveis", "valor": 2300},
    {"produto": "Estante", "categoria": "Móveis", "valor": 800},
    {"produto": "Impressora", "categoria": "Eletrônicos", "valor": 650},
]

categorias = {}
for venda in vendas:
    if not categorias.get(venda["categoria"]):
        categorias[venda["categoria"]] = {
            "Valor": venda["valor"],
            "Produtos": [venda["produto"]],
        }
    else:
        categorias[venda["categoria"]]["Valor"] += venda["valor"]
        categorias[venda["categoria"]]["Produtos"].append(venda["produto"])

for categoria in categorias:
    print(
        f"{categoria} tem o valor somado de: {categorias[categoria]['Valor']} com os seguintes produtos listados: {', '.join(categorias[categoria]['Produtos'])}."
    )

print("# 02:")

funcionarios = [
    {"nome": "Ana", "setor": "Financeiro", "salario": 5000},
    {"nome": "João", "setor": "TI", "salario": 3000},
    {"nome": "Maria", "setor": "TI", "salario": 7000},
    {"nome": "Joana", "setor": "TI", "salario": 8750},
    {"nome": "José", "setor": "TI", "salario": 9300},
    {"nome": "Angela", "setor": "Financeiro", "salario": 2500},
    {"nome": "Carlos", "setor": "Financeiro", "salario": 2500},
    {"nome": "Bruno", "setor": "RH", "salario": 4200},
    {"nome": "Patricia", "setor": "RH", "salario": 6100},
    {"nome": "Marcos", "setor": "Financeiro", "salario": 5400},
]

setores = {}
for funcionario in funcionarios:
    if not setores.get(funcionario["setor"]):
        setores[funcionario["setor"]] = {
            "Total": funcionario["salario"],
            "Funcionários": [funcionario["nome"]],
        }
    else:
        setores[funcionario["setor"]]["Total"] += funcionario["salario"]
        setores[funcionario["setor"]]["Funcionários"].append(funcionario["nome"])

for setor in setores:
    media_salarial = setores[setor]["Total"] / len(setores[setor]["Funcionários"])
    print(
        f"{setor} tem o total de salários em: R$ {setores[setor]['Total']} com os seguintes funcionários: {', '.join(setores[setor]['Funcionários'])} e com média salarial de: {media_salarial}."
    )


print("# 03:")
pets = [
    {"nome": "Thor", "especie": "Cachorro", "peso": 12},
    {"nome": "Mimi", "especie": "Gato", "peso": 4},
    {"nome": "Rex", "especie": "Cachorro", "peso": 30},
    {"nome": "Luna", "especie": "Gato", "peso": 6},
    {"nome": "Bob", "especie": "Cachorro", "peso": 9},
    {"nome": "Mel", "especie": "Gato", "peso": 5},
    {"nome": "Nina", "especie": "Coelho", "peso": 3},
    {"nome": "Pipoca", "especie": "Coelho", "peso": 2},
    {"nome": "Max", "especie": "Cachorro", "peso": 18},
    {"nome": "Fred", "especie": "Papagaio", "peso": 1},
]

especies = {}
for pet in pets:
    if not especies.get(pet["especie"]):
        especies[pet["especie"]] = {
            "Média de Peso": sum(
                [
                    animal["peso"]
                    for animal in pets
                    if pet["especie"] == animal["especie"]
                ]
            )
            / len([pet for animal in pets if pet["especie"] == animal["especie"]]),
            "Nomes": [
                animal["nome"] for animal in pets if pet["especie"] == animal["especie"]
            ],
            "Mais de 10 Kg": [
                animal["nome"] for animal in pets if pet["especie"] == animal["especie"] and animal['peso'] > 10
            ],
            "Menos de 10 Kg": [
                animal["nome"] for animal in pets if pet["especie"] == animal["especie"] and animal['peso'] < 10
            ],
        }
    else:
        pass

for especie in especies:
    print(
        f"{especie}s tem peso médio de: {especies[especie]['Média de Peso']} Kg com os seguintes animaizinhos: {', '.join(especies[especie]['Nomes'])}. Desses: {', '.join(especies[especie]['Mais de 10 Kg'])} são os que tem mais de 10 Kg e os: {', '.join(especies[especie]['Menos de 10 Kg'])} tem menos. "
    )


print("# 04:")
pedidos = [
    {"id": 1, "cidade": "Joinville", "status": "entregue"},
    {"id": 2, "cidade": "Joinville", "status": "pendente"},
    {"id": 3, "cidade": "Araquari", "status": "entregue"},
    {"id": 4, "cidade": "Joinville", "status": "entregue"},
    {"id": 5, "cidade": "Araquari", "status": "pendente"},
    {"id": 6, "cidade": "São Francisco do Sul", "status": "entregue"},
    {"id": 7, "cidade": "Jaraguá do Sul", "status": "pendente"},
    {"id": 8, "cidade": "Joinville", "status": "pendente"},
    {"id": 9, "cidade": "Araquari", "status": "entregue"},
    {"id": 10, "cidade": "Jaraguá do Sul", "status": "entregue"},
]

cidades_pedidos = {}
for pedido in pedidos:
    cidade = pedido["cidade"]
    if not cidades_pedidos.get(cidade):
        cidades_pedidos[cidade] = {"entregue": 0, "pendente": 0}
    else:
        cidades_pedidos[cidade][pedido["status"]] += 1

for cidade in cidades_pedidos:
    print(f"Em {cidade}, foram {cidades_pedidos[cidade]['entregue']} entregues e {cidades_pedidos[cidade]['pendente']} pendentes.")


print("\n# 05:")
alunos = [
    {"nome": "Lucas", "turma": "A", "nota": 8},
    {"nome": "Fernanda", "turma": "A", "nota": 5},
    {"nome": "Pedro", "turma": "B", "nota": 6},
    {"nome": "Julia", "turma": "B", "nota": 9},
    {"nome": "Mariana", "turma": "A", "nota": 7},
    {"nome": "Gabriel", "turma": "B", "nota": 4},
    {"nome": "Aline", "turma": "C", "nota": 10},
    {"nome": "Rafael", "turma": "C", "nota": 6},
    {"nome": "Bianca", "turma": "A", "nota": 9},
    {"nome": "Tiago", "turma": "C", "nota": 8},
]

turmas = {}
categorias_nota = {"Nota Acima de 7": [], "Nota 7 ou abaixo": []}

for aluno in alunos:
    turma = aluno["turma"]
    if not turmas.get(turma):
        turmas[turma] = {"Nomes": [aluno["nome"]], "Notas": [aluno["nota"]]}
    else:
        turmas[turma]["Nomes"].append(aluno["nome"])
        turmas[turma]["Notas"].append(aluno["nota"])
    info_aluno = f"{aluno['nome']} ({aluno['nota']})"
    if aluno["nota"] > 7:
        categorias_nota["Nota Acima de 7"].append(info_aluno)
    else:
        categorias_nota["Nota 7 ou abaixo"].append(info_aluno)

for turma in sorted(turmas):
    media = sum(turmas[turma]["Notas"]) / len(turmas[turma]["Notas"])
    print(f"Turma {turma} tem os alunos: {', '.join(turmas[turma]['Nomes'])} e média de notas de: {media:.2f}.")

for categoria in categorias_nota:
    print(f"{categoria}: {', '.join(categorias_nota[categoria])}")


print("\n# 06:")
transacoes = [
    {"tipo": "entrada", "categoria": "venda", "valor": 200},
    {"tipo": "saida", "categoria": "compra", "valor": 150},
    {"tipo": "entrada", "categoria": "servico", "valor": 300},
    {"tipo": "saida", "categoria": "compra", "valor": 100},
    {"tipo": "entrada", "categoria": "venda", "valor": 450},
    {"tipo": "saida", "categoria": "salario", "valor": 1200},
    {"tipo": "entrada", "categoria": "investimento", "valor": 800},
    {"tipo": "saida", "categoria": "aluguel", "valor": 900},
    {"tipo": "entrada", "categoria": "servico", "valor": 250},
    {"tipo": "saida", "categoria": "compra", "valor": 220},
]

por_tipo = {}
por_categoria = {}
por_combinacao = {}

for t in transacoes:
    tipo = t["tipo"]
    cat = t["categoria"]
    valor = t["valor"]
    
    if not por_tipo.get(tipo):
        por_tipo[tipo] = valor
    else:
        por_tipo[tipo] += valor

    if not por_categoria.get(cat):
        por_categoria[cat] = valor
    else:
        por_categoria[cat] += valor
        
    chave_combo = f"{tipo} - {cat}"
    if not por_combinacao.get(chave_combo):
        por_combinacao[chave_combo] = valor
    else:
        por_combinacao[chave_combo] += valor

for tipo in por_tipo:
    print(f"Tipo '{tipo}' totalizou: R$ {por_tipo[tipo]:.2f}")
print()
for cat in por_categoria:
    print(f"Categoria '{cat}' totalizou: R$ {por_categoria[cat]:.2f}")
print()
for combo in por_combinacao:
    print(f"Combinação [{combo}] totalizou: R$ {por_combinacao[combo]:.2f}")


print("\n# 07:")
filmes = [
    {"titulo": "Aventura Final", "genero": "Ação", "classificacao": "14", "duracao": 130},
    {"titulo": "Risos em Dobro", "genero": "Comédia", "classificacao": "10", "duracao": 95},
    {"titulo": "Noite de Mistério", "genero": "Suspense", "classificacao": "16", "duracao": 110},
    {"titulo": "Coração em Cena", "genero": "Romance", "classificacao": "12", "duracao": 125},
    {"titulo": "Missão Oceânica", "genero": "Ação", "classificacao": "12", "duracao": 118},
    {"titulo": "Férias Malucas", "genero": "Comédia", "classificacao": "Livre", "duracao": 102},
    {"titulo": "Segredos da Cidade", "genero": "Suspense", "classificacao": "14", "duracao": 140},
    {"titulo": "Destino de Verão", "genero": "Romance", "classificacao": "10", "duracao": 98},
    {"titulo": "Heróis do Amanhã", "genero": "Ação", "classificacao": "14", "duracao": 145},
    {"titulo": "Amigos do Bairro", "genero": "Comédia", "classificacao": "Livre", "duracao": 88},
]

generos_filmes = {}
classificacoes_filmes = {}

for filme in filmes:
    gen = filme["genero"]
    cls = filme["classificacao"]
    
    if not generos_filmes.get(gen):
        generos_filmes[gen] = {
            "Titulos": [filme["titulo"]],
            "Mais de 120 min": [filme["titulo"]] if filme["duracao"] > 120 else [],
            "120 min ou menos": [filme["titulo"]] if filme["duracao"] <= 120 else []
        }
    else:
        generos_filmes[gen]["Titulos"].append(filme["titulo"])
        if filme["duracao"] > 120:
            generos_filmes[gen]["Mais de 120 min"].append(filme["titulo"])
        else:
            generos_filmes[gen]["120 min ou menos"].append(filme["titulo"])
    if not classificacoes_filmes.get(cls):
        classificacoes_filmes[cls] = [filme["duracao"]]
    else:
        classificacoes_filmes[cls].append(filme["duracao"])

for gen in generos_filmes:
    print(f"Gênero {gen} possui os filmes: {', '.join(generos_filmes[gen]['Titulos'])}.")
    print(f"Mais de 120 min: {', '.join(generos_filmes[gen]['Mais de 120 min']) or 'Nenhum'}")
    print(f"120 min ou menos: {', '.join(generos_filmes[gen]['120 min ou menos']) or 'Nenhum'}")

print()
for cls in classificacoes_filmes:
    media_duracao = sum(classificacoes_filmes[cls]) / len(classificacoes_filmes[cls])
    print(f"Classificação Indicativa {cls} tem duração média de: {media_duracao:.1f} minutos.")