#Função para Classificar a faixa Etária - Pynthon
def classificacao_idade (idade) :

    if idade >= 60 :
      return "idoso"

    elif idade >= 18 :
      return "adulto"

    elif idade < 12 :
      return "crianca"

    else :
      return "adolescente"


from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def home():
    return {"mensagem" : "API de cadastro ativa!"}
#Tela que aparece ao usuário final



from pydantic import BaseModel

class Pessoa(BaseModel):
    nome: str
    idade: int

bd = []

#POST enviar informações
@app.post("/cadastro")

def cadastrar(pessoa: Pessoa):
    #Chamando a Função de Classificação
    classificacao = classificacao_idade(pessoa.idade)

    #Adicionando todos os dados dentro de uma array
    registro = {
        "nome": pessoa.nome,
        "idade": pessoa.idade,
        "classificacao": classificacao
    }

    #Comando para adicionar no BD
    bd.append(registro)

    #Mensagem de retorno para o usuário
    return {"mensagem": "Cadastro realizado com sucesso", "dados": registro}


@app.get("/pessoas")

def listar_pessoa():
   return bd


@app.get("/estatisticas")

def estatisticas():
   
   #Mensagem caso não tenha registros no BD
   if not bd:
      return {"mensagem": "Sem registros ainda."}
   
   #Laço de repetição para contar quantos registros
   idades = [p["idade"] for p in bd]
   #Média
   media = sum(idades) / len(idades)
   #Contabiliza
   mais_novo = min(bd, key=lambda x: x["idade"])
   mais_velho = max(bd, key=lambda x: x["idade"])

   return {
      "total": len(bd),
      "media_idade": media,
      "mais_novo": mais_novo,
      "mais_velho": mais_velho,
   }