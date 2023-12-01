from datetime import datetime, timedelta
import re

consultas_agendadas = []

def ValidaIdade(data_nascimento):
    hoje = datetime.now().date()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade >= 18

def AgendaConsultas():
    nome_paciente = input("Digite seu nome completo: ")

    while True:
        try:
            nascimento_paciente = input("Digite sua data de nascimento (DD/MM/AAAA): ")
            nascimento_paciente = datetime.strptime(nascimento_paciente, "%d/%m/%Y").date()

            if ValidaIdade(nascimento_paciente):
                break
            else:
                print("É necessário ser maior de 18 anos para agendar uma consulta.")

        except ValueError:
            print("Formato de data inválido. Tente novamente.")

    while True:
        try:
            telefone_paciente = input("Digite seu telefone para contato (Digite somente números): ")
            if re.match(r'^\d{2}\d{9}$', telefone_paciente):
                break
            else:
                print("Formato de telefone inválido. Tente novamente.")
        except Exception as exeption:
            print(f"Erro: {exeption}")

    while True:
        try:
            data_consulta = input("Digite a data da consulta (DD/MM/AAAA): ")
            data_consulta = datetime.strptime(data_consulta, "%d/%m/%Y").date()

            data_limite = datetime.now().date() + timedelta(days=2)

            if data_consulta >= data_limite:
                break
            else:
                print("É necessário agendar consultas com pelo menos 2 dias após a data atual. Digite Novamente.")

        except ValueError:
            print("Formato de data inválido. Tente novamente.")

    while True:
        try:
            horario_consulta = input("Digite o horário desejado para a consulta entre 7:00 e 18:00 (HH:MM): ")
            horario_consulta = datetime.strptime(horario_consulta, "%H:%M").time()

            if 7 <= horario_consulta.hour <= 18:
                break
            else:
                print("Horário fora do intervalo permitido (7:00 - 18:00). Digite novamente.")

        except ValueError:
            print("Formato de data ou horário inválido. Tente novamente.")

    consulta = {
        'Nome do Paciente': nome_paciente,
        'Telefone': telefone_paciente,
        'Data Nascimento': nascimento_paciente,
        'Data da Consulta': data_consulta,
        'Horário da Consulta': horario_consulta
    }

    consultas_agendadas.append(consulta)
    print("\nConsulta agendada Com Sucesso!")

def VerConsultasAgendadas():
    print("\nConsultas Agendadas:")
    for i, consulta in enumerate(consultas_agendadas):
        print(f"\nÍndice: {i + 1}")
        print(f"Nome do Paciente: {consulta['Nome do Paciente']}")
        print(f"Telefone: {consulta['Telefone']}")
        print(f"Data da Consulta: {consulta['Data da Consulta']}")
        print(f"Horário da Consulta: {consulta['Horário da Consulta']}")
        print("------------------------")

def RemoverConsulta(indice):
    if 0 <= indice < len(consultas_agendadas):
        consultas_agendadas.pop(indice)
        print(f"\nConsulta removida com sucesso!")
    else:
        print("Índice inválido. Nenhuma consulta removida.")

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

    match opcao:
        case 1:
            AgendaConsultas()
        case 2:
            VerConsultasAgendadas()
        case 3:
            VerConsultasAgendadas()
            indice_remover = int(input("Digite o índice da consulta a ser removida: ")) - 1
            RemoverConsulta(indice_remover)
        case 4:
            print("Até logo!")
            break
        case _:
            print("Opção inválida. Digite novamente!")

