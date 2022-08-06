"""
Criei uma classe Agenda que pode armazenar 5 pessoas e seja capaz de realizar as seguintes operações:

* void armazenaPessoa(String nome, int idade, float altura);                                                     (OK)
* void removePessoa(String nome);                                                                                (OK)
* int buscaPessoa(String nome); // informa em que posição da agenda está a pessoa                                (OK)
* void imprimeAgenda(); // imprime os dados de todas as pessoas da agenda                                        (OK)
* void imprimePessoa(int index); // imprime os dados da pessoa que está na posição "i" da agenda.                (OK)
"""


class Agenda:
    """o contador vai ser responsavel por numerar as posições de cada pessoa na agenda"""
    contador = 0
    agendas = []

    def __init__(self, nome, idade, altura):
        self.__id = Agenda.contador + 1
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
        self.__dic = {'id': self.__id, 'nome': nome, 'idade': self.__idade, 'altura': self.__altura}
        Agenda.agendas.append(self.__dic)
        Agenda.contador += 1

    def add_agenda(self):
        if len(Agenda.agendas) < 2:
            Agenda.agendas.append(self.__dic)

    def imprimi_agendas(self):
        for pessoa in Agenda.agendas:
            print(f'nome: {pessoa["nome"]}, idade: {pessoa["idade"]}, altura: {pessoa["altura"]}')

    def remove_pessoa(self, nome):
        for pessoa in Agenda.agendas:
            if nome == pessoa['nome']:
                Agenda.agendas.remove(pessoa)
                print(f'{nome} foi removido')

    def busca_pessoa(self, nome):
        for pessoa in Agenda.agendas:
            if nome == pessoa['nome']:
                posicao_pessoa = pessoa['id']
                print(f'{nome} esta na posição {posicao_pessoa}')

    def imprimi_pessoa(self, valor):
        for pessoa in Agenda.agendas:
            if pessoa['id'] == valor:
                print(f'nome: {pessoa["nome"]}, idade: {pessoa["idade"]}, altura: {pessoa["altura"]}')


a = Agenda.agendas
"""intanciando o objeto agendas que esta dentro da classe agenda """
n1 = Agenda('douglas', 20, 1.90)
n2 = Agenda('cesar', 20, 1.96)
n3 = Agenda('lucas', 25, 1.80)
n4 = Agenda('mario', 30, 1.95)
n5 = Agenda('celso', 40, 1.70)
# criando os usuarios, com nome seguindo de suas idades e altura

Agenda.imprimi_agendas(a)
Agenda.remove_pessoa(a, 'cesar')
Agenda.busca_pessoa(a, 'douglas')
Agenda.imprimi_pessoa(a, 4)
# testando todos os metodos que estao dentro da classe
