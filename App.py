### Classe que representa o app
from Menu import Menu

class App:
    def inicializar(self, listaProdutos):
        menu = Menu(listaProdutos)
        menu.exibirMenu()
