# Relatório — Construção de imagem própria e persistência de dados em volume

**Projeto:** notas-api
**Autor(es):** _[preencher]_
**Repositório:** _[link do repositório Git]_

## 1. Explicação linha a linha do Dockerfile

```dockerfile
FROM python:3.12-slim
```
Define a imagem base: Debian mínimo com Python 3.12 já instalado. A variante
`slim` foi escolhida em vez da imagem `python:3.12` "completa" porque exclui
compiladores e bibliotecas de desenvolvimento que a aplicação não usa,
resultando em uma imagem final bem menor (também existe a alternativa
`alpine`, ainda menor, mas baseada em musl libc, o que ocasionalmente causa
incompatibilidades com pacotes Python que dependem de extensões em C).

```dockerfile
WORKDIR /app
```
Cria (se não existir) e define `/app` como diretório de trabalho corrente
dentro do contêiner. Todas as instruções `COPY`, `RUN` e o `CMD` finais são
resolvidos relativos a esse caminho.

```dockerfile
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
```
O `requirements.txt` é copiado **antes** do restante do código de propósito:
o Docker constrói a imagem em camadas e reaproveita (cacheia) uma camada
sempre que os arquivos de entrada dela não mudaram. Como as dependências
mudam com muito menos frequência que o código da aplicação, isolar esse
`COPY` + `RUN pip install` em camadas próprias faz com que, em rebuilds
subsequentes que só alteram `app.py`, o Docker reutilize a camada com as
dependências já instaladas, em vez de reinstalá-las do zero. `--no-cache-dir`
evita que o pip guarde arquivos de cache de download dentro da imagem,
reduzindo seu tamanho final.

```dockerfile
COPY . .
```
Copia o restante do código da aplicação (respeitando as exclusões do
`.dockerignore`) para `/app` dentro da imagem. Feito depois da instalação de
dependências para não invalidar o cache da camada anterior a cada alteração
de código.

```dockerfile
ENV DATA_DIR=/app/data
```
Define a variável de ambiente que a aplicação lê (`os.environ.get("DATA_DIR", ...)`)
para saber onde gravar o banco SQLite. Fica explícita na imagem, mas pode ser
sobrescrita em tempo de execução com `docker run -e DATA_DIR=...`.

```dockerfile
EXPOSE 8000
```
Instrução declarativa/documental: indica que o processo dentro do contêiner
escuta na porta 8000. Não publica a porta para o host por si só — isso só
acontece com a flag `-p` em `docker run`.

```dockerfile
VOLUME /app/data
```
Declara `/app/data` como um ponto de montagem de volume. Isso garante que,
mesmo que o contêiner seja iniciado sem `-v` explícito, o Docker crie
automaticamente um volume anônimo para esse caminho — evitando que os dados
fiquem presos apenas na camada gravável (de escrita) do contêiner. Ainda
assim, sem um volume **nomeado**, cada novo contêiner recebe um volume
anônimo novo e vazio, então o efeito prático (do ponto de vista da
aplicação) continua sendo perda de dados ao recriar o contêiner — ver seção
da Etapa 6.

```dockerfile
CMD ["python3", "app.py"]
```
Comando padrão executado quando o contêiner é iniciado (forma *exec*, sem
shell intermediário). Pode ser sobrescrito passando outro comando ao final
de `docker run`.

## 2. Etapa 3 — Build da imagem

Tamanho final da imagem (`docker image ls notas-api`):
`[preencher após build — ex.: 150MB]`

Lista de camadas (`docker history notas-api:1.0`):
```
[colar saída do comando aqui]
```

## 3. Etapa 4 — Execução com volume nomeado

```
[colar saída de docker ps]
[colar saída de docker logs notas]
[colar as 3 respostas de POST /notas e a resposta de GET /notas]
```

## 4. Etapa 5 — Prova de persistência

```
[colar saída de: docker stop notas && docker rm notas]
[colar saída de: docker volume ls]
[colar saída de: docker volume inspect notas-dados]
[colar saída de: docker run ... notas2 ...]
[colar saída de: curl http://localhost:8000/notas  -> deve mostrar as 3 notas anteriores]
```

**Conclusão:** as anotações sobreviveram à destruição completa do contêiner
(`stop` + `rm`) porque estavam gravadas no volume nomeado `notas-dados`, que
é uma entidade gerenciada pelo Docker Engine independente do ciclo de vida
de qualquer contêiner específico. O novo contêiner (`notas2`) apenas montou
o mesmo volume no mesmo caminho (`/app/data`) e encontrou o arquivo
`notas.db` já populado.

## 5. Etapa 6 — Contraexemplo (efemeridade)

```
[colar saída de: docker run ... notas-efemero (sem -v)]
[colar saída do POST de uma nota]
[colar saída de: docker stop notas-efemero && docker rm notas-efemero]
[colar saída de: docker run ... notas-efemero2 (sem -v)]
[colar saída de: curl http://localhost:8001/notas  -> deve retornar []]
```

**Explicação:** sem `-v`, o `/app/data` do contêiner é atendido por um
volume **anônimo**, criado automaticamente por causa da instrução `VOLUME`
do Dockerfile. Cada `docker run` gera um volume anônimo novo e sem nenhuma
ligação com o volume anônimo do contêiner anterior. Ao remover o contêiner
com `docker rm` (sem a flag `-v` desse comando), o volume anônimo associado
fica órfão — não é automaticamente apagado, mas também não é reaproveitado
por nenhum contêiner futuro, então, do ponto de vista da aplicação, os
dados "somem": o `notas-efemero2` não tem nenhuma referência ao volume que
guardava a nota do `notas-efemero`, e enxerga um `/app/data` vazio.

## 6. Etapa 7 — Inspeção

**a) Onde, no host, o Docker armazena fisicamente o volume `notas-dados`?**

A saída de `docker volume inspect notas-dados` mostra o campo `Mountpoint`,
tipicamente algo como:
```
/var/lib/docker/volumes/notas-dados/_data
```
(em Docker Desktop no Windows/macOS, esse caminho fica dentro da VM Linux
que roda o Docker Engine, não diretamente no sistema de arquivos do host).

```
[colar saída completa de docker volume inspect notas-dados]
```

**b) Qual é o conteúdo do diretório `/app/data` dentro do contêiner?**

```
[colar saída de: docker exec notas2 ls -la /app/data]
```
Esperado: o arquivo `notas.db` (SQLite) com tamanho maior que zero.

**c) O que acontece com os dados se você executar `docker volume rm
notas-dados` com o contêiner parado e removido?**

Os dados são apagados permanentemente. O comando `docker volume rm` remove
o volume gerenciado (e, com ele, o arquivo físico em
`/var/lib/docker/volumes/notas-dados/_data`) do disco do host. Diferente de
parar/remover um contêiner — que preserva o volume — remover o próprio
volume é uma operação destrutiva e irreversível sobre os dados, só possível
enquanto nenhum contêiner o está usando (o Docker recusa a remoção de um
volume em uso).

```
[colar saída do comando docker volume rm notas-dados
 e de uma tentativa de subir um novo contêiner com -v notas-dados:/app/data
 mostrando que os dados antigos não estão mais lá]
```

## 7. Dificuldades e aprendizados

_[preencher com pelo menos um parágrafo pessoal — por exemplo, dificuldades
com cache de camadas, entendimento da diferença entre volume nomeado e
anônimo, problemas de permissão de arquivo, tempo de build, etc.]_

Um ponto que costuma gerar confusão nesta atividade é achar que a instrução
`VOLUME` no Dockerfile, por si só, já garante persistência entre execuções.
Na prática, ela só evita que os dados fiquem presos na camada gravável do
contêiner (o que ajuda em desempenho e no `docker commit`), mas não impede
a perda de dados entre contêineres diferentes: para isso é indispensável
nomear o volume explicitamente com `-v notas-dados:/app/data` e reutilizar
esse mesmo nome nas execuções seguintes.
