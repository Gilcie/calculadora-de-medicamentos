# Calculator Methods

def drip(vol, time):
    if mode == 'Horas':
        macro = vol / (time * 3)
        micro = vol / time
    else:
        micro = vol / (time / 60)
        macro = vol / ((time / 60) * 3)
    print(f'\n Microgotejamento:'
          f'\n {round(micro, 2)} Microgotas por minuto '
          f'\n {"":-^30}'
          f'\n Macrogotejamento:'
          f'\n {round(macro, 2)} Macrogotas por Minuto'
          f'\n {"":-^30}\n')


def intravenous_medication(presc, vol, cpm):
    result = presc * vol / cpm
    print(f'\n {"":-^30}'
          f'\n Administre {result} ml de medicamento'
          f'\n{"":-^30}')


def medication_dilution(presc, conc, vol, solv):
    result_1 = conc * vol / solv
    result_2 = presc / result_1
    print(f'\n {"":-^30}'
          f'\n Cada ml contém {result_1} mg de medicamento\n'
          f'\n Aspire {result_2} ml de medicamento'
          f'\n{"":-^30}')


def pill_concentration(presc, conc):
    result = presc / conc
    print(f'\n'
          f'\n {"":><5} Administre {result} Comprimidos\n')


def conversion_drops_to_ml(drops):
    result = drops / 20
    print(f'\n'
          f'\n {"":><5} {drops} gotas = {result} ml\n')


def conversion_ml_to_drops(ml):
    result = ml * 20
    print(f'\n'
          f'\n {"":><5} {ml} ml = {result} Gotas\n')


def conversion_seconds_to_minutes(seconds):
    result = seconds / 60
    print(f'\n'
          f'\n {"":><5}{seconds}s = {result} Minutos\n')


def conversion_minutes_to_seconds(minutes):
    result = minutes * 60
    print(f'\n'
          f'\n {"":><5} {minutes}min = {result} Segundos\n')


def conversion_minutes_to_hours(minutes):
    result = minutes / 60
    print(f'\n'
          f'\n {"":><5} {minutes}min = {result} Horas\n')


def conversion_hours_to_minutes(hours):
    result = round(hours * 60)
    print(f'\n'
          f'\n {"":><5} {hours}h = {result} Minutos\n')


def conversion_mg_to_g(mg):
    result = mg / 1000
    print(f'\n'
          f'\n {"":><5} {mg}mg = {result} Gramas\n')


def conversion_g_to_mg(g):
    result = g * 1000
    print(f'\n'
          f'\n {"":><5} {g}g = {result} Miligramas\n')


def imprimir_menu_conversao():
    print(f'{" O que você deseja converter? ":=^40}'
          f'\n1 - Gotas para Mililitros(ml)'
          f'\n2 - Mililitros(ml) para Gotas'
          f'\n3 - Segundos para Minutos'
          f'\n4 - Minutos para Segundos'
          f'\n5 - Minutos para Horas'
          f'\n6 - Horas para Minutos'
          f'\n7 - Miligrama(mg) para Grama'
          f'\n8 - Grama para Miligrama(mg)'
          f'\n9 - Sair '
          f'\n{"":-^30}')


def imprimir_menu():
    print(f'{" Menu ":=^30}'
          f'\n1 - Gotejamento'
          f'\n2 - Medicação Endovenosa'
          f'\n3 - Diluição de Medicamentos'
          f'\n4 - Concentração de Comprimidos'
          f'\n5 - Conversão de Unidades'
          f'\n6 - '
          f'\n7 - '
          f'\n0 - '
          f'\n{"":-^30}')


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
    elif opcao == '4':
        presc = int(input('Prescrição Médica em Miligramas(mg): '))
        conc = int(input('Concentração Disponível em Miligramas(mg): '))
        pill_concentration(presc, conc)
    elif opcao == '5':
        while True:
            imprimir_menu_conversao()
            opcao = input('Opção Desejada: ')
            if opcao == '1':
                drops = int(input('Quantidade de Gotas: '))
                conversion_drops_to_ml(drops)
            elif opcao == '2':
                ml = int(input('Quantidade de Mililitros: '))
                conversion_ml_to_drops(ml)
            elif opcao == '3':
                seconds = int(input('Quantidade de Segundos: '))
                conversion_seconds_to_minutes(seconds)
            elif opcao == '4':
                minutes = int(input('Quantidade de Minutos: '))
                conversion_minutes_to_seconds(minutes)
            elif opcao == '5':
                minutes = int(input('Quantidade de Minutos: '))
                conversion_minutes_to_hours(minutes)
            elif opcao == '6':
                hours = int(input('Quantidade de Horas: '))
                conversion_hours_to_minutes(hours)
            elif opcao == '7':
                mg = int(input('Quantidade de Miligramas: '))
                conversion_mg_to_g(mg)
            elif opcao == '8':
                g = int(input('Quantidade de Gramas: '))
                conversion_g_to_mg(g)
            elif opcao == '9':
                break
