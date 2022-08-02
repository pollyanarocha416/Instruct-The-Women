
class Estacionamento:
    #CONSTRUO ENCIMA DISSO DAQUI
    def __init__(self):
        self.vagas_de_carro = None
        self.vagas_de_moto = None
        self.carro_para_vaga = None
        self.moto_para_vaga = None
        self.total_de_vagas_livres_carro = None
        self.total_de_vagas_livres_moto = None

    def estacionar_carro(self, carro):
        self.carro_para_vaga = carro
        self.total_de_vagas_livres_carro = 5
        print(f"estacionando carro, total de vagas livres: {self.total_de_vagas_livres_carro - self.carro_para_vaga}")
    def remover_carro(self, carro):
        self.carro_para_vaga = carro
        print(f"removendo carro")
    
    def estacionar_moto(self, moto):
        self.moto_para_vaga = moto
        self.total_de_vagas_livres_moto = 5
        print(
            f"estacionando moto, total de vagas livres: {self.total_de_vagas_livres_moto - self.moto_para_vaga}")
    def remover_moto(self, moto):
       self.moto_para_vaga = moto
       print(f"removendo moto")
    
    def estado_do_estacionamento(self):
        print(
            f"estado do estacionamento, vagas livres carros: {self.total_de_vagas_livres_carro - self.carro_para_vaga}")

class Vagas(Estacionamento):
    def __init__(self):
        self.id = None
        self.tipo = None
        self.livre = None
        self.placa = None
    def ocupar(self):
        self.id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.tipo = ["Para carro", "Para moto"]
        self.livre = False
        self.placa = ['car', 'mot']
    def desocupar(self):
        self.id = 'Nenhum'
        self.tipo = False
        self.livre = True
        self.placa = ['car', 'mot']

class Carro(Vagas):
    def __init__(self):
        self.placa = None
        self.estacionado = None
    def estacionar(self):
        self.id = 1
        self.placa = 1
        self.estacionado = True
    def sair_da_vaga(self):
        self.placa = False
        self.estacionado = False

class Moto(Vagas):
    def __init__(self):
        self.placa = None
        self.estacionado = None

    def estacionar(self):
        self.estacionado = True

    def sair_da_vaga(self):
        self.estacionado = False


estacionar = Estacionamento()
car = Carro()
car.estacionar()
estacionar.estacionar_carro(1)
car.ocupar()
print(
    f"estacionado: {car.estacionado}, Placa: {car.placa[0]}, id: {car.id[0]}, tipo: {car.tipo[0]}, vaga esta livre: {car.livre}\n")
estacionar.estado_do_estacionamento()

car2=Carro()
car2.estacionar()
estacionar.estacionar_carro(2)
car2.ocupar()
print(
    f"estacionado: {car2.estacionado}, Placa: {car2.placa[0]}, id: {car2.id[1]}, tipo: {car2.tipo[0]}, vaga esta livre: {car2.livre}\n")
estacionar.estado_do_estacionamento()

car3 = Carro()
car3.sair_da_vaga()
estacionar.remover_carro(1)
car3.desocupar()
print(
    f"estacionado: {car3.estacionado}, Placa: {car3.placa[0]}, id: {car3.id}, tipo: {car3.tipo}, vaga esta livre: {car3.livre}\n")



moto = Moto()
moto.estacionar()
estacionar.estacionar_moto(1)
moto.ocupar()
print(
    f"estacionado: {moto.estacionado}, Placa: {moto.placa[1]}, id: {moto.id[0]}, tipo: {moto.tipo[1]}, vaga esta livre: {moto.livre}\n")
