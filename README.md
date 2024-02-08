# Comandos Básicos do SQLite

Este repositório contém a resolução de uma lista de exercíos para práticar os comandos em SQL.
<p>E aqui você encontra informações sobre os principais comandos de banco de dados SQLite, um banco de dados relacional leve e embutido.

## Introdução ao SQLite

SQLite é um sistema de gerenciamento de banco de dados relacional (SGBDR) que não requer um processo de servidor separado e permite acesso direto ao banco de dados usando uma linguagem de consulta. Ele é amplamente utilizado em aplicativos móveis, navegadores da web e outros aplicativos que precisam de armazenamento de dados local.

## Principais Comandos

### Criação de Tabelas

```sql
CREATE TABLE nome_da_tabela (
    coluna1 tipo1,
    coluna2 tipo2,
    ...
);
```
### Inserção de Dados
```sql
INSERT INTO nome_da_tabela (coluna1, coluna2, ...)
VALUES (valor1, valor2, ...);
```

### Seleção de Dados
```sql
SELECT coluna1, coluna2, ...
FROM nome_da_tabela
WHERE condição;
```

### Atualização de Dados
```sql
UPDATE nome_da_tabela
SET coluna1 = novo_valor1, coluna2 = novo_valor2, ...
WHERE condição;
```

### Exclusão de Dados
```sql
DELETE FROM nome_da_tabela
WHERE condição;
```

### Alterar Tabela
```sql
ALTER TABLE nome_da_tabela
ADD COLUMN nova_coluna tipo;
```

### Deletar Tabela
```sql
DROP TABLE nome_da_tabela;
```

### Ordenação
```sql
SELECT coluna1, coluna2, ...
FROM nome_da_tabela
ORDER BY coluna1 ASC|DESC, coluna2 ASC|DESC;
```

### HAVING
```sql
SELECT produto, SUM(quantidade * preco_unitario) AS total_vendas
FROM vendas
GROUP BY produto
HAVING SUM(quantidade) > 100;
```

### Join
```sql
SELECT *
FROM tabela1
JOIN tabela2 ON tabela1.coluna = tabela2.coluna;
```

### Left Join
```sql
SELECT *
FROM tabela1
LEFT JOIN tabela2 ON tabela1.coluna = tabela2.coluna;
```

### Full Join
```sql
SELECT *
FROM tabela1
FULL JOIN tabela2 ON tabela1.coluna = tabela2.coluna;
```


