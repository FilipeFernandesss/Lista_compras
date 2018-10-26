#Classe de modelo
class Model:
    #Método construtor
    def __init__(self):
        self.lista_compras = {'Omo': 1, 'Arroz': 2, 'Bombril': 10}

    #Método que recupera a lista
    def get_lista_compras(self):
        return self.lista_compras

    #Método para add item
    def add_item(self, item, qtd):
        for itens in self.get_lista_compras().keys():
            if itens in item:
                print("O item já pertencia a lista.\n Deseja atualizar a quantidade?")
                self.atualizar_quantidade(item, qtd)
            else:
                self.lista_compras[item] = qtd
                break


    #Método para excluir item
    def exluir(self, item):
        for chave in self.get_lista_compras().keys():
            if chave == item:
                del self.get_lista_compras()[chave]
                break


    #Método para atualizar a quantidade
    def atualizar_quantidade(self, item, qtd):
        print(self.get_lista_compras()[item])