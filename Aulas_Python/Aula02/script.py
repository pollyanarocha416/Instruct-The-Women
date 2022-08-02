#isadoraferrao@usp.br

#encapsulamento ocutar detalhes _protegido

#get e set: @property >pra obter o get set
#return self.__medida
#_protegido
#__privado
#encapculamento
class Pessoa:
    def __init__(self, nome, profissao, identidade):
        self._nome = nome
        self.profissao = profissao
        self.__identidade = identidade

    def __str__(self) -> str:
        return f'nome: {self._nome}, Proficao: {self.profissao}, identidade: {self.__identidade}'

pessoa1 = Pessoa('Ana', 'Programadora', '123434')
print(pessoa1)
#altera o publico e alterado
pessoa1.profissao = 'Medica'
print(pessoa1)
# no privado o valor nao se altera
pessoa1.__identidade = '0000000'
print(pessoa1)
#no protegido o valor muda so se for escrito correto
pessoa1._nome = 'marta'
print(pessoa1)
