from cliente import Cliente
from produto import Produto

class pedido:

    def __init__(self,cliente,produto,quantidade,status):
        self.cliente = Cliente
        self.produto = Produto
        self.quantidade = quantidade
        self.status = "pendente"
        
    def calcular_total(self):
        return self.produto.preco * self.pedido.peso_total
        
    def calcular_peso_total(self):
        peso_total = self.produto.peso_kg * self.quantidade
        return peso_total
    
    def atualizar_status(self, status_novo):
        if self.status == "pendente" and status_novo in ["processando", "entregue"]:
            self.status = status_novo
        elif self.status == "processando" and status_novo in ["entregue"]:
            self.status = status_novo
        elif self.status == "entregue":
            print("Erro nao e possivel mudar o status atualmente")
    def cancelar(self):
        if self.status == "pendente":
            del self.Pedido
        else:
            print(f"pedido esta em {self.status} entao espere chegar para retornar ele.")