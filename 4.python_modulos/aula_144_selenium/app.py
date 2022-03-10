from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
from datetime import datetime

class FirefoxAuto:
    def __init__(self):
        options = Options()
        options.add_argument('-profile')
        options.add_argument('/home/bruno.teixeira/.mozilla/firefox/kyn84xla.default-release')
        self.firefox = webdriver.Firefox(executable_path='geckodriver', options=options)
        
    def acessa(self, site):
        self.firefox.get(site)

    def sair(self):
        self.firefox.quit()

    def manda_mensagem(self, pessoa, mensagem):
        self.acessa('https://web.whatsapp.com/')
        sleep(3)
        try:
            acha_pessoa = self.firefox.find_element('xpath','//span[@title="{}"]'.format(pessoa))
            acha_pessoa.click()
            mensagem_input = self.firefox.find_element('xpath','//div[@title="Mensagem"]')
            mensagem_input.send_keys(mensagem)
        except Exception as e:
            print('Erro ao enviar mensagem:', e)
            pass
        
        sleep(3)
        self.sair()

if __name__ == '__main__':
    pessoa = 'Isabella Teixeira'
    data = datetime.now().strftime('%d/%m/%Y')
    mensagem = f'Essa mensagem foi enviada de forma automática no dia {data} para o meu contato {pessoa}.\n'+f'Olá, {pessoa}. ' \
    'Tudo bem com você?\n' + 'Dá pra eu ficar espamando coisa pra você agora.\n'

    firefox = FirefoxAuto()
    firefox.manda_mensagem(pessoa, mensagem)