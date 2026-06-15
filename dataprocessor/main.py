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

print('\nDesafio guiado:')
cidades = {}
for cliente in clientes:
    cidade = cliente.get("cidade", "N/A")
    if cidades.get(cidade):
        cidades[cidade] += 1
    else:
        cidades[cidade] = 1

for cidade in cidades:
    print(f"{str(cidade)}: {cidades[cidade]} clientes")

print('\nDesafio extra:')
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
    print(cidade,
        f"{str(cidade)} ({cidade_clientes[cidade]["contagem"]}): {', '.join(cidade_clientes[cidade]["clientes"])}"
    )
