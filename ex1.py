class conta_bancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.__saldo = saldo_inicial
        self.titular = titular
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    
    def mostrar_saldo(self):
        return self.__saldo


conta = conta_bancaria(titular="Erik", saldo_inicial=100)
conta.depositar(100)

print(conta.mostrar_saldo())
print(conta.titular)