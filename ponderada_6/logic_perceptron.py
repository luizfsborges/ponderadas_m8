import numpy as np

class Perceptron:
    def __init__(self, taxa_aprendizado=0.1, n_iteracoes=100, limiar=0.5):
        self.taxa_aprendizado = taxa_aprendizado
        self.n_iteracoes = n_iteracoes
        self.limiar = limiar
        self.pesos = np.zeros(2)
        self.vies = 0

    def funcao_ativacao(self, x):
        return 1 if x >= self.limiar else 0

    def prever(self, entradas):
        saida_linear = np.dot(entradas, self.pesos) + self.vies
        y_predito = self.funcao_ativacao(saida_linear)
        return y_predito

    def treinar(self, X, y):
        for _ in range(self.n_iteracoes):
            for x, y_true in zip(X, y):
                y_pred = self.prever(x)
                erro = y_true - y_pred
                self.pesos += erro * self.taxa_aprendizado * x
                self.vies += erro * self.taxa_aprendizado

# Dados para a porta AND
X_and = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_and = np.array([0, 0, 0, 1])

# Dados para a porta OR
X_or = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_or = np.array([0, 1, 1, 1])

# Dados para a porta NAND
X_nand = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_nand = np.array([1, 1, 1, 0])

# Dados para a porta XOR
X_xor = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_xor = np.array([0, 1, 1, 0])

# Treinando os Perceptrons
perceptron_and = Perceptron()
perceptron_and.treinar(X_and, y_and)

perceptron_or = Perceptron()
perceptron_or.treinar(X_or, y_or)

perceptron_nand = Perceptron()
perceptron_nand.treinar(X_nand, y_nand)

perceptron_xor = Perceptron()
perceptron_xor.treinar(X_xor, y_xor)

# Função de teste oara o perceptron de portas lógicas
def testar_perceptron(perceptron, X, y, porta_logica):
    print(f"\n################## Porta {porta_logica} ##################\n")
    for x, y_true in zip(X, y):
        y_pred = perceptron.prever(x)
        print(f"Entrada: {x}, Predição: {y_pred}, Saída Esperada: {y_true}")

# Casos de teste para o Perceptron
testar_perceptron(perceptron_and, X_and, y_and, "AND")
testar_perceptron(perceptron_or, X_or, y_or, "OR")
testar_perceptron(perceptron_nand, X_nand, y_nand, "NAND")
testar_perceptron(perceptron_xor, X_xor, y_xor, "XOR")