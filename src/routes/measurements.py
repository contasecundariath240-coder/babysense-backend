from flask import Blueprint, request, jsonify
import psycopg2
import os

measurements_bp = Blueprint("measurements", __name__)

def get_db():
    return psycopg2.connect(os.environ["DATABASE_URL"])

@measurements_bp.route("/", methods=["POST"])
def add_measurement():
    data = request.json
    temp = data.get("temperature")
    baby_id = data.get("baby_id")

    if not temp or not baby_id:
        return {"error": "Dados incompletos"}, 400

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO measurements (baby_id, temperature) VALUES (%s, %s)",
        (baby_id, temp)
    )
    conn.commit()
    cur.close()
    conn.close()

    return {"status": "ok"}, 201

@measurements_bp.route("/<baby_id>", methods=["GET"])
def list_measurements(baby_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, temperature, created_at FROM measurements WHERE baby_id = %s ORDER BY created_at DESC",
        (baby_id,)
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify([
        {"id": r[0], "temperature": r[1], "created_at": r[2]} for r in rows
    ]) 
