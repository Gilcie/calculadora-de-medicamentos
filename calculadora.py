# Calculator Methods

def drip(vol, time):
    if mode == 'Horas':
        macro = vol/(time*3)
        micro = vol/time
    else:
        micro = vol/(time/60)
        macro = vol/((time/60)*3)
    print(f'\n Microgotejamento:'
          f'\n {round(micro,2)} Microgotas por minuto '
          f'\n ------------------------------'
          f'\n Macrogotejamento:'
          f'\n {round(macro,2)} Macrogotas por Minuto'
          f'\n ------------------------------\n')


def intravenous_medication(presc, vol, cpm):
    result = presc*vol/cpm
    print(f'\n ----------------------------------'
          f'\n Administre {result} ml de medicamento'
          f'\n-----------------------------------')


def medication_dilution(presc, conc, vol, solv):
    result_1 = conc * vol / solv
    result_2 = presc / result_1
    print(f'\n ----------------------------------'
          f'\n Cada ml contém {result_1} mg de medicamento\n'
          f'\n Aspire {result_2} ml de medicamento'
          f'\n-----------------------------------')



def imprimir_menu():
    print(f'-----------------------------------------'
          f'\n1 - Gotejamento'
          f'\n2 - Medicação Endovenosa'
          f'\n3 - Diluição de Medicamentos'
          f'\n4 - Concentração de Comprimidos'
          f'\n5 - Excluir Contato'
          f'\n6 - Exportar Contatos para CSV'
          f'\n7 - Importar Contatos'
          f'\n0 - Fechar Agenda'
          f'\n-----------------------------------------')



# Menu da Calculadora
while True:
    imprimir_menu()
    opcao = input('Opção Desejada: ')
    if opcao == '1':
        vol = int(input('Volume do Medicamento em Mililitro(ml):'))
        mode = input('Desejar especificar o tempo de aplicação em Minutos ou Horas?:')
        x = mode.capitalize()
        if x == 'Horas':
            time = int(input('Tempo de Aplicação em Horas: '))
        else:
            time = int(input('Tempo de Aplicação em Minutos: '))
        drip(vol, time)
    elif opcao == '2':
        presc = int(input('Prescrição Médica em Miligramas(mg): '))
        vol = int(input('Volume Disponível em Mililitro(ml):'))
        cpm = int(input('Concentração Disponível por Miligramas(mg): '))
        intravenous_medication(presc, vol, cpm)
    elif opcao == '3':
        presc = int(input('Prescrição Médica em Miligramas(mg): '))
        conc = int(input('Concentração Disponível em Miligramas(mg): '))
        vol = int(input('Volume da Concentração em Mililitro(ml): '))
        solv = int(input('Volume do Solvente em Mililitro(ml): '))
        medication_dilution(presc, conc, vol, solv)



