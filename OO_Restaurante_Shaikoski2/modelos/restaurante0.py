#QUESTÃO 2
'''class ContaBancaria:
    def __init__(self, titular, saldo, ativo=False):
        self.titular = titular
        self.saldo = saldo
        self.ativo = ativo

    def __str__(self):
        return f"Conta de {self.titular} Tem saldo de: R$ {self.saldo:.2f} - Ativo: {self.ativo}"

    def saudacao(self):
        if self.ativo:
            return f"Sua conta está ativa, {self.titular}!"
        else:
            return f"Sua conta está inativa, {self.titular}!"

conta = ContaBancaria("Shaikoski", 1000000.00)
print(conta)
print(conta.saudacao())
conta.ativo = True
print(conta)
print(conta.saudacao())

#QUESTÃO 3
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = "Shaikoski"
        self.saldo = saldo

    def __str__(self):
        return f"O titular é {self.titular} e o saldo da conta é de {self.saldo}."

conta1 = ContaBancaria("Shaikoski" "R$ 20.000,60")
conta2 = ContaBancaria("Shaikoski", "R$ 1.550,55")

print(conta1)
print(conta2)'''

#QUESTÃO 4
'''class ContaBancaria:
    def __init__(self, titular, saldo, ativo=False):
        self.titular = titular
        self.saldo = saldo
        self.ativo = ativo

    def __str__(self):
        return f"Conta de {self.titular} Tem saldo de: R$ {self.saldo:.2f} - Ativo: {self.ativo}"

    def saudacao(self):
        if self.ativo:
            return f"Sua conta está ativa, {self.titular}!"
        else:
            return f"Sua conta está inativa, {self.titular}!"

    @classmethod
    def ativar_conta(cls, titular, saldo):
        return cls(titular, saldo, ativo=True)

conta = ContaBancaria("Shaikoski", 1000000.00)
print(conta)
print(conta.saudacao())

conta_ativa = ContaBancaria.ativar_conta("Shaikoski", 1000000.00)
print(conta_ativa)
print(conta_ativa.saudacao())'''

#QUESRÃO 5
class ContaBancaria:
    def __init__(self, titular, saldo, ativo=False):
        self._titular = titular
        self._saldo = saldo
        self._ativo = ativo

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

    @ativo.setter
    def ativo(self, value):
        self._ativo = value

    def __str__(self):
        return f"Conta de {self.titular} Tem saldo de: R$ {self.saldo:.2f} - Ativo: {self.ativo}"

    def saudacao(self):
        if self.ativo:
            return f"Sua conta está ativa, {self.titular}!"
        else:
            return f"Sua conta está inativa, {self.titular}!"

    @classmethod
    def ativar_conta(cls, titular, saldo):
        return cls(titular, saldo, ativo=True)

conta = ContaBancaria("Shaikoski", 1000000.00)
print(conta)
print(conta.saudacao())

conta_ativa = ContaBancaria.ativar_conta("Shaikoski", 1000000.00)


    

