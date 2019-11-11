from django.test import TestCase

# Create your tests here.
import unittest

class Pruebas(unittest.TestCase):
    def test(self):
        pass

if __name__ == "__main__":
    unittest.main()


import unittest

def doblar(a): return a*2
def sumar(a,b): return a+b  
def es_par(a): return 1 if a%2 == 0 else 0

class PruebasFunciones(unittest.TestCase):

    def test_doblar(self):
        self.assertEqual(doblar(10), 20)
        self.assertEqual(doblar('Ab'), 'AbAb')

    def test_sumar(self):
        self.assertEqual(sumar(-15, 15), 0)
        self.assertEqual(sumar('Ab' ,'cd'), 'Abcd')

    def test_es_par(self):
        self.assertEqual(es_par(11), False)
        self.assertEqual(es_par(68), True)


if __name__ == '__main__':
    unittest.main()
    import unittest

class PruebasMetodosCadenas(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('hola'.upper(), 'HOLA')

    def test_isupper(self):
        self.assertTrue('HOLA'.isupper())
        self.assertFalse('Hola'.isupper())

    def test_split(self):
        s = 'Hola mundo'
        self.assertEqual(s.split(), ['Hola', 'mundo'])


if __name__ == '__main__':
    unittest.main()

import unittest


class PruebaTestFixture(unittest.TestCase):

    def setUp(self):
        print("Preparando el contexto")
        self.numeros = [1, 2, 3, 4, 5]

    def test(self):
        print("Realizando una prueba")
        r = [doblar(n) for n in self.numeros]
        self.assertEqual(r, [2, 4, 6, 8, 10])

    def tearDown(self):
        print("Destruyendo el contexto")
        del(self.numeros)


if __name__ == '__main__':
    unittest.main() 