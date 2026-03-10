from datetime import date, timedelta
from Mantecado import Mantecado
from datos import get_mantecados


class Almacen:
    def __init__(self, id: int, direccion: str, mantecados: list[Mantecado] | None = None):
        self.id = id
        self.direccion = direccion
        self.mantecados = mantecados


    def total_mantecados(self) -> int:
        return len(self.mantecados)
    

    def añadir_mantecado(self, m: Mantecado) -> None:
        self.mantecados.append(m)


    def eliminar_mantecado(self, id_mantecado: int) -> bool:
        for m in self.mantecados:
            if m.id == id_mantecado:
                self.mantecados.remove(m)
                return True
        return False


    def mantecados_caducados(self) -> list[Mantecado]:
        mantecados_caducados = []

        for m in self.mantecados:
            if Mantecado.esta_caducado(m) == True:
                mantecados_caducados.append(m)
        
        return mantecados_caducados


    def proximos_a_caducar(self, n: int) -> list[Mantecado]:
        mantecados_proximos = []

        for m in self.mantecados:
            if Mantecado.dias_para_caducar(m) <= n and Mantecado.dias_para_caducar(m) >= 0:
                mantecados_proximos.append(m)
        return mantecados_proximos

            
    def mantecads_en_rango_precio(self, minimo: float, maximo: float) -> list[Mantecado]:
        mantecados_filtrados = []

        for m in self.mantecados:
            if m.precio >= minimo and m.precio <= maximo:
                mantecados_filtrados.append(m)
        return mantecados_filtrados
    

    def sin_ingrediente(self, ingrediente: str) -> list[Mantecado]:
        ingrediente_free = []

        for m in self.mantecados:
            if ingrediente not in m.ingredientes:
                ingrediente_free.append(m)
        return ingrediente_free
    

    def reporte_por_ingrediente(self) -> dict[str, int]:
        reporte = {}

        for m in self.mantecados:
            for i in m.ingredientes:
                reporte[i] = reporte.get(i, 0) + 1
        return reporte


    def reporte_por_tipo(self) -> dict[str, int]:
        reporte = {}

        for m in self.mantecados:
            if m.tipo not in reporte:
                reporte[m.tipo] = 1
            else:
                reporte[m.tipo] += 1
        return reporte

        
if __name__ == "__main__":
    lista_mantecados = get_mantecados(0)
    almacen_mantecados = Almacen(1, "hola que tal", lista_mantecados)

    print("===== ESTADO INICIAL =====")
    print(f"Total mantecados: {Almacen.total_mantecados(almacen_mantecados)}\n")

    print("Eliminando mantecado con id 3...")
    print(f"Eliminado: {Almacen.eliminar_mantecado(almacen_mantecados, 3)}")
    print(f"Total tras eliminar: {Almacen.total_mantecados(almacen_mantecados)}\n")

    print("Añadiendo nuevo mantecado...")
    hoy = date.today()
    nuevo_mantecado = Mantecado(99, "especial_navidad", hoy, hoy + timedelta(days=20), 4, ["harina", "manteca", "miel"])
    Almacen.añadir_mantecado(almacen_mantecados, nuevo_mantecado)
    print(f"Total tras añadir: {Almacen.total_mantecados(almacen_mantecados)}\n")

    print("===== CADUCADOS =====")
    caducados = Almacen.mantecados_caducados(almacen_mantecados)
    [print(f"{m.id} {m.tipo}") for m in caducados]

    print("\n===== PRÓXIMOS A CADUCAR (>= 3 días) =====")
    proximos = Almacen.proximos_a_caducar(almacen_mantecados, 3)
    [print(f"{m.id} {m.tipo}") for m in proximos]

    print("\n===== RANGO DE PRECIO (2.0 - 3.0) =====")
    filtrados_precios = Almacen.mantecads_en_rango_precio(almacen_mantecados, 2, 3)
    [print(f"{m.id} {m.tipo} {m.precio}") for m in filtrados_precios]

    print("\n===== SIN AZUCAR =====")
    sin_azucar = Almacen.sin_ingrediente(almacen_mantecados, "azucar")
    [print(f"{m.id} {m.tipo}") for m in sin_azucar]

    print("\n===== REPORTE POR INGREDIENTE =====")
    reporte_ingrediente = Almacen.reporte_por_ingrediente(almacen_mantecados)
    [print(f"{ingrediente} -> {cantidad}") for ingrediente, cantidad in reporte_ingrediente.items()]

    print("\n===== REPORTE POR TIPO =====")
    reporte_tipo = Almacen.reporte_por_tipo(almacen_mantecados)
    [print(f"{tipo} -> {cantidad}") for tipo, cantidad in reporte_tipo.items()]



