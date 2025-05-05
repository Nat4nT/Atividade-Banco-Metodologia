from rich import print 

class Conta:
    def __init__(self, saldo=0, limite=0, pix="", numero=""):
        self.limite = limite 
        self.saldo = saldo
        self.pix = pix
        self.numero = numero
        self.agencia = 0
        self.banco = None
        self.cliente = None
        
    @property
    def saldo(self) -> float:
        return self._saldo

    @saldo.setter
    def saldo(self, valor: float):
        if ((valor + self.limite) < 0):
            raise ValueError("Saldo inferior ao limite")
        self._saldo = valor


    def transferir(self, pix: str, valor: float) :
        if pix == self.pix:
            print("Não é possivel mandar pix para você mesmo")
            return 0 
        
        if ((self.saldo + self.limite) - valor >= 0):
            if (self.saldo < valor):
                self.limite = self.limite - (self.saldo - valor)
                self.saldo = 0
            else:
                self.saldo -= valor
            print(f"Pix de R$ {valor} enviado para {pix}")
            return 1 
        else:
            print(f"Saldo indisponível")
            return 0 
        
    def depositar(self, valor):
        """ adiciona valor no saldo """
        self.saldo += valor
        print(f"Deposito de [blue]R$ {valor}[/]")
    
    def consulta(self):
        """ 
        Consulta saldo em conta 
        """
        cl = "red" if self.saldo < 0 else "blue"
        print(f"Saldo atual R$ [{cl}]{self.saldo}[/]")
        print(f"limite atual R$ [{cl}]{self.limite}[/]")

    def extrato(self):
        """ 
        Gera extrato das operações financeiras 
        D   R$ 2000  21/03
        C   R$ 350   21/03
        """
        print("extrato")
        print(f"saldo: {self.saldo}")
        print(f"limite: {self.limite}")
        pass


if __name__ == "__main__":
    
    print("*"*30)
    conta = Conta(saldo=3000, limite=1000, numero="12200-2")
    conta.consulta()
    print("*"*30)

    conta.transferir(pix="45-984011110", valor=2000)
    conta.consulta()

    print("*"*30)

    conta.depositar(350)
    conta.consulta()
        
    print("*"*30)

    conta.transferir(pix="fulano@gmail.com", valor=4000)
    conta.consulta()

    print("*"*30)

    conta.transferir(pix="fulano@gmail.com", valor=1000)
    conta.consulta()

    print("*"*30)

    conta.depositar(3050)
    conta.consulta()

    print("-"*30)

    conta.transferir(pix="45-984011110", valor=1000)
    conta.consulta()

    print("-"*30)
    conta.extrato()

