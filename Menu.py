from CadastroProduto import CadastroProduto
from CalculadorDeEstoque import CalculadorDeEstoque

### Classe que representa o menu do app
class Menu:
    def __init__(self, listaProdutos):
        self.cadastroProduto = CadastroProduto(listaProdutos)
        self.calculaEstoque = CalculadorDeEstoque(listaProdutos)

    ### Por meio da opção selecionada, o comando é executado.
    def executarComando(self, opcao: str) -> bool:
        if opcao == "1":
            self.cadastroProduto.executarAcao()
        elif opcao == "2":
            self.cadastroProduto.exibirProdutosCadastrados()
            self.calculaEstoque.calcularEstoque()
        elif opcao == "3":
            return True
        else:
            print("Opção inválida")

        return False

    ### Exibe o menu de seleção
    def exibirMenu(self) -> None:
        while (True):
            print("Bem-vindo ao controle de estoque da WZSISTEMAS")

            print("\n---------------------------------------------------------")
            print("1 - Cadastrar produto")
            print("2 - Cálcular estoque")
            print("3 - Sair")
            print("---------------------------------------------------------")
            print("Selecione a opção desejada:")

            if self.executarComando(str(input())):
                break

            print("\nPressione qualquer tecla para continuar")
            input()
