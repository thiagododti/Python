# Variáveis de classe e instância

class Estudante:
    escola = "Projeção"  # Variável de classe

    def __init__(self, nome, numero):
        self._nome = nome   # Variável de instância
        self._numero = numero  # Variável de instância

    def __str__(self):
        return f"{self._nome} ({self._numero}) - {self.escola}"


# Variável de classe é definida logo apos a criação da classe
# A mesma fica disponível para qualquer instancia da classe

# Variável de Instancia só tem acesso as variáveis da própria instancia
