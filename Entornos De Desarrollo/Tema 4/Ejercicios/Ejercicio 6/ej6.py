class B:
    def __init__(self, nombre: str, notas: list):
        self.a1 = nombre
        self.a2 = notas


    def aprobado(self) -> bool:
        for n in self.notas:
            if n[1] < 5:
                return False
        return True


    def media_de_notas(self) -> float:
        if len(self.notas) == 0:
            return 0
        sumatoria = 0
        for n in self.notas:
            sumatoria += n[1]
        return sumatoria / len(self.notas)


    def listar_suspensos(self) -> list:
        suspensos = []
        for n in self.notas:
            if n[1] < 5:
                suspensos.append(n[0])
        return r


    def m4(self) -> int:
        c = 0
        for p in self.a2:
            if p[1] >= 5:
                c += p[0].a2
        return c

    def __str__(self) -> str:
        return self.a1
