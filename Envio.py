#Biblioteca

import json
import requests
import hashlib

#Base url

letras = 'abcdefghijklmnopqrstuvwxyz'


token = 'd116a75d2caacc33c3d4a27057740eeedc249965'

#Entrada

entrada = input('Olá! Vamos decifrar o código? Por favor, me informe o token: Digite 1 para exemplo ou digite um código ')

if entrada == '1':
    entrada = token
else:
    entrada

site = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={0}'.format(entrada)

questao = requests.get(site)
questao_json = questao.json()

#processamento
token = questao_json['token']
casas = questao_json['numero_casas']
codigo = questao_json['cifrado']
leitura = questao_json['decifrado']
resume = questao_json['resumo_criptografico']

def traduzir():
    frase = ''
    print('Código recebido, processando ... AGUARDE')

    print(codigo)
    for a in codigo:
        if a in letras:
            posicao = letras.index(a)
            frase = frase + letras[posicao - casas]
        else:
            frase = frase + a
    print('Finalizamos! Hehe')

    return frase

leitura = traduzir()



cd = hashlib.sha1(leitura.encode()).hexdigest()

data = {
    'token': token,
    'numero_casas': casas,
    'cifrado':codigo,
    'decifrado':leitura,
    'resumo_criptografico':cd
}

with open('data.json', 'w') as f:
    json.dump(data, f)

site_envio = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token={0}'.format(entrada)


rsp = requests.post(site_envio, files = dict(answer = open('data.json')))

#retorno de resposta do site

print(rsp.status_code)
print(rsp.text)
