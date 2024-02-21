# Use a imagem base do Python
FROM python:3.8

# Copie o seu código para dentro do contêiner
COPY . /app

# Configure o diretório de trabalho
WORKDIR /app

# Instale as dependências do seu programa
RUN pip install --no-cache-dir -r requirements.txt

# Comando para executar o programa
CMD ["python", "grafico_geral.py"]
