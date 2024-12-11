# Definir a imagem base
FROM python:3.9-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos necessários para o container
COPY app.py requirements.txt /app/

# Instalar as dependências
RUN pip install -r requirements.txt

# Expôr a porta da aplicação
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
