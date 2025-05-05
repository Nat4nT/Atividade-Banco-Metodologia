from src.conta.conta import Conta
import pytest
from pathlib import Path
import csv

class TestConta:
    @staticmethod
    def carregar_arquivo() -> list:
        data = []
        arquivo = "contas.csv"
        #lendo o arquivo
        path = Path(__file__).parent / arquivo
        with open(path, 'r') as file:
            leitor = csv.DictReader(file)
            #setando os parametros do arquivo
            for row in leitor:
                data.append((
                    row['chave'],
                    float(row['valor']),
                    float(row['saldo']),
                    float(row['limite']),
                    row['bool'] 
                ))
        return data

    @pytest.fixture
    def test_criar_conta_limite_zero(self):
        #tentando criar conta com limite 0 
        return Conta(saldo=0, limite=0, pix="eliezer@silva.com")


    @pytest.mark.parametrize("chave,valor,saldo,limite,bool", carregar_arquivo())
    def test_transferencia(self, chave, valor, saldo, limite, bool):
        """Testa as transferências utilizando o arquivo CSV onde os parametros seguem aquele escopo"""
        #criando conta através da Classe
        conta = Conta(saldo=saldo, limite=limite)
        result = conta.transferir(chave, valor)
        assert result == int(bool)

    def test_criar_conta_com_divida(self):
        with pytest.raises(ValueError):
            Conta(saldo=-200, limite=50, pix="geradordeErro@gmail.com")

    def test_realizar_transferencia_para_mesmo_pix(self):
        eu = Conta(100,50,"eumesmo@gmail.com",'123')
        resultado = eu.transferir(eu.pix, 1200.00)
        assert resultado == 0

    def test_criar_conta_sem_limite_nao_pode_ter_saldo_negativo(self):
        conta_negativa = Conta(100,0,"caloteiro@gmail.com","0800")
        with pytest.raises(ValueError):
            conta_negativa.saldo = -1