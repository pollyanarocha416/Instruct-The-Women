class Pessoas_da_escola:
    def __init__(self):
        self.cpf = None
        self.nome = None
        self.endereco = None

class Aluno(Pessoas_da_escola):
    def __init__(self):
        self.nome = 'al'
        self.aulas = 12
        self.parcelas = 20
        self.matricula = 1

    def __str__(self) -> str:
        return f'Pessoa: {self.nome} aulas: {self.aulas}'

class Professor(Pessoas_da_escola):
    def __init__(self):
        self.nome = "poll"
        self.endereco = None
        self.cpf = None
        self.salario = 2000
        self.codigoAula = 5674877

aluno = Aluno()
print(
    f"\nO nome do aluno é {aluno.nome} \n\f \f \f \f \f\n")

prof = Professor()
print(
    f"o salario do prof {prof.nome} é de {prof.salario} e o seu codigo é {prof.codigoAula}")
