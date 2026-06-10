import tkinter as tk
from tkinter import ttk, messagebox
import random
import json
import os

CONFIG_FILE = "config.json"

DEFAULT_CONFIG = {
    "dice_type": "D6",
    "language": "es"
}

LANGUAGES = {
    "es": {
        "start": "Empezar",
        "config": "Configuración",
        "roll": "Tirar",
        "result": "Resultado",
        "back": "Volver",
        "dice": "Tipo de dado (ej: D6, D10, D20)",
        "language": "Idioma",
        "save": "Guardar",
        "error_dice": "Introduce un dado válido (ej: D6, D20...)"
    },
    "en": {
        "start": "Start",
        "config": "Settings",
        "roll": "Roll",
        "result": "Result",
        "back": "Back",
        "dice": "Dice type (e.g: D6, D10, D20)",
        "language": "Language",
        "save": "Save",
        "error_dice": "Enter a valid dice (e.g: D6, D20...)"
    },
    "an": {
        "start": "Enga pa'lante",
        "config": "Amo a cambia'",
        "roll": "Que rule!",
        "result": "Resurtao",
        "back": "Pa' tra'",
        "dice": "Tipo der dao (illo un D6 y esas cosas)",
        "language": "Idioma",
        "save": "Queate con esto!",
        "error_dice": "Cuxa, la q ha' liao pollito"
    }
}


def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return DEFAULT_CONFIG.copy()


def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)


class DiceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Dados")
        self.config = load_config()

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill="both", expand=True)

        self.show_main_menu()

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def t(self, key):
        return LANGUAGES[self.config["language"]][key]

    def get_dice_sides(self):
        try:
            return int(self.config["dice_type"][1:])
        except:
            return 6

    def show_main_menu(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Juego de Dados", font=("Arial", 18)).pack(pady=20)

        tk.Button(self.main_frame, text=self.t("start"), width=20, command=self.show_game).pack(pady=10)
        tk.Button(self.main_frame, text=self.t("config"), width=20, command=self.show_config).pack(pady=10)

    def show_game(self):
        self.clear_frame()

        self.result_label = tk.Label(self.main_frame, text="-", font=("Arial", 24))
        self.result_label.pack(pady=20)

        self.dice_label = tk.Label(self.main_frame, text=self.config["dice_type"], font=("Arial", 14))
        self.dice_label.pack(pady=5)

        tk.Button(self.main_frame, text=self.t("roll"), command=self.roll_dice).pack(pady=10)
        tk.Button(self.main_frame, text=self.t("back"), command=self.show_main_menu).pack(pady=10)

    def roll_dice(self):
        sides = self.get_dice_sides()
        result = random.randint(1, sides)
        self.result_label.config(text=f"{self.t('result')}: {result}")

    def show_config(self):
        self.clear_frame()

        tk.Label(self.main_frame, text=self.t("dice")).pack(pady=5)
        dice_var = tk.StringVar(value=self.config["dice_type"])
        dice_entry = tk.Entry(self.main_frame, textvariable=dice_var)
        dice_entry.pack(pady=5)

        tk.Label(self.main_frame, text=self.t("language")).pack(pady=5)
        lang_var = tk.StringVar(value=self.config["language"])
        lang_menu = ttk.Combobox(self.main_frame, textvariable=lang_var, values=list(LANGUAGES.keys()), state="readonly")
        lang_menu.pack(pady=5)

        def valid_dice(value):
            value = value.upper()
            if value.startswith("D") and value[1:].isdigit():
                return True
            return False

        def save_and_back():
            dice_value = dice_var.get().upper()

            if not valid_dice(dice_value):
                messagebox.showerror("Error", self.t("error_dice"))
                return

            self.config["dice_type"] = dice_value
            self.config["language"] = lang_var.get()
            save_config(self.config)
            self.show_main_menu()

        tk.Button(self.main_frame, text=self.t("save"), command=save_and_back).pack(pady=10)
        tk.Button(self.main_frame, text=self.t("back"), command=self.show_main_menu).pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = DiceApp(root)
    root.mainloop()