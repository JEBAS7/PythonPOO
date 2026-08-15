from ex008 import ContaBancaria

def main():
    c1 = ContaBancaria(111, 'Maria', 5_000)
    c1.depositar(-500)
    c1.sacar(-100)
    c1.saldo = 0
    print(c1)

if __name__ == '__main__':
    main()

