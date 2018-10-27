#Programa princial

#importacao de classes
from view import View
from control import Control
from model import Model
from arquivo import Arquivo

#Instanciar o Model
m = Model()

#Instanciar a View
v = View()

#Instanciar o arquivo
a = Arquivo()

#Instanciar a Control
c = Control(v, m, a)

#Guardando a control na model
m.set_control(c)

#Guardando a control na view
v.set_control(c)

#Exibir o menu
c.exibir_menu()

#print(m.carregar_arquivo())