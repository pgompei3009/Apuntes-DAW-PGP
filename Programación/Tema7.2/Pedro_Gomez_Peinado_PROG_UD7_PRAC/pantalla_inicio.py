import tkinter as tk


class PantallaInicio(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app

        # Título
        self.label_titulo = tk.Label(self, font=("Arial", 22, "bold"))
        self.label_titulo.pack(pady=(40, 30))

        # Botón empezar partida
        self.boton_empezar = tk.Button(
            self,
            command=lambda: self.app.mostrar(self.app.p_juego),
            width=20,
            height=2
        )
        self.boton_empezar.pack(pady=10)

        # Botón configuración
        self.boton_configurar = tk.Button(
            self,
            command=lambda: self.app.mostrar(self.app.p_config),
            width=20,
            height=2
        )
        self.boton_configurar.pack(pady=10)

    def actualizar(self):
        self.label_titulo.config(text=self.app.t("inicio_titulo"))
        self.boton_empezar.config(text=self.app.t("inicio_empezar"))
        self.boton_configurar.config(text=self.app.t("inicio_configurar"))