import random
import tkinter as tk


class PantallaJuego(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app

        self.vidas = 3
        self.cancion_actual = None
        self.verso_actual = None

        # Resumen
        self.label_resumen = tk.Label(self, font=("Arial", 14))
        self.label_resumen.pack(pady=20)

        # Verso
        self.label_verso = tk.Label(self, text="", font=("Arial", 14), wraplength=600)
        self.label_verso.pack(pady=20)

        # Input usuario
        self.entry_respuesta = tk.Entry(self, justify="center", width=40)
        self.entry_respuesta.pack(pady=10)

        # Botón comprobar
        self.boton_comprobar = tk.Button(self, command=self.comprobar, width=20)
        self.boton_comprobar.pack(pady=10)

        # Resultado
        self.label_resultado = tk.Label(self, text="", font=("Arial", 14, "bold"))
        self.label_resultado.pack(pady=10)

        # Botón siguiente
        self.boton_siguiente = tk.Button(self, command=self.nueva_ronda, width=20)
        self.boton_siguiente.pack(pady=10)

        # Volver
        self.boton_volver = tk.Button(
            self,
            command=lambda: self.app.mostrar(self.app.p_inicio),
            width=20
        )
        self.boton_volver.pack(pady=10)

    def actualizar(self):
        self.boton_comprobar.config(text=self.app.t("juego_comprobar"))
        self.boton_siguiente.config(text=self.app.t("juego_siguiente"))
        self.boton_volver.config(text=self.app.t("juego_volver"))

        self.nueva_ronda()

    def nueva_ronda(self):
        # Limpiar UI
        self.entry_respuesta.delete(0, tk.END)
        self.label_resultado.config(text="")

        # Obtener álbumes seleccionados
        albums_seleccionados = self.app.config.get("albums", [])

        # Filtrar canciones
        canciones = []

        for album in albums_seleccionados:
            if album in self.app.versos:
                canciones.extend(self.app.versos[album])

        # Seguridad
        if not canciones:
            self.label_verso.config(text="No hay canciones disponibles")
            return

        # Elegir canción aleatoria
        cancion_dict = random.choice(canciones)

        # Extraer título y verso
        self.cancion_actual = list(cancion_dict.keys())[0]
        self.verso_actual = cancion_dict[self.cancion_actual]

        # Mostrar verso
        self.label_verso.config(text=self.verso_actual)

        # Mostrar resumen
        self.label_resumen.config(text=f"Vidas: {self.vidas}")

    def comprobar(self):
        respuesta = self.entry_respuesta.get().strip()

        if respuesta.lower() == self.cancion_actual.lower():
            self.label_resultado.config(
                text=self.app.t("juego_correcto")
            )
        else:
            self.label_resultado.config(
                text=self.app.t("juego_fallaste")
            )
            self.vidas -= 1
            self.label_resumen.config(text=f"Vidas: {self.vidas}")
            if self.vidas == 0:
                self.label_resultado.config(text="Fin de la partida")
                self.boton_siguiente.config(state="disabled")
                self.boton_comprobar.config(state="disabled")