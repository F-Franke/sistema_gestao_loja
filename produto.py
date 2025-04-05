class Produto:
    def __init__(self,nome,preco,estoque,peso_kg):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.peso_kg = peso_kg
    def atualizar_preco(self,novo_preco):
        if novo_preco > 0:
            self.preco = novo_preco
    
    def aplicar_desconto(self,percentual,preco):
        preco_descontado = self.preco*percentual/100
        preco_com_desconto = self.preco - preco_descontado
        self.preco =  preco_com_desconto
    
    def verificar_estoque_baixo(self,estoque):
        if self.estoque < 5:
            return True
        else:
            return False
        
    def __str__(self):
        return f"Produto: {self.nome} | Preco: {self.preco}"
    def __eq__(self, other):
        return self.nome == other.nome and self.preco == other.preco