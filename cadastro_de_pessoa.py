def salva_dados(bd) :


    print("CSV ou TXT")
    tipo = input().strip().upper()

    if tipo == "TXT":
        with open("dados_pessoas.txt", "w", encoding="utf-8") as arquivo:
            for pessoa in bd:
                linha = f"Nome: {pessoa['Nome']} | Idade: {pessoa['idade']} | Classificação: {pessoa['Classificacao']}\n"
                arquivo.write(linha)
        print("Arquivo 'dados_pessoas.txt' salvo com sucesso!")

    elif tipo == "CSV":
        import csv
        with open("dados_pessoas.csv", "w", newline="", encoding="utf-8") as arquivo_csv:
            writer = csv.DictWriter(arquivo_csv, fieldnames=["Nome", "idade", "Classificacao"])
            writer.writeheader()
            for pessoa in bd:
                writer.writerow(pessoa)
        print("Arquivo 'dados_pessoas.csv' salvo com sucesso!")


#Função para Classificar a faixa Etária
def classificacao_idade (idade) :

    if idade >= 60 :
      return "idoso"

    elif idade >= 18 :
      return "adulto"

    elif idade < 12 :
      return "crianca"

    else :
      return "adolescente"

#Função para registrar pessoa

def registrar_pessoa () :

  while True :

    print("Informe seu Nome")
    nome = input().strip()

    if nome and nome.isalpha():
          break
    print("Nome inválido. Por favor, insira um nome válido.")

  while True :
    try:
        print("Informe sua Idade")
        idade = int(input())

        if idade > 0:
            break
        else :
            print("Idade deve ser maior que zero")
    except ValueError:
        print("Idade inválida. Por favor, insira um número inteiro válido.")

  classificacao = classificacao_idade(idade)

  return {
        "Nome" : nome,
        "idade" : idade,
        "Classificacao" : classificacao
    }

def calcular_estatisticas(bd) :

    #EXTRAINDO SOMENTE A IDADE
    idades = [pessoa["idade"] for pessoa in bd]
    media = sum(idades) / len(idades)

    #Não Entendi
    mais_novo = min(bd, key=lambda x: x["idade"])
    mais_velho = max(bd, key=lambda x: x["idade"])

    print("Média de idade:", media)
    print("Maior idade:", max(idades))
    print("Menor idade:", min(idades))

    print(f"Mais novo: {mais_novo['Nome']} ({mais_novo['idade']} anos)")
    print(f"Mais velho: {mais_velho['Nome']} ({mais_velho['idade']} anos)")

def main() :

  cont_idoso = 0
  cont_adulto = 0
  cont_crianca = 0
  cont_adolescente = 0
  fim = "S"
  bd = []

  while fim != "N" :

    bd.append(registrar_pessoa())

    print("Deseja Continuar? S/N")
    fim = input().upper()

  for pessoa in bd:
    if pessoa["Classificacao"] == "idoso":
        cont_idoso += 1
    elif pessoa["Classificacao"] == "adulto":
        cont_adulto += 1
    elif pessoa["Classificacao"] == "crianca":
        cont_crianca += 1
    elif pessoa["Classificacao"] == "adolescente":
        cont_adolescente += 1

  calcular_estatisticas(bd)


  print("\n - - * RESULTADO FINAL * - - \n")

  print("Total de pessoas:", len(bd))
  print("Idosos: ", cont_idoso)
  print("Crianças: ", cont_crianca)
  print("Adultos: ", cont_adulto)
  print("Adolescentes: ", cont_adolescente)

  print("Deseja Baixar os Arquivos em CSV ou TXT?")
  baixar_arquivo = input()

  if baixar_arquivo == "Não" :
    print("Dados não foram salvos.")
    quit()
  else :
    salva_dados(bd)

if __name__ == "__main__":
    main()