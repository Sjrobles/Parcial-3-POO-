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




op=input("Desea iniciar el dia? si o no ")

if op == "si":
  z = turno()
  y = puntogeografico()
  x = tiempo()
  t = Trashcity()
  t.iniciar_recoleccion(y.latitud,y.longitud,z.camiones,z.empleados)
  t.valorar_turno(x.horas,x.minutos,x.segundos)
  c = CentroAcopio()
  c.reciclar()

  op2 = input("Desea hacer otro turno? si o no ")
  while op2 == "si":
    print("--------------------------------------------------------")

    
    y = puntogeografico()
    t.iniciar_recoleccion(y.latitud,y.longitud,t.camiones,t.empleados)
    if t.switch == True:

       
     x = tiempo()

     t.valorar_turno(x.horas,x.minutos,x.segundos)

     c.reciclar()
     
    
      
    op2 = input("Desea hacer otro turno? si o no ")
  else:
    print("Se acabaron los turnos por hoy, ya sea por falta de camiones y/o empleados, o el gerente decidió cerrar")  
   


else:
 print("El dia de hoy no se recogió basura")  


#Se realizo el ejemplo con un numero de camiones y empleados delimitados por mi, la cantidad de turnos posibles dependera de si el usuario quiere parar#
# o si el numero de camiones o empleados es insuficiente#








    

          
      



        






        



