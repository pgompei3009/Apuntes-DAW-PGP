import unittest
from estudiante import Estudiante

class TestEstudiante(unittest.TestCase):
    def test_media(self):     
        est1 = Estudiante(1, 'Joselito', [5.0, 7.0, 6.0])
        est1000 = Estudiante(67, 'El Hacker de los ejecicios de Borja', [10.0, 10.0, 10.0])
        
        self.assertEqual(est1.media(), 6.0)
        self.assertEqual(est1000.media(), 10.0)

    def test_promocionar(self):
        est2 = Estudiante(2, 'Fabio', [3.0, 0.0, 3.0])
        est3 = Estudiante(3, 'Emilio', [6.0, 5.0, 5.0])

        self.assertFalse(est2.promocionar())
        self.assertTrue(est3.promocionar())

    def test_anadir_nota(self):
        est1 = Estudiante(1, 'Joselito', [5.0, 7.0, 6.0])

        est1.anadir_nota(10.0)
        self.assertEqual(len(est1.notas), 4)

if __name__ == "__main__":
    unittest.main()