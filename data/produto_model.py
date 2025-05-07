from dataclasses import dataclass

@dataclass
class Produto:
    id: int
    nome: str
    descricao: str
    preco: float
    quantidade: int

    def __str__(self):
        return f"Produto(id={self.id}, nome='{self.nome}', descricao='{self.descricao}', preco={self.preco}, quantidade={self.quantidade})"