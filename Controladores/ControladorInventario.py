from Modelos.Inventario import Inventario
from Modelos.Proyecto import Proyecto
from Modelos.Material import Material
from Repositorios.RepositorioMaterial import RepositorioMaterial
from Repositorios.RepositorioProyecto import RepositorioProyecto
from Repositorios.RepositorioInventario import RepositorioInventario


class ControladorInventario():

    """
   constructor que permite llevar a cabo la creacion de instancias del controlador.
   """

    def __init__(self):
        self.repositorioInventario = RepositorioInventario()
        self.repositorioProyecto = RepositorioProyecto()
        self.repositorioMaterial = RepositorioMaterial()
        print("Creando Controlador Inventario")

    def index(self):
        print("Listar Los Inventario")
        return self.repositorioInventario.findAll()

    def create(self, laInventario, id_Material, id_Proyecto):
        print("Creando Inventario")
        nuevoInventario = Inventario(laInventario)
        laMaterial = Material(self.repositorioMaterial.findById(id_Material))
        laProyecto = Proyecto(self.repositorioProyecto.findById(id_Proyecto))
        nuevoInventario.Material = laMaterial
        nuevoInventario.Proyecto = laProyecto

        return self.repositorioInventario.save(nuevoInventario)

    def show(self, id):
        print("Mostrando Inventario Con id ", id)
        laInventario = Inventario(self.repositorioInventario.findById(id))
        return laInventario.__dict__

    def update(self, id, id_Material, id_Proyecto):
        print("Actualizando Inventario con id ", id)
        InventarioActual = Inventario(self.repositorioInventario.findById(id))
        laMaterial = Material(self.repositorioMaterial.findById(id_Material))
        laProyecto = Proyecto(self.repositorioProyecto.findById(id_Proyecto))
        InventarioActual.Material = laMaterial
        InventarioActual.Proyecto = laProyecto
        return self.repositorioInventario.save(InventarioActual)

    def delete(self, id):
        print("Elimiando Inventario con id ", id)
        return self.repositorioInventario.delete(id)
