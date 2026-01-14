from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY").strip()

llm = ChatGroq(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    temperature=0.2,
    groq_api_key=GROQ_API_KEY)

def generate_itinerary(destination, days, style=None, budget=None):
    """
    Genera un itinerario usando el LLM.

    :param destination: Destino del viaje
    :param days: Número de días
    :param style: Estilo del viaje (opcional)
    :param budget: Presupuesto del viaje (opcional)
    :return: Texto con el itinerario generado
    """

    style = style or "normal"
    budget = budget or "medio"

    messages = [
        SystemMessage(
            content=(
                f"Crea un itinerario de {days} días para {destination}, "
                f"con estilo {style} y presupuesto {budget}. "
                "Responde día por día e incluye consejos prácticos."
            )
        ),
        HumanMessage(
            content=(
                f"Por favor, genera el itinerario completo para {days} días en {destination}, "
                f"siguiendo el estilo {style} y el presupuesto {budget}."
            )
        )
    ]
  
    generated_plan = llm.invoke(messages) 
    return generated_plan