from funcionarios import FuncionarioHorista, FuncionarioMensalista


def main():
    # 1. Testando o Horista (Paulo)
    # R$ 15.00 a hora trabalhando 160 horas resulta em R$ 2400.00 bruto.
    # Com os 7.5% de desconto do INSS, bate certinho nos R$ 2220.00 do print.
    f1 = FuncionarioHorista(nome="Paulo", valor_hora=15.0, horas_trab=160.0)
    f1.calcular_salario()
    f1.analisar_salario()

    # 2. Testando o Mensalista (Amanda)
    # R$ 9500.00 bruto. Com 7.5% de desconto do INSS, bate nos R$ 8787.50 do print.
    f2 = FuncionarioMensalista(nome="Amanda", salario_bruto=9500)
    f2.calcular_salario()
    f2.analisar_salario()


if __name__ == "__main__":
    main()
