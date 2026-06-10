from pathlib import Path


class Reporte():
    def __init__(self, dia: str, t_minima: float, t_maxima: float, t_media: float, precipitaciones: float) -> None:
        self.dia = dia
        self.t_minima = t_minima
        self.t_maxima = t_maxima
        self.t_media = t_media
        self.precipitaciones = precipitaciones


if __name__ == '__main__':

    ruta_meteo = Path(__file__).parent / 'datos' / 'meteo.csv'
    ruta_reporte = Path(__file__).parent / 'reporte.txt'

    with open(ruta_meteo, 'r', encoding='utf-8') as f:
        sumatoria_t_min = sumatoria_t_max = sumatoria_precipitaciones = sumatoria_t_media = 0
        reportes = []
        next(f)
        for linea in f:
            linea = linea.strip()
            if linea:
                dia, t_minima, t_maxima, t_media, precipitaciones = linea.split(',')
                nuevo_reporte = Reporte(dia, float(t_minima), float(t_maxima), float(t_media), float(precipitaciones))
                reportes.append(nuevo_reporte)

                sumatoria_t_min += nuevo_reporte.t_minima
                sumatoria_t_max += nuevo_reporte.t_maxima
                sumatoria_precipitaciones += nuevo_reporte.precipitaciones
                sumatoria_t_media += nuevo_reporte.t_media

    apartado_1 = min(reportes, key=lambda r: r.t_minima)
    apartado_2 = max(reportes, key=lambda r: r.t_maxima)
    apartado_3 = round(sumatoria_t_min/len(reportes), 2)
    apartado_4 = round(sumatoria_t_max/len(reportes), 2)
    apartado_5 = round(sumatoria_precipitaciones/len(reportes), 2)
    apartado_6 = round(sumatoria_t_media/len(reportes), 2)

    with open(ruta_reporte, 'w', encoding='utf-8') as f:
        f.write('REPORTE METEOROLÓGICO\n'
                '=====================\n'
                '\n'
                'Temperatura mínima absoluta:\n'
                f'- Día: {apartado_1.dia}\n'
                f'- Temperatura: {apartado_1.t_minima} ºC\n'
                '\n'
                'Temperatura máxima absoluta:\n' \
                f'- Día: {apartado_2.dia}\n'
                f'- Temperatura: {apartado_2.t_maxima} ºC\n'
                '\n'
                f'media de temperaturas mínimas: {apartado_3} ºC\n'
                f'media de temperaturas máximas: {apartado_4} ºC\n'
                f'media de precipitaciones: {apartado_5} mm\n'
                f'media de temperaturas medias: {apartado_6} ºC\n')
        
        