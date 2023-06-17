from Modelos.Material import Material
from Repositorios.RepositorioMaterial import RepositorioMaterial


class ControladorMaterial():
    """
   constructor que permite llevar a cabo la creacion de instancias del controlador.
   """

    def __init__(self):
        self.repositorioMaterial = RepositorioMaterial()
        print("Creando Controlador Material")

    def index(self):
        print("Listar Los Materiales")
        return self.repositorioMaterial.findAll()

    def create(self, laMaterial):
        print("Creando Materiales")
        nuevoMaterial = Material(laMaterial)
        return self.repositorioMaterial.save(nuevoMaterial)

    def show(self, id):
        print("Mostrando Materiales Con id ", id)
        laMaterial = Material(self.repositorioMaterial.findById(id))
        return laMaterial.__dict__

    def update(self, id, laMaterial):
        print("Actualizando Materiales con id ", id)
        MaterialActual = Material(self.repositorioMaterial.findById(id))
        MaterialActual.Nombre = laMaterial["Nombre"]
        MaterialActual.Descripcion = laMaterial["Descripcion"]
        MaterialActual.Dimensiones = laMaterial["Dimensiones"]
        MaterialActual.Precio = laMaterial["Precio"]
        MaterialActual.Cantidad = laMaterial["Cantidad"]
        MaterialActual.CalcularMaterial = laMaterial["CalcularMaterial"]
        return self.repositorioMaterial.save(MaterialActual)

    def delete(self, id):
        print("Elimiando Material con id ", id)
        return self.repositorioMaterial.delete(id)
