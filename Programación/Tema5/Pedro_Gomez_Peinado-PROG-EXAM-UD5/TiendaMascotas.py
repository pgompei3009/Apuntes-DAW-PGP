from Mascota import Mascota
from datos import get_datos


class TiendaMascotas:
    def __init__(self, id: int, nombre: str, dirección: str, mascotas: list[Mascota]):
        self.id = id
        self.nombre = nombre
        self.direccion = dirección

        disponibles = []
        vendidas = []

        for m in mascotas:
            if m.fecha_venta is None:
                disponibles.append(m)
            else:
                vendidas.append(m)

        self.disponibles = disponibles
        self.vendidas = vendidas

    def añadir_mascota(self, mascota: Mascota) -> None:
        if mascota.fecha_venta is None:
            self.disponibles.append(mascota)
        else:
            self.vendidas.append(mascota)

    def eliminar_mascota(self, id: int) -> bool:
        for m in self.disponibles + self.vendidas:
            if m.id == id:
                (self.disponibles + self.vendidas).remove(m)
                return True
        return False

    def mascotas_rango_precio(self, a: float, b: float) -> list[Mascota]:
        mascotas_filtradas = []
        for m in self.disponibles:
            if m.precio >= a and m.precio <= b:
                mascotas_filtradas.append(m)
        return mascotas_filtradas
    
    def no_necesitan_vacunas(self) -> list[Mascota]:
        mascotas_filtradas = []
        for m in self.disponibles:
            if Mascota.se_vacuna(m) == False:
                mascotas_filtradas.append(m)
        return mascotas_filtradas
    
    def mas_antiguas(self) -> list[Mascota]:
        fechas = sorted([m.fecha_entrada for m in self.disponibles])
        mascotas_ordenadas = []
        for f in fechas:
            for m in self.disponibles:
                if m.fecha_entrada == f:
                    mascotas_ordenadas.append(m)
                    break
        return mascotas_ordenadas
    
    def mascotas_por_tipo(self, tipo: str) -> list[Mascota]:
        return [m for m in self.disponibles if m.tipo == tipo]
    
    def mascotas_por_tipos(self, tipos: list[str]) -> list[Mascota]:
        return [m for m in self.disponibles if m.tipo in tipos]
    
    def actualizar_precio_por_tipo(self, tipo: str, porcentaje: float) -> None:
        for m in self.disponibles:
            if m.tipo == tipo:
                m.precio *= 1 + porcentaje

    def reporte_por_tipo(self) -> dict[str, dict[str, float]]:
        reporte = {}
        for m in self.vendidas:     
            if m.tipo not in reporte:
                reporte[m.tipo] = {'num_vendido': 0, 'ganancias': 0}
            reporte[m.tipo]['num_vendido'] += m.precio
            reporte[m.tipo]['ganancias'] += 1
        return reporte


if __name__ == '__main__':
    from datetime import datetime

    mascotas = get_datos()
    tiendita = TiendaMascotas(1, 'Tienda Molona', 'Calle Zarza 87', mascotas)

    print('=== DISPONIBLES ===')
    [print(m) for m in tiendita.disponibles]

    print('\n=== VENDIDAS ===')
    [print(m) for m in tiendita.vendidas]

    print('\n=== MACOTAS EN RANGO DE PRECIO (100 - 200) ===')
    id_animalitos = [m.id for m in TiendaMascotas.mascotas_rango_precio(tiendita, 100, 200)]
    print(id_animalitos)

    print('\n=== NO NECESITAN VACUNAS ===')
    id_animalitos = [m.id for m in TiendaMascotas.no_necesitan_vacunas(tiendita)]
    print(id_animalitos)

    print('\n=== MÁS ANTIGUAS (ordenadas por fecha de entrada) ===')
    id_animalitos = [m.id for m in TiendaMascotas.mas_antiguas(tiendita)]
    print(id_animalitos)

    print('\n=== MASCOTAS POR TIPO "Gato" ===')
    id_animalitos = [m.id for m in TiendaMascotas.mascotas_por_tipo(tiendita, 'Gato')]
    print(id_animalitos)

    print('\n=== MASCOTAS POR TIPOS ["Gato", "Erizo"] ===')
    id_animalitos = [m.id for m in TiendaMascotas.mascotas_por_tipos(tiendita, ['Gato', 'Erizo'])]
    print(id_animalitos)

    print('\n=== ACTUALIZAR PRECIO +10% A LOS GATOS ===')
    TiendaMascotas.actualizar_precio_por_tipo(tiendita, 'Gato', 0.1)
    animalitos_actualizados = [(m.id, m.precio) for m in tiendita.disponibles if m.tipo == 'Gato']
    print(animalitos_actualizados)

    print('\n=== REPORTE POR TIPO (VENDIDAS) ===')
    reporte = TiendaMascotas.reporte_por_tipo(tiendita)
    print(reporte)

    print('\n=== ELIMINAR MASCOTA ID 3 ===')
    print('Eliminada: ', TiendaMascotas.eliminar_mascota(tiendita, 3))
    print(f'IDs disponibles tras eliminar: {[m.id for m in tiendita.disponibles]}')

    print('\n=== AÑADIR NUEVA MACOTA ===')
    mascota = Mascota(99, 'a', 'a', datetime.today(), 999999.0, datetime.today(), None, None)
    TiendaMascotas.añadir_mascota(tiendita, mascota)
    print(f'IDs disponibles tras añadir: {[m.id for m in tiendita.disponibles]}')
