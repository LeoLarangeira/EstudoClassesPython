def verificaTransferencia(valor, saldo, banco):
    t = False
    if banco == 'bradesco':
        taxa = valor + (valor * 0.01)
        if taxa > saldo:
            t = True
            return print('Impossivel realizar a operação, saldo insuficente!'), t
        else:
            saldo = saldo - taxa
            return print(f'Seu saldo atual é de {saldo}'), t


    elif banco == 'itau':
        pass
    else:
        t = True
        return print('Impossivel realizar a operação'),