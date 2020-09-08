import unittest                       #Importo el modulo de prueba UnitTest

class TestBasica(unittest.TestCase): #creo una clase y heredo TestCase que viene dentro de unitTest

    def test_es_menor_que(self):     #creo un metodo de prueba
        self.assertTrue(1 < 3)       #hago el assert, en este caso elegi el True

if __name__ == "__main__":
    unittest.main()