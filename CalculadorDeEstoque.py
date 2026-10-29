
### Classe que representa o cálculo de listaProdutos em estoque
class CalculadorDeEstoque:

    def __init__(self, listaProdutos):
        self.listaProdutos = listaProdutos

    ### Realiza o cálculo dos listaProdutos.
    def calcularEstoque(self) -> None:
        print("Vamos cálcular a quantidade total do estoque:")

        quantidade: int = 0

        for produto in self.listaProdutos:
            quantidade += produto['quantidade']

        print(f"\nQuantidade de produtos no estoque: {quantidade}")
