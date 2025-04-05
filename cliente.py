class Cliente:
    def __init__(self,nome,email,pontos_fidelidade):
        self.nome = nome
        self.email = email
        self.pontos_fidelidade = pontos_fidelidade

    def adicionar_pontos(self,pontos):
        if pontos > 0:
            self.pontos_fidelidade = self.pontos_fidelidade + pontos
    def resgatar_pontos(self,pontos):
        if pontos > 0:
            self.pontos_fidelidade = self.pontos_fidelidade - pontos

    def verificar_vip(self):
        return self.pontos_fidelidade >= 1000
        
    def __str__(self):
        return f"Cliente: {self.nome} | Pontos: {self.pontos_fidelidade}"
    
    def __eq__(self,other):
        return self.email == other.email
    
    def __iadd__(self,pontos):
        self.pontos_fidelidade += pontos
        return self