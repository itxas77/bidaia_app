from flask import Flask, request, jsonify
import os
import psycopg2
from dotenv import load_dotenv
from llm import generate_itinerary

load_dotenv()

app = Flask(__name__)
app.config["DEBUG"] = True

DATABASE_URL = os.getenv("DATABASE_URL").strip()

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "BidaIA_app API funcionando correctamente 🚀"})


@app.route("/itinerary", methods=["POST"])
def create_itinerary():
    data = request.get_json()
    
    destination = data.get("destination")
    days = data.get("days")
    style = data.get("style", "")
    budget = data.get("budget", "")

    if not destination or not days:
        return jsonify({"error": "Los campos 'destination' y 'days' son obligatorios"}), 400

    # Generar itinerario con LLM
    generated_plan = generate_itinerary(
        destination=destination,
        days=days,
        style=style,
        budget=budget)
    
    
    # Guardar en PostgreSQL
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO itineraries
        (destination, days, style, budget, generated_plan)
        VALUES (%s, %s, %s, %s, %s)
    """, (destination, days, style, budget, generated_plan.content))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({
        "destination": destination,
        "days": days,
        "style": style,
        "budget": budget,
        "generated_plan": generated_plan.content})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)