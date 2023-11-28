

while True:
    print("\n-----------------------------------")
    print("| Bem vindo ao sistema NotreDame! |")
    print("| 1- Agendar Consultas            |")
    print("| 2- Ver Consultas Agendadas      |")
    print("| 3- Cancelar Agendamento         |")
    print("| 4- Sair                         |")
    print("-----------------------------------")

    try:
        opcao = int(input("\nDigite a opção desejada: "))
    except ValueError:
        print("Opção Inválida! Digite Novamente")
        continue