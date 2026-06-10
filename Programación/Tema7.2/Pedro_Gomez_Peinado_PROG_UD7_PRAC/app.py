import json
import tkinter as tk

from pathlib import Path

from pantalla_inicio import PantallaInicio
from pantalla_quizz_extremo import PantallaJuego
from pantalla_configuracion import PantallaConfig


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Extremoduro Quiz")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        # --- CARGA DE DATOS ---
        self.textos = self.cargar_textos()
        self.versos = self.cargar_versos()
        self.config = self.cargar_config()

        # --- PANTALLAS ---
        self.p_inicio = PantallaInicio(self)
        self.p_juego = PantallaJuego(self)
        self.p_config = PantallaConfig(self)

        self.pantalla_actual = None
        self.mostrar(self.p_inicio)

    # -------------------------
    # CARGA DE ARCHIVOS
    # -------------------------

    def cargar_textos(self):
        ruta = Path(__file__).parent / "textos.json"
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)

    def cargar_versos(self):
        ruta = Path(__file__).parent / "versos.json"
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)

    def cargar_config(self):
        try:
            ruta = Path(__file__).parent / "config.json"
            with open(ruta, "r", encoding="utf-8") as f:
                config = json.load(f)

            # Validaciones básicas
            if "idioma" not in config or "albums" not in config:
                raise ValueError("Configuración incompleta")

            if config["idioma"] not in self.textos:
                raise ValueError("Idioma no válido")

            return config

        except Exception:
            # Config por defecto (todos los álbumes seleccionados)
            return {
                "idioma": "ES",
                "albums": list(self.versos.keys())
            }

    def guardar_config(self):
        ruta = Path(__file__).parent / "config.json"
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(self.config, f, ensure_ascii=False, indent=4)

    # -------------------------
    # TRADUCCIONES
    # -------------------------

    def t(self, clave):
        idioma = self.config["idioma"]
        return self.textos[idioma].get(clave, clave)

    # -------------------------
    # NAVEGACIÓN ENTRE PANTALLAS
    # -------------------------

    def mostrar(self, pantalla):
        if self.pantalla_actual is not None:
            self.pantalla_actual.pack_forget()

        if hasattr(pantalla, "actualizar"):
            pantalla.actualizar()

        if hasattr(pantalla, "cargar_valores"):
            pantalla.cargar_valores()

        self.pantalla_actual = pantalla
        self.pantalla_actual.pack(fill="both", expand=True)


# -------------------------
# EJECUCIÓN
# -------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()