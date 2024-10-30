print('-----MENU PRINCIPAL-----\n')
print('(1) Gerenciar estudantes.')
print('(2) Gerenciar professores.')
print('(3) Gerenciar disciplinas.')
print('(4) Gerenciar turmas.')
print('(5) Gerenciar matriculas.')
print('(9) Sair.\n')
op = int(input('Informe a opção desejada: '))

if op == 1:
    print("\n\n***** [ESTUDANTES] MENU DE OPERAÇÕES *****\n")
elif op == 2:
    print("\n\n***** [PROFESSORES] MENU DE OPERAÇÕES *****\n")
elif op == 3:
    print("\n\n***** [DICIPLINAS] MENU DE OPERAÇÕES *****\n")
elif op == 4:
    print("\n\n***** [TURMAS] MENU DE OPERAÇÕES *****\n")
elif op == 5:
    print("\n\n***** [MATRICULAS] MENU DE OPERAÇÕES *****\n")
elif op == 9:
   pass
else:
    print("\n\nOpção incorreta!")

print('(1) incluir.')
print('(1) Listar.')
print('(1) Atualizar.')
print('(1) Excluir.')
print('(1) Voltar ao menos principal.\n')
acao = int(input('Informe a ação desejada: '))

if acao == 1:
    print("\n\n===== INCLUSÃO =====\n")
elif acao == 2:
    print("\n\n===== LISTAGEM =====\n")
elif acao == 4:
    print("\n\n===== EXCLUSÃO =====\n")
elif acao == 9:
    pass
else:

    print(acao)