print("Olá! Seja Bem Vindo.")

quant: int
quant = int(input("Quantos funcionários serão digitados?"))

idade: [int] = [0 for x in range(quant)]
salario: [float] = [0 for x in range(quant)]
altura: [float] = [0 for x in range(quant)]
genero: [str] = [0 for x in range(quant)]
nome: [str] = [0 for x in range(quant)]
i: int
quest: str

quest = "S"

while quest == "S" or quest == "s":
    for i in range(0, quant):
        nome[i] = input("Digite o Nome do Funcionário: ")
        idade[i] = int(input("Digite a idade do Funcionário: "))
        salario[i] = float(input("Digite o salário do Funcionário: "))
        altura[i] = float(input("Digite a altura do Funcionário: "))
        genero[i] = input("Digite o Gênero do Funcionário: ")

    print()
    for i in range(0, quant):
        if genero == "masculino" or genero == "Masculino" or genero == "MASCULINO" or genero == "m" or genero == "M":
            print(f"O Funcionário {nome[i]}, gênero {genero[i]}, ganha R${salario[i]:.2f} e tem {idade[i]} anos.")
        else:
            print("A Funcionária {:s}, gênero {:s}, ganha R${:.2f} e tem {:d} anos.".format(nome[i], genero[i], salario[i], idade[i]))

    quest = input("Digitar novamente? S/N. ")