# A palavra "class" é usada para criar uma classe.
# Uma classe funciona como um molde para criar objetos
class Carro:

    # Método Construtor
    def __init__(self, marca, modelo, ano, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

    # Métodos
    # Método acelerar
    # O aumento sera o valor recebido para aumentar a velocidade
    def acelerar(self, aumento):
        # self.velocidade = self.velocidade + aumento 
        self.velocidade += aumento

        print(f"O carro acelerou para {self.velocidade} km/h")

    #metodo freiar
    def freiar(self, redução):
        # self.velocidade = self.velocidade + aumento 
        self.velocidade -= redução

        print(f"O carro freou para {self.velocidade} km/h")

    def exibir_info(self):
        print("=== INFORMAÇÕES DO CARRO")

        # Método para exibir informações
        print(f"Marca: {self.Marca}")
        print(f"Marca: {self.Modelo}")
        print(f"Marca: {self.Ano}")
        print(f"Marca: {self.velocidade}")
        



# Criando um objeto da Classe Carro

# "carro1" é uma variável que recebe um objeto
carro1 = Carro("Chevrolet", "S10", 2013)

# Exibir informações do carro 1
print(f"Marca: {carro1.marca}")
print(f"Modelo: {carro1.modelo}")
print(f"Ano: {carro1.ano}")

# o valor 50 será parametro para "aumento"
carro1.acelerar(50)
# o valor 20 será parametro para redução
carro1.freiar(20)

carro1.exibir_info()

# # "carro2" é uma variável que recebe um objeto
carro2 = Carro("BYD", "Dolphin Mini", 2025)

# # Exibir informações do carro 2
print(f"Marca: {carro2.marca}")
print(f"Modelo: {carro2.modelo}")
print(f"Ano: {carro2.ano}")

carro2.acelerar(480)

carro2.freiar(2000)

carro1.exibir_info()
