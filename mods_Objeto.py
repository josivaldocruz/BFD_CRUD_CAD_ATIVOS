class BemPatrimonial:
    def __init__(self, id, nome, tipo, valor, data_aquisicao, localizacao, condicao):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.valor = valor
        self.data_aquisicao = data_aquisicao
        self.localizacao = localizacao
        self.condicao = condicao

    def exibir(self):
        return (
            f"ID: {self.id}\n"
            f"Nome: {self.nome}\n"
            f"Tipo: {self.tipo}\n"
            f"Valor: R$ {self.valor:.2f}\n"
            f"Data de Aquisição: {self.data_aquisicao}\n"
            f"Localização: {self.localizacao}\n"
            f"Condição: {self.condicao}\n"
        )