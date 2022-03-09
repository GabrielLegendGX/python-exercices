from telnetlib import PRAGMA_HEARTBEAT
import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pidim não está disponivel no momento ')
else:
    print('Consegui acessar o site pudim ')
    #print(site.read())  conteudo html do site