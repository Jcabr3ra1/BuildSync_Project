from Modelos.Proyecto import Proyecto
from Repositorios.RepositorioProyecto import RepositorioProyecto


class ControladorProyecto():
    """
   constructor que permite llevar a cabo la creacion de instancias del controlador.
   """

    def __init__(self):
        self.repositorioProyecto = RepositorioProyecto()
        print("Creando Controlador Proyecto")

    def index(self):
        print("Listar Los Proyectos")
        return self.repositorioProyecto.findAll()

    def create(self, laProyecto):
        print("Creando Proyecto")
        nuevoProyecto = Proyecto(laProyecto)
        return self.repositorioProyecto.save(nuevoProyecto)

    def show(self, id):
        print("Mostrando Proyecto Con id ", id)
        laProyecto = Proyecto(self.repositorioProyecto.findById(id))
        return laProyecto.__dict__

    def update(self, id, laProyecto):
        print("Actualizando Proyecto con id ", id)
        ProyectoActual = Proyecto(self.repositorioProyecto.findById(id))
        ProyectoActual.Nombre = laProyecto["Nombre"]
        ProyectoActual.Descripcion = laProyecto["Descripcion"]
        ProyectoActual.fechaInicio = laProyecto["fechaInicio"]
        ProyectoActual.fechaFin = laProyecto["fechaFin"]
        ProyectoActual.Estado = laProyecto["Estado"]
        return self.repositorioProyecto.save(ProyectoActual)

    def delete(self, id):
        print("Elimiando Proyecto con id ", id)
        return self.repositorioProyecto.delete(id)
