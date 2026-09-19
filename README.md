# notas-api

Serviço HTTP simples de anotações, escrito em Python/Flask, empacotado em
imagem Docker própria, com persistência de dados em volume nomeado.

## Estrutura

```
notas-docker/
├── app.py            # aplicação Flask
├── requirements.txt  # dependências Python
├── Dockerfile         # receita de construção da imagem
├── .dockerignore
├── compose.yaml        # opcional: build + run + volume via docker compose
├── README.md
└── RELATORIO.md        # relatório da atividade
```

## Rotas da API

| Método | Rota      | Descrição                                   |
|--------|-----------|----------------------------------------------|
| GET    | `/health` | Retorna `{"status": "ok"}`                    |
| POST   | `/notas`  | Recebe `{"texto": "..."}` e salva com data/hora |
| GET    | `/notas`  | Retorna todas as anotações salvas             |

Dados são armazenados em SQLite, no arquivo `<DATA_DIR>/notas.db`.
`DATA_DIR` é uma variável de ambiente (padrão: `/app/data`).

## Executar localmente (sem Docker)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
DATA_DIR=./data python3 app.py
```

## Build da imagem

```bash
docker build -t notas-api:1.0 .
docker image ls notas-api
docker history notas-api:1.0
```

## Executar com volume nomeado (persistência)

```bash
docker volume create notas-dados
docker run -d --name notas -p 8000:8000 -v notas-dados:/app/data notas-api:1.0
docker ps
docker logs notas
```

Inserir anotações:

```bash
curl -X POST http://localhost:8000/notas -H "Content-Type: application/json" -d '{"texto": "primeira nota"}'
curl -X POST http://localhost:8000/notas -H "Content-Type: application/json" -d '{"texto": "segunda nota"}'
curl -X POST http://localhost:8000/notas -H "Content-Type: application/json" -d '{"texto": "terceira nota"}'
curl http://localhost:8000/notas
```

## Prova de persistência

```bash
# destrói o contêiner
docker stop notas && docker rm notas

# o volume continua existindo, independente do contêiner
docker volume ls
docker volume inspect notas-dados

# sobe um NOVO contêiner reaproveitando o MESMO volume
docker run -d --name notas2 -p 8000:8000 -v notas-dados:/app/data notas-api:1.0

# as anotações anteriores continuam lá
curl http://localhost:8000/notas
```

## Contraexemplo (efemeridade, sem `-v`)

```bash
docker run -d --name notas-efemero -p 8001:8000 notas-api:1.0
curl -X POST http://localhost:8001/notas -H "Content-Type: application/json" -d '{"texto": "nota que vai sumir"}'
docker stop notas-efemero && docker rm notas-efemero

# novo contêiner, também sem -v: recebe um volume anônimo NOVO e vazio
docker run -d --name notas-efemero2 -p 8001:8000 notas-api:1.0
curl http://localhost:8001/notas   # retorna []
```

## Rodando com docker compose (opcional)

```bash
docker compose up -d --build
docker compose down          # remove o contêiner, mantém o volume
docker compose down -v       # remove também o volume
```

## Limpeza

```bash
docker rm -f notas notas2 notas-efemero notas-efemero2 2>/dev/null
docker volume rm notas-dados
```
