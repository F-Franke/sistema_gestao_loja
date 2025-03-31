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

class Cliente:
    def __init__(self,nome,email,pontos_fidelidade):
        self.nome = nome
        self.email = email
        self.pontos_fidelidade = pontos_fidelidade

    def adicionar_pontos(self,pontos):
        if pontos > 0:
            self.pontos_fidelidade =+ pontos
    def resgatar_pontos(self,pontos):
        if pontos > 0:
            self.pontos_fidelidade =- pontos

    def verificar_vip(self,pontos_fidelidade):
        return self.pontos_fidelidade >= 1000
        
    def __str__(self):
        return f"Cliente: {self.nome} | Pontos: {self.pontos_fidelidade}"
    
    def __eq__(self,other):
        return self.email == other.email
    
    def __iadd__(self,pontos):
        if pontos > 0:
            self.pontos_fidelidade =+ pontos

class pedido:

    def __init__(self,cliente,produto,quantidade,status):
        self.cliente = Cliente
        self.produto = Produto
        self.quantidade = quantidade
        self.status = status
        
    def calcular_total(self):
        return self.produto.preco * self.pedido.peso_total
        
    def calcular_peso_total(self):
        peso_total = self.produto.peso_kg * self.quantidade
        return peso_total
    
    def atualizar_status(status_novo):

    
    