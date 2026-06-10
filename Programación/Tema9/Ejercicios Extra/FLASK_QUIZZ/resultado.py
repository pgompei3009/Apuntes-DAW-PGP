from flask import request, render_template, current_app
import sqlite3

def get_db_conn():
    return sqlite3.connect(current_app.config["DATABASE"])

def resultado():
    conn = get_db_conn()
    cur = conn.cursor()

    # Obtener todas las preguntas
    cur.execute("SELECT id FROM questions ORDER BY id")
    question_ids = [row[0] for row in cur.fetchall()]

    correctas = 0
    total = len(question_ids)
    resultados = []

    for qid in question_ids:
        # Respuesta elegida por el usuario
        respuesta_id = request.form.get(f"question_{qid}")

        # Texto de la pregunta
        cur.execute("SELECT texto FROM questions WHERE id = ?", (qid,))
        qtext = cur.execute("SELECT texto FROM questions WHERE id = ?", (qid,)).fetchone()[0]

        # Opción correcta
        cur.execute("SELECT id, texto FROM options WHERE question_id = ? AND is_correct = 1", (qid,))
        correcta = cur.fetchone()

        # Opción elegida
        opcion_elegida = None
        if respuesta_id:
            cur.execute("SELECT texto FROM options WHERE id = ?", (respuesta_id,))
            row = cur.fetchone()
            opcion_elegida = row[0] if row else None

        es_correcta = respuesta_id and int(respuesta_id) == correcta[0]
        if es_correcta:
            correctas += 1

        resultados.append({
            "pregunta": qtext,
            "elegida": opcion_elegida or "Sin respuesta",
            "correcta": correcta[1] if correcta else "?",
            "es_correcta": es_correcta
        })

    conn.close()

    porcentaje = round((correctas / total) * 100) if total > 0 else 0

    # Mensaje temático según puntuación
    if porcentaje == 100:
        mensaje = "¡Eres un verdadero maestro de los videojuegos! 🏆"
        rango = "S"
    elif porcentaje >= 75:
        mensaje = "¡Gran partida! Tienes nivel de jugador experto. 🎮"
        rango = "A"
    elif porcentaje >= 50:
        mensaje = "Nada mal, pero aún te queda grinding por hacer. ⚔️"
        rango = "B"
    elif porcentaje >= 25:
        mensaje = "Parece que necesitas más horas de juego. 🕹️"
        rango = "C"
    else:
        mensaje = "Game Over... ¡Vuelve a intentarlo! 💀"
        rango = "D"

    return render_template(
        "resultado.html",
        correctas=correctas,
        total=total,
        porcentaje=porcentaje,
        mensaje=mensaje,
        rango=rango,
        resultados=resultados
    )