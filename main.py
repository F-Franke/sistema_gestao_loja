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
        preco_descontado = preco*percentual/100
        preco_com_desconto = preco - preco_descontado
        self.preco =  preco_com_desconto
    
    def verificar_estoque_baixo():
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
    def verificar_vip():
        if self.pontos_fidelidade >= 1000:
            return True
        else:
            return False
        
    def __str__(self):
        return f"Cliente: {self.nome} | Pontos: {self.pontos_fidelidade}"
    
    def __eq__(self,other):
        return self.email == other.email
    
    def __iadd__(self,pontos):
        if pontos > 0:
            self.pontos_fidelidade =+ pontos
    
    