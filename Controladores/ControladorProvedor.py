from Modelos.Provedor import Provedor
from Repositorios.RepositorioProvedor import RepositorioProvedor


class ControladorProvedor():
    """
   constructor que permite llevar a cabo la creacion de instancias del controlador.
   """

    def __init__(self):
        self.repositorioProvedor = RepositorioProvedor()
        print("Creando Controlador Provedor")

    def index(self):
        print("Listar Los Provedores")
        return self.repositorioProvedor.findAll()

    def create(self, laProvedor):
        print("Creando Provedores")
        nuevoProvedor = Provedor(laProvedor)
        return self.repositorioProvedor.save(nuevoProvedor)

    def show(self, id):
        print("Mostrando Provedores Con id ", id)
        laProvedor = Provedor(self.repositorioProvedor.findById(id))
        return laProvedor.__dict__

    def update(self, id, laProvedor):
        print("Actualizando Provedores con id ", id)
        ProvedorActual = Provedor(self.repositorioProvedor.findById(id))
        ProvedorActual.Nombre = laProvedor["Nombre"]
        ProvedorActual.Direccion = laProvedor["Direccion"]
        ProvedorActual.Contacto = laProvedor["Contacto"]
        ProvedorActual.Telefono = laProvedor["Telefono"]
        return self.repositorioProvedor.save(ProvedorActual)

    def delete(self, id):
        print("Elimiando Provedor con id ", id)
        return self.repositorioProvedor.delete(id)
