# Usa uma imagem oficial do Python
FROM python:3.11

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos para dentro do container
COPY . /app

# Instala as dependências
RUN pip install --no-cache-dir fastapi uvicorn

# Expõe a porta 8000 (usada pelo FastAPI)
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["uvicorn", "cadastro_em_Fastapi:app","--host", "0.0.0.0", "--port", "8000"]