# Cadastro por Faixa Etária em Python 🧓👶👨‍🦱

Projeto desenvolvido em Python para realizar o **cadastro de pessoas**, com base em **nome e idade**, que:

- Classifica cada pessoa como: `criança`, `adolescente`, `adulto` ou `idoso`
- Armazena os dados em uma lista de dicionários (simulando um banco de dados)
- Calcula e exibe estatísticas como:
  - Média de idade
  - Pessoa mais nova e mais velha
  - Quantidade por faixa etária
- Exporta os dados para `.TXT` ou `.CSV`, conforme escolha do usuário
- Valida entradas (nome e idade)

## 🚀 Como usar

1. Clone o repositório ou baixe o arquivo `.py`
2. Execute o script com Python 3:

```bash
python nome_do_arquivo.py
```

3. Siga as instruções do terminal:
   - Digite nome e idade das pessoas
   - Escolha se deseja continuar o cadastro
   - Ao final, visualize o relatório no terminal
   - Escolha salvar os dados em `.txt` ou `.csv`

## 🧠 Tecnologias utilizadas

- Python 3.x
- FastAPI: Framework utilizado para criar a API RESTful.
- Pydantic: Para a validação e estruturação dos dados.
- Manipulação de arquivos (`open()`, `csv`)
- Estrutura de dados com `listas` e `dicionários`
- Modularização com funções
- Validação de entrada (`try/except`, `.isalpha()`)

## 🌐 API FastAPI
Agora, é possível interagir com o sistema de cadastro de pessoas através de requisições HTTP.
A versão do projeto com FastAPI adiciona uma interface de API para cadastrar e listar pessoas, além de fornecer estatísticas sobre os cadastros.


## 📂 Exemplo de saída `.txt`

```
Nome: Tiago | Idade: 35 | Classificação: adulto
Nome: Ana   | Idade: 10 | Classificação: criança
```

## 📊 Exemplo de saída `.csv`

```
Nome,Idade,Classificacao
Tiago,35,adulto
Ana,10,crianca
```

## 👨‍💻 Autor

**Tiago Freitas** 
Formado em Análise e Desenvolvimento de Sistema
Desenvolvedor em formação, apaixonado por lógica, organização de dados e novas tecnologias.

## 📝 Licença

Este projeto está sob a licença MIT. Fique à vontade para usar, modificar e compartilhar!