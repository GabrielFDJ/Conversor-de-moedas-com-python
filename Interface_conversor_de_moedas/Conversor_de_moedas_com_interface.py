import PySimpleGUI as sg 
from currency_converter import ECB_URL, SINGLE_DAY_ECB_URL
from currency_converter import CurrencyConverter
from os import system
import requests
import json

c = CurrencyConverter(ECB_URL)  # Carrega o histórico completo atualizado
c = CurrencyConverter(SINGLE_DAY_ECB_URL)  # Carrega as taxas mais recentes
system('cls')
first_date, last_date = c.bounds['USD']  # Carrega a primeira e ultima data
# Muda o formato da última data de cotação
Data_Conversao = last_date.strftime('%d/%m/%Y')
moedas = c.currencies

# Lista de Moedas
list_moedas_inicial = ['USD','USDT', 'BRL', 'CAD', 'GBP', 'ARS', 'BTC', 'LTC', 'SGD',
               'EUR', 'JPY', 'CHF', 'AUD', 'CNY', 'ILS', 'ETH', 'XRP', 'DOGE']

list_moedas_cambio = ['USD', 'BRL','CAD', 'GBP', 'BTC', 'LTC', 'ZAR', 'ISK', 'CZK',
                'SEK', 'MXN', 'HUF', 'INR', 'MYR', 'DKK', 'TRY', 'BGN', 'IDR',
                'RUB', 'RON', 'HKD', 'THB', 'PLN', 'SGD', 'KRW', 'NOK', 'PHP',
                'EUR', 'JPY', 'CHF', 'AUD', 'CNY', 'ILS', 'NZD']

sg.theme('DarkBlack1')
class TelaPython:
    def __init__(self) -> None:
        # Layout
        layout = [
            [sg.Text('Valor:', size=(5, 1)),
             sg.Input(key='valor', size=(11, 1))],
            [sg.Text('Selecione a Moeda desejada.')],
            [sg.Text('Da_Moeda:', size=(10, 1)), sg.Combo(sorted(list_moedas_inicial), size=(8, 1), default_value='EUR', key='moeda_inicial'),
             sg.Text('Para_Moeda:', size=(11, 1)), sg.Combo(sorted(list_moedas_cambio), size=(8, 1), default_value='BRL', key='moeda_cambio')],
            [sg.Output(size=(50, 10), key='_output_')],
            [sg.Button('Limpar', button_color=('white', 'green')), sg.Button(
                'Converter', button_color=('white', 'blue')), sg.Button('Sair')]
        ]
        # Janela
        self.window = sg.Window('CONVERSOR DE MOEDAS', layout,font=11)      
        

    def limpar(self):
        self.window['valor'].update('')
        self.window['valor'].SetFocus()
        return

    def conversao_moeda(self, valor, moeda_inicial, moeda_cambio):
        moeda_inicial = moeda_inicial.upper()
        moeda_cambio = moeda_cambio.upper()     
        try:          
            conversao = c.convert(valor, moeda_inicial, moeda_cambio)
            print(f'Data da Cotação: {Data_Conversao}')
            print(f' {valor:,.2f} {moeda_inicial} = {conversao:,.2f} {moeda_cambio}')
        except ValueError:
            requisicao = requests.get(
                'https://economia.awesomeapi.com.br/json/all')
            cotacao = requisicao.json()
            try:               
                moeda_inicial = (cotacao[moeda_inicial]['code'])
                moeda_cambio = cotacao[moeda_inicial]['codein']
                v1 = float(cotacao[moeda_inicial]['bid'])                                             
                vt = valor*v1                
                print(f'Data da Cotação:  {Data_Conversao}')
                print(f'{valor:,.2f} {moeda_inicial} = {vt:,.2f} {moeda_cambio}')    
            except ValueError:
                print('Você deve selecionar as moedas para conversão!')
            except KeyError:
                print('Não encontrou!') 
    
    def Iniciar(self):         
        while True:
            # Extrair os dados da tela
            evento, valores = self.window.read()
            v = self.window['valor'].get()
            moeda_inicial = self.window['moeda_inicial'].get()
            moeda_cambio = self.window['moeda_cambio'].get()
            if evento == sg.WINDOW_CLOSED:
                break
            elif evento == 'Sair':
                sg.popup_no_titlebar(
                    'Volte sempre!', font='18', text_color='yellow')
                self.window.close()
            elif evento == 'Converter':
                try:
                    valor = float(v.replace(',', '.'))
                    if type(valor) == float:
                        self.conversao_moeda(valor, moeda_inicial, moeda_cambio)
                except ValueError:
                    print('Favor digitar um valor válido, "NÚMERO".')
            elif evento == 'Limpar':
                self.limpar()
                self.window['_output_'].update('')       
        

tela = TelaPython()
tela.Iniciar()



