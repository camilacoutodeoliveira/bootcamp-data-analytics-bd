import sqlite3

connection = sqlite3.connect('bd')
cursor = connection.cursor()

# 1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).
connection.execute('CREATE TABLE alunos (id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (1, "Camila", 31, "Data Analytics")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (2, "Luana", 27, "Educação Fisica")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (3, "Raissa", 35, "Gestão de Projetos")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (4, "Janine", 41, "Cinema")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (5, "Ana", 18, "Jornalismo")')

# 3. Consultas Básicas
# Escreva consultas SQL para realizar as seguintes tarefas:
# a) Selecionar todos os registros da tabela "alunos".
alunos = cursor.execute('SELECT * FROM alunos')

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos
alunos_gt_20 = cursor.execute('SELECT * FROM alunos WHERE idade > 20')

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
alunos_eng = cursor.execute('SELECT * FROM alunos WHERE curso == "Engenharia" ORDER BY nome ASC')
for aluno in alunos_eng:
    print(aluno)

# d) Contar o número total de alunos na tabela
alunos_total = cursor.execute('SELECT COUNT(nome) AS alunos_total FROM alunos')
print(alunos_total)

# 4. Atualização e Remoção
# a) Atualize a idade de um aluno específico na tabela.
cursor.execute('UPDATE alunos SET idade="40" WHERE id=4')

# b) Remova um aluno pelo seu ID
cursor.execute('DELETE FROM alunos WHERE id=5')

# 5. Criar uma Tabela e Inserir Dados
# Crie uma tabela chamada "clientes" com os campos: id (chave
# primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns
# registros de clientes na tabela.

cursor.execute('CREATE TABLE clientes (id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT)')

cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (1, "Camila", 31, 400000)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (2, "Maria", 18, 1000)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (3, "Antonio", 60, 35000)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (4, "Rah", 35, 70000)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (5, "Ro", 54, 30000)')

# 6. Consultas e Funções Agregadas
# Escreva consultas SQL para realizar as seguintes tarefas:
# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos
cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')

# b) Calcule o saldo médio dos clientes.
cursor.execute('SELECT AVG(saldo) FROM clientes')

# c) Encontre o cliente com o saldo máximo.
cursor.execute('SELECT * FROM clientes ORDER BY saldo DESC LIMIT 1')

# d) Conte quantos clientes têm saldo acima de 1000.
cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000 ')

# 7. Atualização e Remoção com Condições
# a) Atualize o saldo de um cliente específico.
cursor.execute('UPDATE clientes SET saldo= 150000 WHERE id= 4')

# b) Remova um cliente pelo seu ID.
cursor.execute('DELETE FROM clientes WHERE id = 5')

# 8. Junção de Tabelas
# Crie uma segunda tabela chamada "compras" com os campos: id(chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). 
#Insira algumas
# compras associadas a clientes existentes na tabela "clientes".
# Escreva uma consulta para exibir o nome do cliente, o produto e o
# valor de cada compra

cursor.execute('CREATE TABLE compras (id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor FLOAT, FOREIGN KEY (cliente_id) REFERENCES clientes(id))')

cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor)  VALUES(1, 1, "Produto A", 100.50),(2, 2, "Produto B", 200.75),(3,3, "Produto C", 50.25) ')

cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM compras LEFT JOIN clientes ON compras.cliente_id = clientes.id')

connection.commit()
connection.close()
