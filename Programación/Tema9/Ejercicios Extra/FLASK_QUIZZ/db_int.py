import sqlite3
import os

DB_PATH = os.path.join("data", "quiz.db")

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Crear tablas
    cur.executescript("""
        DROP TABLE IF EXISTS options;
        DROP TABLE IF EXISTS questions;

        CREATE TABLE questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto TEXT NOT NULL
        );

        CREATE TABLE options (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_id INTEGER NOT NULL,
            texto TEXT NOT NULL,
            is_correct INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY (question_id) REFERENCES questions(id)
        );
    """)

    # Preguntas y respuestas
    preguntas = [
        {
            "texto": "¿En qué año se lanzó el primer The Legend of Zelda?",
            "opciones": [
                ("1983", 0),
                ("1986", 1),
                ("1989", 0),
                ("1991", 0),
            ]
        },
        {
            "texto": "¿Cuál es el nombre del protagonista de la saga Dark Souls?",
            "opciones": [
                ("El No-Muerto Elegido", 1),
                ("El Cazador", 0),
                ("El Sin Nombre", 0),
                ("Solaire de Astora", 0),
            ]
        },
        {
            "texto": "¿Qué compañía desarrolló la saga Halo originalmente?",
            "opciones": [
                ("343 Industries", 0),
                ("Epic Games", 0),
                ("Bungie", 1),
                ("id Software", 0),
            ]
        },
        {
            "texto": "¿En qué videojuego aparece el personaje Kratos?",
            "opciones": [
                ("Devil May Cry", 0),
                ("God of War", 1),
                ("Bayonetta", 0),
                ("Dante's Inferno", 0),
            ]
        },
        {
            "texto": "¿Cuál fue la primera consola de Sony?",
            "opciones": [
                ("PlayStation 2", 0),
                ("PlayStation Portable", 0),
                ("PlayStation", 1),
                ("Sony Saturn", 0),
            ]
        },
        {
            "texto": "¿Qué objeto recoge Mario para hacerse grande?",
            "opciones": [
                ("Estrella", 0),
                ("Champiñón", 1),
                ("Flor de fuego", 0),
                ("Moneda", 0),
            ]
        },
        {
            "texto": "¿En qué saga aparece el personaje \"Master Chief\"?",
            "opciones": [
                ("Call of Duty", 0),
                ("Gears of War", 0),
                ("Halo", 1),
                ("Destiny", 0),
            ]
        },
        {
            "texto": "¿Qué estudio desarrolló The Witcher 3?",
            "opciones": [
                ("Bioware", 0),
                ("CD Projekt Red", 1),
                ("Bethesda", 0),
                ("Obsidian", 0),
            ]
        },
    ]

    for pregunta in preguntas:
        cur.execute("INSERT INTO questions (texto) VALUES (?)", (pregunta["texto"],))
        qid = cur.lastrowid
        for texto, is_correct in pregunta["opciones"]:
            cur.execute(
                "INSERT INTO options (question_id, texto, is_correct) VALUES (?, ?, ?)",
                (qid, texto, is_correct)
            )

    conn.commit()
    conn.close()
    print("✅ Base de datos creada correctamente en", DB_PATH)

if __name__ == "__main__":
    init_db()