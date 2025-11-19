from flask import Blueprint, request, jsonify
import psycopg2
import os

babies_bp = Blueprint("babies", __name__)

def get_db():
    return psycopg2.connect(os.environ["DATABASE_URL"])

@babies_bp.route("/", methods=["POST"])
def add_baby():
    data = request.json
    name = data.get("name")
    birth_date = data.get("birth_date")

    if not name or not birth_date:
        return {"error": "Dados incompletos"}, 400

    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO babies (name, birth_date) VALUES (%s, %s) RETURNING id",
        (name, birth_date)
    )

    baby_id = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return {"status": "ok", "baby_id": baby_id}, 201


@babies_bp.route("/", methods=["GET"])
def list_babies():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT id, name, birth_date FROM babies")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify([
        {"id": r[0], "name": r[1], "birth_date": r[2]}
        for r in rows
    ]) 
