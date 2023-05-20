import random as rnd
class turno:
  def __init__(self):
    
    self.camiones = 3
    self.empleados = 9
  








class puntogeografico:
  def __init__(self):
    self.latitud = rnd.randint(-1000,1000)
    self.longitud = rnd.randint(-1000,1000)

class tiempo:
  def __init__(self):
    self.horas = rnd.randint(1,5)
    self.minutos = rnd.randint(0,59)
    self.segundos = rnd.randint(0,59)


class Trashcity:
  _instance = None
  def _new_(cls):
        if not cls._instance:
            cls.instance = super().new_(cls)
        return cls._instance

  def __init__(self):
    
    self.idempleados = [123,321,666,777,888,999,555,234,809,352,790,376,213]
    self.latitud = 0
    self.longitud = 0
    self.tiempo = int
    self.switch = True

    
    
  def iniciar_recoleccion(self,latitud,longitud,camiones,empleados):
    
    self.camiones = camiones
    self.empleados = empleados
    
    if self.camiones < 1 | self.empleados < 3:
      print("no se puede realizar el recorrido, no hay camiones o empleados suficientes") 
      self.switch = False
    else:
      self.camiones = self.camiones - 1
      self.longitud = longitud
      self.latitud = latitud


      
      print("Se inicio turno en la ruta con latitud",self.latitud," y longitud ",self.longitud) 
      
  def valorar_turno(self,horas,minutos,segundos):
    self.horas = horas
    self.minutos = minutos
    self.segundos = segundos
    print(" El turno demoro ",self.horas," hora(s) - ",self.minutos," minuto(s) - ",self.segundos," segundo(s)")
    print("Los empleados a cargo fueron:")
    for i in range(3):
      print("Empleado con identificacion:")
      print(self.idempleados[i])
    self.idempleados.pop(0)
    self.idempleados.pop(1)
    self.idempleados.pop(2)



      
    print("Estos empleados ya no se encuentran disponibles para turnos hoy")
    self.empleados = self.empleados - 3
    
      
      
    


      

class CentroAcopio:
  def __init__(self):
    self.vidrio = rnd.randint(1,10)
    self.papel = rnd.randint(1,10)
    self.plastico = rnd.randint(1,10)
    self.metal = rnd.randint(1,10)
    self.organicos = rnd.randint(1,10)
    self.totalvidrio = 0
  def reciclar(self):
    self.vidrio = rnd.randint(1,10)
    self.papel = rnd.randint(1,10)
    self.plastico = rnd.randint(1,10)
    self.metal = rnd.randint(1,10)
    self.organicos = rnd.randint(1,10)
    print("los empleados que acaban de terminar turno reciclaron:")
    print("vidrio: ",self.vidrio,"tonelada(s)")
    self.totalvidrio = self.totalvidrio + self.vidrio

    print("papel: ",self.papel,"tonelada(s)")
    print("plastico: ",self.plastico,"tonelada(s)")
    print("metal: ",self.metal,"tonelada(s)")
    print("organicos: ",self.organicos,"tonelada(s)")
    print("El total de vidrio hasta ahora es de",self.totalvidrio," tonelada(s)")





#-------------------------------------------------------------------------------------------------------------------------------------~#


import unittest

class TestTrashcity(unittest.TestCase):
    def test_iniciar_recoleccion(self):
        t = Trashcity()
        t.iniciar_recoleccion(10, 20, 2, 4)
        self.assertEqual(t.camiones, 1)
        self.assertEqual(t.empleados, 4)
        self.assertEqual(t.latitud, 10)
        self.assertEqual(t.longitud, 20)
        self.assertTrue(t.switch)

    def test_valorar_turno(self):
        t = Trashcity()
        t.valorar_turno(2, 30, 45)
        self.assertEqual(t.horas, 2)
        self.assertEqual(t.minutos, 30)
        self.assertEqual(t.segundos, 45)
        self.assertEqual(len(t.idempleados), 10)
        self.assertEqual(t.empleados, 6)

class TestCentroAcopio(unittest.TestCase):
    def test_reciclar(self):
        c = CentroAcopio()
        c.reciclar()
        self.assertTrue(1 <= c.vidrio <= 10)
        self.assertTrue(1 <= c.papel <= 10)
        self.assertTrue(1 <= c.plastico <= 10)
        self.assertTrue(1 <= c.metal <= 10)
        self.assertTrue(1 <= c.organicos <= 10)

if __name__ == '__main__':
    unittest.main()










    

          
      



        



