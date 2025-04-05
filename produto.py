class Produto:
    def __init__(self,nome,preco,estoque,peso_kg):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.peso_kg = peso_kg
    def atualizar_preco(self,novo_preco):
        if novo_preco > 0:
            self.preco = novo_preco
    
    def aplicar_desconto(self,percentual):
        preco_descontado = self.preco*percentual/100
        preco_com_desconto = self.preco - preco_descontado
        self.preco =  preco_com_desconto
    
    def verificar_estoque_baixo(self):
        return self.estoque < 5
        
    def __str__(self):
        if self.preco > 1:
            return f"Produto: {self.nome} | Preco: {self.preco:.2f} Reais"
        elif self.preco < 1:
            return f"Produto: {self.nome} | Preco: {self.preco:.2f} centavos"

    def __eq__(self, other):
        return self.nome == other.nome and self.preco == other.preco