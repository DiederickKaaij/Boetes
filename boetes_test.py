import unittest
from boetes import hoogteBoete

class TestBoetes(unittest.TestCase):
    def test_boetes1(self):
        result = hoogteBoete(45)
        self.assertEqual(result, "OK")

    def test_boetes2(self):
        result = hoogteBoete(65)
        self.assertEqual(result, 30)
    
    def test_boetes3(self):
        result = hoogteBoete(90)
        self.assertEqual(result, "Rijbewijs ingenomen")

    def test_boetes4(self):
        result = hoogteBoete(0)
        self.assertEqual(result, "OK")

    def test_boetes5(self):
        result = hoogteBoete(50)
        self.assertEqual(result, "OK")

    def test_boetes6(self):
        result = hoogteBoete(80)
        self.assertEqual(result, 60)
    
    def test_boetes7(self):
        result = hoogteBoete(58)
        self.assertEqual(result, 10)
    
if __name__ == '__main__':
    unittest.main()