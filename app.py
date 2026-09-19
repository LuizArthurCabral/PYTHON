"""
Serviço de anotações (notas-api)

Rotas:
  POST /notas   -> recebe {"texto": "..."} e salva com data/hora
  GET  /notas   -> retorna todas as anotações salvas
  GET  /health  -> {"status": "ok"}

Armazenamento: SQLite em <DATA_DIR>/notas.db
DATA_DIR é lido da variável de ambiente DATA_DIR (padrão: /app/data)
"""

import os
import sqlite3
from datetime import datetime, timezone

from flask import Flask, jsonify, request

DATA_DIR = os.environ.get("DATA_DIR", "/app/data")
DB_PATH = os.path.join(DATA_DIR, "notas.db")

app = Flask(__name__)


def get_connection():
    os.makedirs(DATA_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS notas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                texto TEXT NOT NULL,
                criado_em TEXT NOT NULL
            )
            """
        )
        conn.commit()


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@app.route("/notas", methods=["POST"])
def criar_nota():
    payload = request.get_json(silent=True)
    if not payload or "texto" not in payload or not str(payload["texto"]).strip():
        return jsonify({"erro": "campo 'texto' é obrigatório"}), 400

    texto = str(payload["texto"]).strip()
    criado_em = datetime.now(timezone.utc).isoformat()

    with get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO notas (texto, criado_em) VALUES (?, ?)",
            (texto, criado_em),
        )
        conn.commit()
        nota_id = cursor.lastrowid

    return jsonify({"id": nota_id, "texto": texto, "criado_em": criado_em}), 201


@app.route("/notas", methods=["GET"])
def listar_notas():
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT id, texto, criado_em FROM notas ORDER BY id ASC"
        ).fetchall()

    notas = [dict(row) for row in rows]
    return jsonify(notas)


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=8000)
