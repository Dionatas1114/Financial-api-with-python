# Usa a imagem oficial do Python como base
FROM python:3.13.1

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y build-essential

# Criar diretório de trabalho
WORKDIR /app

# Copiar arquivos do projeto
COPY . .

# Instalar dependências específicas para produção
RUN pip install -r requirements-prod.txt

# Expor a porta do servidor
EXPOSE 8000

# Rodar o servidor com gunicorn
CMD ["gunicorn", "-w", "4", "main:app", "--host", "0.0.0.0", "--port", "8000"]
