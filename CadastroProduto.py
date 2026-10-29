### Classe que representa o serviço de cadastro de listaProdutos
import locale

class CadastroProduto:

    def __init__(self, listaProdutos):
        self.listaProdutos = listaProdutos

    ### Verifica as regras de negócio do produto
    def validarDados(self, produto) -> bool:
        if produto["codigo"] == "":
            print("O código do produto não foi informado.")
            return False

        if produto["nome"] == "":
            print("O nome do produto não foi informado.")
            return False

        if produto["preco"] <= 0:
            print("O preço do produto não pode ser zero ou negativo.")
            return False

        if produto["quantidade"] < 0:
            print("A quantidade do produto não pode ser negativa.")
            return False

        for item in self.listaProdutos:
            if item["codigo"] == produto["codigo"]:
                print("Já existe um produto com esse código.")
                return False
            else:
                return True

        return True

    ### Solicita os dados do produto e retorna o produto
    def solicitarDados(self):
        print("Vamos cadastrar o produto:")

        print("\nInforme o código do produto:")
        codigo = str(input())

        print("\nInforme o nome do produto:")
        nome = str(input()).upper()

        print("\nInforme o preço do produto:")
        preco = float(input())

        print("\nInforme a quantidade do produto:")
        quantidade = int(input())

        return {"codigo": codigo, "nome": nome, "preco": preco, "quantidade": quantidade}

    ### Executa as ações para criar o produto
    def executarAcao(self) -> None:
        try:
            produto = self.solicitarDados()

            if self.validarDados(produto):
                self.listaProdutos.append(produto)

                print("O produto foi adicionado com sucesso")

        except ValueError:
            print("A quantidade informada do produto não é válida. Por favor verifique")

    ### Mostra os listaProdutos criados
    def exibirProdutosCadastrados(self) -> None:
        print("\nExibindo produtos cadastrados:")

        for produto in self.listaProdutos:
            print("\n---------------------------------------------------------")
            print(f"Nome: {produto["nome"]}\nCodigo: {produto["codigo"]}\nPreço: {locale.currency(produto["preco"])}\nQuantidade: {produto["quantidade"]}")
            print("---------------------------------------------------------")

        print("")