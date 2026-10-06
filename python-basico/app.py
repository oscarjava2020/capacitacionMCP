import json
import camelcase
from pathlib import Path
 
from models.Car import Car
from models.Boat import Boat
from models.Plane import Plane
 
 
class app:
    c = camelcase.CamelCase()
    def __init__(self):
        self.clases_vehiculo = {"CAR": Car, "BOAT": Boat, "PLANE": Plane}
 
    def cargar_datos(self):
        ruta_datos = Path(__file__).with_name("datos_vehiculo.json")
        with ruta_datos.open(encoding="utf-8") as archivo:
            return json.load(archivo)
 
    def ejecutar(self):
        for item in self.cargar_datos():
            clase_vehiculo = self.clases_vehiculo[item["class"]]
            vehiculo = clase_vehiculo(**item["datos"])
            movimiento = vehiculo.move()
            print c.hump(
                f"{vehiculo.brand} {vehiculo.model} ({vehiculo.age})"
                f"\nEstado: {movimiento}\n"
            )
 
 
if __name__ == "__main__":
    app().ejecutar()
 
 
 