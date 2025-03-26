salario = float(input("Digite o salário por hora: "))
horas = float(input("Digite as horas trabalhadas no mês: "))

bruto = salario*horas
ir = bruto * (11/100)
inss = bruto * (8/100)
sindicato = bruto * (5/100)
liquido = bruto - ir -inss- sindicato

print(f'''Salário bruto {bruto:.2f},
      IR (11%) {ir:.2f}
      INSS (8%) {inss:.2f}
      sindicato (5%) {sindicato:.2f}
      Salário Líquido {liquido:.2f}''')