def calculadora():
    while True:
        print("Selecione a operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        opcao = input("Digite o número para a operação correspondente: ")

        if opcao == '0':
            print("Saindo da calculadora. Até logo!")
            break
        elif opcao in ['1', '2', '3', '4']:
            try:
                primeiro_valor = float(input("Digite o primeiro valor: "))
                segundo_valor = float(input("Digite o segundo valor: "))
            except ValueError:
                print("Por favor, insira números válidos.")
                continue

            if opcao == '1':
                resultado = primeiro_valor + segundo_valor
                print(f"Resultado da soma: {resultado}")
            elif opcao == '2':
                resultado = primeiro_valor - segundo_valor
                print(f"Resultado da subtração: {resultado}")
            elif opcao == '3':
                resultado = primeiro_valor * segundo_valor
                print(f"Resultado da multiplicação: {resultado}")
            elif opcao == '4':
                if segundo_valor == 0:
                    print("Erro: Divisão por zero não é permitida.")
                else:
                    resultado = primeiro_valor / segundo_valor
                    print(f"Resultado da divisão: {resultado}")
        else:
            print("Essa opção não existe. Tente novamente.")

# Chama a função calculadora
calculadora()