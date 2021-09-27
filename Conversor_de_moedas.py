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
   

    
            


