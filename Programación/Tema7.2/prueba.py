import tkinter as tk
import math

ANCHO = 600
ALTO = 700

class BulletHell:
    def __init__(self, root):
        self.root = root
        self.root.title("💀 Bullet Hell INSANO")

        self.canvas = tk.Canvas(root, width=ANCHO, height=ALTO, bg="#0d0d0d")
        self.canvas.pack()

        self.jugador = {"x": ANCHO//2, "y": ALTO-80}
        self.balas = []
        self.balas_enemigas = []
        self.enemigo = {"x": ANCHO//2, "y": 100, "vida": 200}

        self.teclas = set()
        self.frame = 0
        self.game_over = False

        self.patron = 0
        self.angulo_base = 0

        self.root.bind("<KeyPress>", self.key_down)
        self.root.bind("<KeyRelease>", self.key_up)

        self.loop()

    def key_down(self, e):
        self.teclas.add(e.keysym.lower())

    def key_up(self, e):
        self.teclas.discard(e.keysym.lower())

    def mover_jugador(self):
        speed = 5
        if "w" in self.teclas: self.jugador["y"] -= speed
        if "s" in self.teclas: self.jugador["y"] += speed
        if "a" in self.teclas: self.jugador["x"] -= speed
        if "d" in self.teclas: self.jugador["x"] += speed

        self.jugador["x"] = max(0, min(ANCHO, self.jugador["x"]))
        self.jugador["y"] = max(0, min(ALTO, self.jugador["y"]))

    def disparar(self):
        if self.frame % 4 == 0:
            self.balas.append([self.jugador["x"], self.jugador["y"], -12])

    def disparo_enemigo(self):
        x = self.enemigo["x"]
        y = self.enemigo["y"]

        if self.frame % 250 == 0:
            self.patron = (self.patron + 1) % 3

        # 🔥 PATRÓN 1: círculo ultra denso y rápido
        if self.patron == 0:
            if self.frame % 6 == 0:
                for ang in range(0, 360, 10):  # antes 30 → más denso
                    rad = math.radians(ang + self.angulo_base)
                    dx = math.cos(rad) * 5   # más velocidad
                    dy = math.sin(rad) * 5
                    self.balas_enemigas.append([x, y, dx, dy])
            self.angulo_base += 8  # gira más rápido

        # 🔥 PATRÓN 2: espiral infernal
        elif self.patron == 1:
            if self.frame % 2 == 0:
                rad = math.radians(self.angulo_base)
                dx = math.cos(rad) * 6
                dy = math.sin(rad) * 6
                self.balas_enemigas.append([x, y, dx, dy])
                self.angulo_base += 15  # espiral más cerrada

        # 🔥 PATRÓN 3: lluvia MUY densa
        elif self.patron == 2:
            if self.frame % 3 == 0:
                for i in range(-6, 7):  # más ancho
                    self.balas_enemigas.append([x + i*10, y, i*0.7, 6])

    def mover_balas(self):
        nuevas = []
        for x, y, dy in self.balas:
            y += dy
            if y > 0:
                nuevas.append([x, y, dy])
        self.balas = nuevas

        nuevas = []
        for x, y, dx, dy in self.balas_enemigas:
            x += dx
            y += dy
            if 0 < x < ANCHO and 0 < y < ALTO:
                nuevas.append([x, y, dx, dy])
        self.balas_enemigas = nuevas

    def colisiones(self):
        px, py = self.jugador["x"], self.jugador["y"]

        for x, y, _, _ in self.balas_enemigas:
            if abs(x - px) < 6:
                if abs(y - py) < 6:
                    self.game_over = True

        nuevas = []
        for x, y, dy in self.balas:
            if abs(x - self.enemigo["x"]) < 15 and abs(y - self.enemigo["y"]) < 15:
                self.enemigo["vida"] -= 1
            else:
                nuevas.append([x, y, dy])
        self.balas = nuevas

        if self.enemigo["vida"] <= 0:
            self.game_over = True

    def dibujar(self):
        self.canvas.delete("all")

        x, y = self.jugador["x"], self.jugador["y"]
        self.canvas.create_oval(x-4, y-4, x+4, y+4, fill="#00ffcc", outline="")

        for x, y, _ in self.balas:
            self.canvas.create_rectangle(x-2, y-6, x+2, y+6, fill="#39ff14", outline="")

        for x, y, _, _ in self.balas_enemigas:
            self.canvas.create_oval(x-3, y-3, x+3, y+3, fill="#ff0033", outline="")

        if self.enemigo["vida"] > 0:
            e = self.enemigo
            self.canvas.create_rectangle(e["x"]-15, e["y"]-15, e["x"]+15, e["y"]+15, fill="#ff00ff")

            self.canvas.create_text(10, 10, anchor="nw",
                                    text=f"Boss HP: {e['vida']}",
                                    fill="white")

        if self.game_over:
            texto = "🏆 GANASTE 🏆" if self.enemigo["vida"] <= 0 else "💀 GAME OVER 💀"
            self.canvas.create_text(ANCHO//2, ALTO//2,
                                    text=texto,
                                    fill="red",
                                    font=("Arial", 30, "bold"))

    def loop(self):
        if not self.game_over:
            self.mover_jugador()
            self.disparar()
            self.disparo_enemigo()
            self.mover_balas()
            self.colisiones()

        self.dibujar()
        self.frame += 1
        self.root.after(16, self.loop)

root = tk.Tk()
game = BulletHell(root)
root.mainloop()