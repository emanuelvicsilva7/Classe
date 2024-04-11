class ContaBancaria:
    def __init__ (self,nconta,saldo,titular):
        self.nconta = nconta
        self.saldo = saldo
        self.titular = titular


    def depositar(self):
        deposito = int(input('Quanto dinheiro você deseja depositar?: R$'))
        self.saldo += deposito
        return f'O deposito inserido foi de R${deposito}.'
    
    def sacar(self):
        saque = int(input('Quanto você quer sacar?: R$'))
        self.saldo -= saque
        return f'O dinheiro que será sacado é de R$ {saque}.'
    
    def atual(self):
        return f'O valor atual do titular {self.titular} é R${self.saldo}.'
    
if __name__ == '__main__':
    cliente1 = ContaBancaria('1',1800,'Emanuel')
    cliente1.depositar()
    print(cliente1.atual())
    cliente1.sacar()
    print(cliente1.atual())


    
