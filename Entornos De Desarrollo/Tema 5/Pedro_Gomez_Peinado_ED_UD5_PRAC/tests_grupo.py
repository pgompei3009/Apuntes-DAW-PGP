import unittest
from estudiante import Estudiante
from grupo import Grupo


class TestGrupo(unittest.TestCase):
    def test_agregar(self):
        grupo = Grupo(1, 'DAW1')
        est1 = Estudiante(1, 'Joselito', [5.0, 7.5, 6.0])

        grupo.agregar(est1)
        self.assertEqual(len(grupo.estudiantes), 1)

    def test_eliminar(self):
        grupo = Grupo(1, 'DAW1')
        est1 = Estudiante(1, 'Joselito', [5.0, 7.5, 6.0])
        est2 = Estudiante(2, 'Fabio', [3.0, 0.0, 4.0])

        grupo.agregar(est1)
        grupo.agregar(est2)

        grupo.eliminar(1)
        
        self.assertEqual(len(grupo.estudiantes), 1)
        self.assertEqual(grupo.estudiantes[0], est2)

    def test_buscar_por_id(self):
        grupo = Grupo(1, 'DAW1')
        est1 = Estudiante(1, 'Joselito', [5.0, 7.5, 6.0])
        est2 = Estudiante(2, 'Fabio', [3.0, 0.0, 3.0])
        est1000 = Estudiante(67, 'El Hacker de los ejecicios de Borja', [10.0, 10.0, 10.0])

        grupo.agregar(est1)
        grupo.agregar(est2)
        grupo.agregar(est1000)

        self.assertEqual(grupo.buscar_por_id(67), est1000)

    def test_promocionados(self):
        grupo = Grupo(1, 'DAW1')
        est1 = Estudiante(1, 'Joselito', [5.0, 7.0, 6.0])
        est2 = Estudiante(2, 'Fabio', [3.0, 0.0, 3.0])
        est1000 = Estudiante(67, 'El Hacker de los ejecicios de Borja', [10.0, 10.0, 10.0])

        grupo.agregar(est1)
        grupo.agregar(est2)
        grupo.agregar(est1000)

        self.assertEqual(grupo.promocionados(), [est1, est1000])

    def test_ordenar_por_media(self):
        grupo = Grupo(1, 'DAW1')
        est1 = Estudiante(1, 'Joselito', [5.0, 7.0, 6.0])
        est2 = Estudiante(2, 'Fabio', [3.0, 0.0, 3.0])
        est1000 = Estudiante(67, 'El Hacker de los ejecicios de Borja', [10.0, 10.0, 10.0])

        grupo.agregar(est1)
        grupo.agregar(est2)
        grupo.agregar(est1000)

        grupo.estudiantes = grupo.ordenar_por_media()
        self.assertAlmostEqual(grupo.estudiantes, [est2, est1, est1000])

    def test_media_grupo(self):
        grupo = Grupo(1, 'DAW1')
        est1 = Estudiante(1, 'Joselito', [5.0, 7.0, 6.0])
        est4 = Estudiante(4, 'Míngzi', [5.0, 5.0, 5.0])
        est1000 = Estudiante(67, 'El Hacker de los ejecicios de Borja', [10.0, 10.0, 10.0])

        grupo.agregar(est1)
        grupo.agregar(est4)
        grupo.agregar(est1000)

        self.assertEqual(grupo.media_grupo(), 7.0)

if __name__ == "__main__":
    unittest.main()