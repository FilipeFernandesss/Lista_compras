#Classe para carregar um arquivo

class Arquivo:

    #Método para ler arquivo
    def ler_arquivo(self):

        dict = {}
        arquivo = open('controle_lista.txt', 'r')
        for linha in arquivo:

            lista = linha.split()
            dict[lista[0]] = int(lista[2])

        arquivo.close()
        return dict

    #Método para gravar os itens no dicionario
    def gravar_arquivo(self, dicionario):
        arquivo = open('controle_lista.txt', 'a')

        for linha in dicionario:
            #print(linha + ' ' + str(dicionario[linha]))
            arquivo.write(linha + ' : ')
            arquivo.write(str(dicionario[linha]) + '\n')

        arquivo.close()

'''teste = Arquivo()
print(teste.ler_arquivo('controle_list.txt'))

dic = {'Omo': 1, 'Cereal': 2, 'Bombril': '10'}
teste.gravar_arquivo(dic)'''

