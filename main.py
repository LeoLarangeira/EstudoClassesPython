from time import sleep


class BankAccount():
    def __int__(self,titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f'Titular: [{self.titular}] --> Saldo:[{self.saldo}]'

    def Transferencia(self):
        return self.saldo


class Itau(BankAccount):
    def Transferencia(self, x):
        taxa = x + (x * 0.01)
        t = False
        if taxa > self.saldo:
            t = True
            print(f'Impossivel realizar a operação')
            return t
        else:
            self.saldo = self.saldo - taxa
            print(f'Transação realizada com sucesso, seu saldo é de {self.saldo}')
            return t

    def Recebimento(self, x):
        self.saldo = self.saldo + x
        return f'Seu saldo atual é de {self.saldo}'


class Bradesco(BankAccount):
    def Transferencia(self, x):
        t = False
        taxa = 5 + (x * 0.5)

        self.saldo = self.saldo - taxa
        if taxa > self.saldo:
            t = True
            print(f'O valor da transferencia é {taxa}, com taxas seu saldo foi para {self.saldo}')
            return t
        else:
            print(f'Transação realizada com sucesso, seu saldo atual é de {self.saldo}')
            return t

    def Recebimento(self, x):

        self.saldo = self.saldo


# c1 -> quem envia
# c2 -> quem recebe
while True:
    nome = str(input("Informe o nome do titular: "))
    saldo = float(input("Saldo do titular: "))
    banco = str(input("Banco: "))
    # se o banco for itau ele realiza o procedimento de transeferencia
    if banco == "itau":
        c1 = Itau(nome, saldo)
        x = str(input("Deseja realizar uma transferencia? "))

        if x == "sim":
            # verifica se o banco é  bradescou ou se é o mesmo
            sleep(2)
            print('    Menu de transação    ')
            print('Informaçõs para quem vai transferir ')
            nome = str(input("Informe o nome do titular: "))
            saldo = float(input("Saldo do titular: "))
            banco = str(input("Banco: "))

            if nome == c1.titular and saldo == c1.saldo and banco == 'itau':
                print('Impossivel realizar uma transferencia para a sua própria conta')
                break
            elif banco == "bradesco":
                c2 = Bradesco(nome, saldo)
                valor = float(input('Valor que deseja transferir: '))

                # se a vericação de c1 em transferencias não for verdadeira ele pausa
                sleep(2)
                t = c1.Transferencia(valor)
                if t == True:
                    break
                else:
                    c2.Recebimento(valor)
                    print('A transação foi recebida com sucesso')
                    break




            elif banco == 'itau':
                c2 = Itau(nome, saldo)
                valor = float(input('Valor que deseja transferir: '))
                t = c1.Transerferencia(valor)
                if t == True:
                    break
                else:
                    c2.Recebimento(valor)
                    print('Valor recebido com sucesso! ')
                    break
            else:
                print('Opção invalida')
        else:
            break



    elif banco == "bradesco":
        c1 = Bradesco(nome, saldo)
        x = input('Deseja realizar uma operação de transferencia ? SIM | Não ')
        if x == "sim":
            # verifica se o banco é  bradescou ou se é o mesmo
            sleep(2)
            print('    Menu de transação    ')
            print('Informaçõs para quem vai transferir ')
            nome = str(input("Informe o nome do titular: "))
            saldo = float(input("Saldo do titular: "))
            banco = str(input("Banco: "))

            if c1.titular == nome and c1.saldo == saldo and banco == 'bradesco':
                print('impossivel realizar operações para a mesma conta ')
                break
            elif banco == 'bradesco':
                c2 = Bradesco(nome, saldo)
                valor = float(input('Valor que deseja transferir: '))

                # se a vericação de c1 em transferencias não for verdadeira ele pausa
                sleep(2)
                t = c1.Transferencia(valor)
                if t == True:
                    break
                else:
                    c2.Recebimento(valor)
                    print('Valor recebido com sucesso! ')
                    break



            elif banco == 'itau':
                c2 = Itau(nome, saldo)
                valor = float(input('Valor que deseja transferir: '))
                sleep(2)
                t = c1.Transerferencia(valor)
                if t == True:
                    break
                else:
                    c2.Recebimento(valor)
                    print('Valor recebido com sucesso! ')
                    break
            else:
                print('Informação inválida: ')
                break
    else:
        print('Informação invalida: ')
        break
try:
    print('Informações adicionais no modo desenvolvedor: ')
    print(c1)
    sleep(2)
    print('')
    print(c2)
except Exception as e:
    print('Error', e)