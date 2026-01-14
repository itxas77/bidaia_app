BidaIA - Generador de Itinerarios con LLM

BidaIA es una aplicación web que genera **itinerarios de viaje personalizados** usando un **modelo LLM de Groq**. Los itinerarios se guardan en una base de datos PostgreSQL (Neon) y se pueden consultar desde un frontend moderno desarrollado con **HTML y TailwindCSS**.

---

📁 Estructura del proyecto

bidaia_app/
├─ app/
│ ├─ main.py
│ ├─ llm.py
│ ├─ templates/
│ │ └─ front.html
├─ requirements.txt
├─ Dockerfile
├─ .env
└─ README.md


---

⚡ Requisitos

- Python 3.10+
- Docker
- Cuenta en **Neon** (PostgreSQL)
- Clave API de **Groq** (`GROQ_API_KEY`)

---

🛠 Instalación local

1. Clonar el repositorio:

```bash
git clone <tu-repositorio>
cd bidaia_app

    Crear entorno virtual e instalar dependencias:

python -m venv venv
# Linux / Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt

    Crear archivo .env:

DATABASE_URL=postgresql://usuario:contraseña@host:puerto/db
GROQ_API_KEY=<tu_groq_api_key>

    Crear la tabla en Neon:

CREATE TABLE itineraries (
    id SERIAL PRIMARY KEY,
    destination TEXT NOT NULL,
    days INT NOT NULL,
    style TEXT,
    budget TEXT,
    generated_plan TEXT
);

    Ejecutar la aplicación localmente:

cd app
python -m main

    La app correrá en http://localhost:8000.

    El frontend estará disponible en / mostrando un formulario para generar itinerarios.

🐳 Uso con Docker

    Construir la imagen:

docker build --no-cache -t itxasodocker/bidaia_app:v1 .

    Ejecutar el contenedor:

docker run -p 8000:8000 --env-file .env itxasodocker/bidaia_app:v1

    La app estará disponible en http://localhost:8000.

🌐 Despliegue en Render

    Crear un Web Service en Render usando el repositorio.

    Configurar Variables de Entorno en Render:

        DATABASE_URL = URL de Neon

        GROQ_API_KEY = tu clave Groq

    Configurar el Build Command:

docker build -t bidaia_app .

    Configurar el Start Command:

python -m app.main

    Después del deploy, tu frontend estará accesible en la URL pública de Render.

💻 Endpoints API
GET /

    Devuelve un mensaje de prueba:

{
  "message": "BidaIA_app API funcionando correctamente 🚀"
}

POST /itinerary

    Genera un itinerario y lo guarda en la base de datos.

Body (JSON):

{
  "destination": "Roma",
  "days": 3,
  "style": "cultural",
  "budget": "medio"
}

Respuesta (JSON):

{
  "destination": "Roma",
  "days": 3,
  "style": "cultural",
  "budget": "medio",
  "generated_plan": "Itinerario generado por el LLM..."
}

🎨 Frontend

    El formulario en / permite introducir:

        Destino

        Número de días

        Estilo de viaje (opcional)

        Presupuesto (opcional)

    El resultado del itinerario se muestra debajo del formulario con estilo moderno y colores pastel usando TailwindCSS.

🔑 Notas importantes

    La conexión con Neon debe estar permitida para la IP del host donde se ejecuta la app (Render o local).

    Asegúrate de que langchain_groq esté incluido en tu requirements.txt.

    La carpeta templates debe estar dentro de app/ y contener front.html.

📝 Dependencias principales

    Flask

    psycopg2

    python-dotenv

    langchain-groq

    jinja2 (para templates)

👤 Autor

Itxaso Campos Molina
Email: itxas.77@gmail.com

Tel: (+34) 652 710 083## BidAI_app