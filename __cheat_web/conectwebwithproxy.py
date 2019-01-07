import socks
import socket
from urllib import request

socks.set_default_proxy(socks.SOCKS5, "1.2.169.109", 61477)
socket.socket = socks.socksocket
r = request.urlopen('http://icanhazip.com')
print(r.read()) # check ips