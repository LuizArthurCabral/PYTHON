# Imagem base oficial do Python, variante "slim" (enxuta: sem
# ferramentas de build/desenvolvimento, menor superfície e menor tamanho)
FROM python:3.12-slim

# Diretório de trabalho dentro do contêiner. Todas as instruções
# seguintes (COPY, RUN, CMD) passam a ser relativas a este caminho.
WORKDIR /app

# Copia APENAS o requirements.txt primeiro. Isso aproveita o cache de
# camadas do Docker: enquanto as dependências não mudarem, o `pip install`
# não precisa ser refeito a cada rebuild, mesmo que o código-fonte mude.
COPY requirements.txt .

# Instala as dependências. --no-cache-dir evita guardar o cache de
# download do pip na imagem, reduzindo o tamanho final.
RUN pip install --no-cache-dir -r requirements.txt

# Só agora copia o restante do código da aplicação. Como o código muda
# com mais frequência que as dependências, colocá-lo depois preserva o
# cache da camada anterior na maioria dos rebuilds.
COPY . .

# Variável de ambiente lida pela aplicação para saber onde persistir
# os dados. É sobrescrevível em tempo de execução com `docker run -e`.
ENV DATA_DIR=/app/data

# Documenta que o contêiner escuta na porta 8000 (não publica a porta
# por si só; isso é feito com `-p` no `docker run`).
EXPOSE 8000

# Declara /app/data como ponto de montagem de volume. Se o contêiner
# for iniciado sem `-v`, o Docker cria automaticamente um volume anônimo
# para esse caminho, evitando que dados fiquem presos na camada
# gravável (mas SEM -v nomeado os dados ainda são perdidos ao remover
# o contêiner, pois o volume anônimo não é reaproveitado — ver Etapa 6).
VOLUME /app/data

# Comando padrão executado quando o contêiner sobe.
CMD ["python3", "app.py"]
