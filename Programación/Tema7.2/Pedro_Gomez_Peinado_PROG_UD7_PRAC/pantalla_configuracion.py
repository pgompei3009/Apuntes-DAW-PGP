import tkinter as tk


class PantallaConfig(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app

        # --- IDIOMA ---
        self.label_idioma = tk.Label(self)
        self.label_idioma.pack(pady=(15, 5))

        self.idioma_var = tk.StringVar()
        self.menu_idioma = tk.OptionMenu(self, self.idioma_var, "")
        self.menu_idioma.pack()

        # --- ALBUMES ---
        self.label_albums = tk.Label(self)
        self.label_albums.pack(pady=(20, 10))

        self.frame_albums = tk.Frame(self)
        self.frame_albums.pack()

        self.album_vars = {}

        # --- BOTONES ---
        self.boton_guardar = tk.Button(self, command=self.guardar, width=20)
        self.boton_guardar.pack(pady=15)

        self.boton_volver = tk.Button(
            self,
            command=lambda: self.app.mostrar(self.app.p_inicio),
            width=20
        )
        self.boton_volver.pack()

    def cargar_valores(self):
        # Idioma
        self.idioma_var.set(self.app.config["idioma"])

        # Limpiar checkboxes
        for widget in self.frame_albums.winfo_children():
            widget.destroy()

        self.album_vars.clear()

        albums_config = self.app.config.get("albums", [])

        for nombre_album in self.app.versos:

            var = tk.BooleanVar()
            var.set(nombre_album in albums_config)

            chk = tk.Checkbutton(
                self.frame_albums,
                text=nombre_album,
                variable=var
            )
            chk.pack(anchor="w")

            self.album_vars[nombre_album] = var

        self.actualizar()

    def actualizar(self):
        self.label_idioma.config(text=self.app.t("config_titulo_idioma"))
        self.label_albums.config(text=self.app.t("config_titulo_albums"))
        self.boton_guardar.config(text=self.app.t("config_guardar"))
        self.boton_volver.config(text=self.app.t("config_volver"))

        # Menú idioma
        menu = self.menu_idioma["menu"]
        menu.delete(0, "end")

        opciones = [
            ("ES", self.app.t("idioma_es")),
            ("EN", self.app.t("idioma_en")),
            ("AN", self.app.t("idioma_an"))
        ]

        for codigo, texto_visible in opciones:
            menu.add_command(
                label=texto_visible,
                command=lambda c=codigo: self.idioma_var.set(c)
            )

    def guardar(self):
        self.app.config["idioma"] = self.idioma_var.get()

        seleccionados = [
            nombre for nombre, var in self.album_vars.items() if var.get()
        ]

        if not seleccionados:
            return

        self.app.config["albums"] = seleccionados

        self.app.guardar_config()
        self.app.mostrar(self.app.p_inicio)