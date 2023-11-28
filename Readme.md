# Global Solution Python

# Integrantes:
- Luiz Otávio Leitão Silva - RM: 553542
- Pedro Donizete Fagundes - RM: 553391
- Maurício Viera Pereira - RM 553748

# Descrição do Projeto: Sistema de Agendamento de Consultas

- Este projeto implementa um sistema simples de agendamento de consultas médicas utilizando Python. O código é dividido em três principais partes: validação de dados pessoais, validação da data da consulta e validação do horário da consulta.

# Validação de Dados Pessoais:

- O usuário é solicitado a inserir seu nome completo, data de nascimento e telefone para contato.
- O sistema utiliza a função ValidaIdade para verificar se o paciente tem mais de 18 anos.
- Caso o usuário forneça dados incorretos, o sistema fornece mensagens de erro e pede para inserir as informações novamente.

# Validação da Data da Consulta:

- O sistema solicita que o usuário insira a data desejada para a consulta.
- A data é validada para garantir que seja pelo menos 2 dias após a data atual.
- Se a data inserida não atender aos critérios, o sistema exibirá uma mensagem de erro e pedirá para o usuário fornecer uma nova data.

# Validação do Horário da Consulta:

- O usuário é solicitado a inserir o horário desejado para a consulta, que deve estar entre 7:00 e 18:00.
- A entrada do usuário é validada, e mensagens de erro são exibidas se o horário estiver fora do intervalo permitido.
- Se a entrada for válida, a consulta é registrada, e uma mensagem de confirmação é exibida.

# Visualização e Remoção de Consultas Agendadas:

- O sistema permite visualizar todas as consultas agendadas, exibindo informações como nome do paciente, telefone, data e horário da consulta.
- Opções também são fornecidas para remover uma consulta específica, informando o índice da consulta a ser removida.

# Menu Principal:

- O sistema possui um menu principal com as opções: agendar consultas, visualizar consultas agendadas, cancelar agendamento e sair.
- O usuário pode escolher a opção desejada digitando o número correspondente.
- O programa continua executando em um loop até que o usuário escolha sair.

Este projeto proporciona uma abordagem interativa para agendamento de consultas, incorporando validações para garantir a integridade e consistência das informações inseridas pelos usuários.

