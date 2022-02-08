from calc import ipv4

rede1 = ipv4(ip = '192.168.0.1', prefixo=24)
print('#######################')
rede2 = ipv4(ip = '192.168.0.1', mascara='222.105.0.1')