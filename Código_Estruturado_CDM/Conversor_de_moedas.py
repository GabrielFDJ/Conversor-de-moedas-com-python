from forex_python.converter import CurrencyCodes, CurrencyRates
c = CurrencyRates()
cd = CurrencyCodes()

def formatacao_titulo(txt):
    print("-"*len(txt))
    print('\033[1;33;40m'+txt+'\033[m')
    print("-"*len(txt))

def print_moeda():    
    print('\033[1;36;40m'+'\n1-BRL\n2-USD\n3-OUTRO:'+'\033[m')

def mensagem_de_erro():
    print('\033[1;33;41m'+'Ops! Entrada Inválida ... tente novamente com um valor válido'+'\033[m')    
 
#inicio
while True:
    formatacao_titulo(' BEM VINDO AO CONVERSOR DE MOEDA')
    formatacao_titulo('- INSIRA O VALOR A SER CAMBIADO\n- INSIRA A MOEDA INICIAL\n- INSIRA A MOEDA DE CAMBIO')
    formatacao_titulo('VALOR INICIAL')

    while True:
        try:
            valor_inicial = float(input("Insira  o valor a ser cambiado: \n"))
            break
        except ValueError:
            mensagem_de_erro()

    formatacao_titulo('SELECIONE A MOEDA INICIAL')
    cod_moeda_inicial = None
    while cod_moeda_inicial not in (1,2,3):
        print_moeda()
        try:
            cod_moeda_inicial = int(input("Selecione uma das 3 opções : \n"))
            if cod_moeda_inicial == 1:
                cod_moeda_inicial = 'BRL'
                print("Cod de escolha:",cod_moeda_inicial)
                break
            elif cod_moeda_inicial == 2:
                cod_moeda_inicial = 'USD'
                print("Cod de escolha:",cod_moeda_inicial)
                break
            elif cod_moeda_inicial == 3:
                cod_moeda_inicial = input('\nOutro, codigo de moeda escolhida:').upper()
                print("Cod de escolha :",cod_moeda_inicial)
                break
            else:
                mensagem_de_erro()
        except:
            mensagem_de_erro()

    formatacao_titulo('SELECIONE A MOEDA DE CAMBIO')
    cod_moeda_cambio = None
    while cod_moeda_cambio not in (1,2,3):
        print_moeda()
        try:
            cod_moeda_cambio = int(input("Selecione uma das 3 opções : \n"))
            if cod_moeda_cambio == 1:
                cod_moeda_cambio = 'BRL'
                print("Cod de escolha:",cod_moeda_cambio)
                break
            elif cod_moeda_cambio == 2:
                cod_moeda_cambio = 'USD'
                print("Cod de escolha:",cod_moeda_cambio)
                break
            elif cod_moeda_cambio == 3:
                cod_moeda_cambio = input('\nOutro, codigo de moeda escolhida:').upper()
                print("Cod de escolha :",cod_moeda_cambio)
                break
            else:
                mensagem_de_erro()                
        except:
            mensagem_de_erro()  
      
    formatacao_titulo('RESULTADO DA CONVERSÃO...')
    result = c.convert(cod_moeda_inicial, cod_moeda_cambio, valor_inicial)
    simbolo_moeda = cd.get_symbol(cod_moeda_inicial)
    simbolo_moeda_cambio = cd.get_symbol(cod_moeda_cambio)
    result = round(result,2)
    print(f'{cod_moeda_inicial} - {simbolo_moeda} - {valor_inicial} = {cod_moeda_cambio} - {simbolo_moeda_cambio} - {result}')    

    formatacao_titulo('SE DESEJA SAIR DIGITE 0 , PARA CONTINUAR QUALQUER OUTRO VALOR : ')
    opcao = int(input())    
    if(opcao == 0):
        formatacao_titulo("PROGRAMA ENCERRADO")       
        break


