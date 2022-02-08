import re

from django.forms import RegexField

class ipv4:
    def __init__(self, ip, mascara=None, prefixo=None):
        self.ip = ip
        self.mascara = mascara
        self.prefixo = prefixo

        if not prefixo and not mascara:
            raise ValueError('Você deve passar o valor do prefixo ou o valor da máscara!')

        if prefixo and mascara:
            raise ValueError('Você não pode passar ambos os valores de prefixo e máscara!')

        self._set_broadcast()
        self._set_rede()

        print(f'IP: {self.ip}')
        print(f'Máscara: {self.mascara}')
        print(f'Rede: {self._rede}')
        print(f'Broadcast: {self._broadcast}')
        print(f'Prefixo: {self.prefixo}')
        print(f'Número de IPs: {self._numero_ips()}')

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, valor):

        if not self._valida_reg(valor):
            raise ValueError('Ip inválido.')
        self._ip = valor
        self._ip_bin = self._ip_to_bin(valor)

    @property
    def mascara(self):
        return self._mascara

    @mascara.setter
    def mascara(self, valor):

        if not valor:
            return
        
        if not self._valida_reg(valor):
            raise ValueError('Máscara inválida.')

        self._mascara = valor
        self._mascara_bin = self._ip_to_bin(valor)

        if not hasattr(self, 'prefixo'):
            self.prefixo = self._mascara_bin.count('1')

    @property
    def prefixo(self):
        if self._prefixo is None:
            return

        return self._prefixo

    @prefixo.setter
    def prefixo(self, valor):
        if not valor:
            return

        if not isinstance(valor, int) or valor > 32:
            raise TypeError('Prefixo necessita ser inteiro e maior que 32.')

        self._prefixo = valor
        self._mascara_bin = (valor * '1').ljust(32, '0')

        if not hasattr(self,'mascara'):
            self.mascara = self._bin_to_ip(self._mascara_bin)

    @staticmethod
    def _valida_reg(ip):
        regexp = r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'

        if re.match(regexp, ip):
            return True

    @staticmethod
    def _ip_to_bin(ip):
        blocos = ip.split('.')
        blocos_binarios = [bin(int(x))[2:].zfill(8) for x in blocos] # converte para inteiro e binário, separando os 2 primeiros dígitos (0b) e completando as casas com 0
        return ''.join(blocos_binarios)

    @staticmethod
    def _bin_to_ip(ip):
        n = 8
        blocos = [str(int(ip[i:n+i], 2)) for i in range(0, 32, n)]
        return '.'.join(blocos)

    def _set_broadcast(self):
        host_bits = 32 - self.prefixo
        self._broadcast_bin = self._ip_bin[:self.prefixo] + (host_bits * '1')
        self._broadcast = self._bin_to_ip(self._broadcast_bin)
        return self._broadcast

    def _set_rede(self):
        host_bits = 32 - self.prefixo
        self._rede_bin = self._ip_bin[:self.prefixo] + (host_bits * '0')
        self._rede = self._bin_to_ip(self._rede_bin)
        return self._rede

    def _numero_ips(self):
        return 2 ** (32 - self.prefixo)