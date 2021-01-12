import json
import requests
import datetime
import urllib.parse

def dolar_hoje():
    r = requests.get('https://economia.awesomeapi.com.br/json/USD-BRL')
    if r.status_code == 200:
        pesquisa = json.loads(r.content)
        dict_dolar = pesquisa[0]
        venda = dict_dolar['ask']
        compra = dict_dolar['bid']
        maximo = dict_dolar['high']
        minimo = dict_dolar['low']
        data_criacao = dict_dolar['create_date']
        mensagem = 'Um dólar equivale a R${0:.2f} \nCompra: R${1}, Venda: R${0} \nMáximo do dia: R${2}\n Minimo do dia: R${3}'.format(float(venda),compra,maximo,minimo)
        return (mensagem,data_criacao)
    else:
        return 'Erro'
        
def dolar(data):
    print(data)
    r = requests.get('https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaDia(moeda=@moeda,dataCotacao=@dataCotacao)?@moeda=%27USD%27&@dataCotacao=%27{}%27&$top=100&$format=json'.format(data))
    if r.status_code == 200:
        pesquisa = json.loads(r.content)
        if(len(pesquisa['value']) == 0):
            mensagem = 'Não há valor registrado nesta data.'
            return (mensagem,data)
        else:
            dict_dolar = pesquisa['value']
            dict_dolar = dict_dolar[-1]
            venda = dict_dolar['cotacaoVenda']
            compra = dict_dolar['cotacaoCompra']
            data_cotacao = dict_dolar['dataHoraCotacao']
            mensagem = 'Um dólar equivale a R${0:.2f}. \nCompra: R${1}, Venda: R${0}'.format(float(venda),compra)
            return (mensagem,data_cotacao)
    else:
        return 'Erro'

def euro(data):
    r = requests.get('https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaDia(moeda=@moeda,dataCotacao=@dataCotacao)?@moeda=%27EUR%27&@dataCotacao=%27{}%27&$top=100&$format=json'.format(data))
    if r.status_code == 200:
        pesquisa = json.loads(r.content)
        if(len(pesquisa['value']) == 0):
            return 'Não há valor registrado nesta data.'
        else:
            dict_euro = pesquisa['value']
            dict_dolar = dict_euro[-1]
            venda = dict_dolar['cotacaoVenda']
            compra = dict_dolar['cotacaoCompra']
            data_cotacao = dict_dolar['dataHoraCotacao']
            mensagem = 'Um Euro equivale a R${0:.2f}. \nCompra: R${1}, Venda: R${0}'.format(float(venda),compra)
            return (mensagem,data_cotacao)
    else:
        return 'Erro'

def euro_hoje():
    r = requests.get('https://economia.awesomeapi.com.br/json/EUR-BRL')
    if r.status_code == 200:
        pesquisa = json.loads(r.content)
        dict_dolar = pesquisa[0]
        venda = dict_dolar['ask']
        compra = dict_dolar['bid']
        maximo = dict_dolar['high']
        minimo = dict_dolar['low']
        data_criacao = dict_dolar['create_date']
        mensagem = 'Um euro equivale a R${0:.2f} \nCompra: R${1}, Venda: R${0} \nMáximo do dia: R${2}\n Minimo do dia: R${3}'.format(float(venda),compra,maximo,minimo)
        return (mensagem,data_criacao)
    else:
        return 'Erro'

def libra(data):
    r = requests.get('https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaDia(moeda=@moeda,dataCotacao=@dataCotacao)?@moeda=%27GBP%27&@dataCotacao=%27{}%27&$top=100&$format=json'.format(data))
    if r.status_code == 200:
        pesquisa = json.loads(r.content)
        if(len(pesquisa['value']) == 0):
            return 'Não há valor registrado nesta data.'
        else:
            dict_euro = pesquisa['value']
            dict_dolar = dict_euro[-1]
            venda = dict_dolar['cotacaoVenda']
            compra = dict_dolar['cotacaoCompra']
            data_cotacao = dict_dolar['dataHoraCotacao']
            mensagem = 'Uma libra equivale a R${0:.2f}. \nCompra: R${1}, Venda: R${0}'.format(float(venda),compra)
            return (mensagem,data_cotacao)
    else:
        return 'Erro'

def libra_hoje():
    r = requests.get('https://economia.awesomeapi.com.br/json/GBP-BRL')
    if r.status_code == 200:
        pesquisa = json.loads(r.content)
        dict_dolar = pesquisa[0]
        venda = dict_dolar['ask']
        compra = dict_dolar['bid']
        maximo = dict_dolar['high']
        minimo = dict_dolar['low']
        data_criacao = dict_dolar['create_date']
        mensagem = 'Uma libra equivale a R${0:.2f} \nCompra: R${1}, Venda: R${0} \nMáximo do dia: R${2}\n Minimo do dia: R${3}'.format(float(venda),compra,maximo,minimo)
        return (mensagem,data_criacao)
    else:
        return 'Erro'

def corona(pais,estado,sigla):
    if(pais is not None):
        if(pais == 'United States'):
            url = 'US'
        else:
            url = urllib.parse.quote(pais)
        print(url)
        r_pais = requests.get('https://covid19-brazil-api.now.sh/api/report/v1/{}'.format(url))
        if r_pais.status_code == 200:
            dict_pais = json.loads(r_pais.content)
            dict_pais = dict_pais['data']
            confirmados = dict_pais['confirmed']
            mortos = dict_pais['deaths']
            curados = dict_pais['recovered']
            ativos = dict_pais['cases']
            menssagem = '{} :flag_{}: \n ✅ Confirmados: {} | 😷 Ativos: {} \n 💀 Mortos: {} | ♻️ Curados: {}'.format(pais,sigla,confirmados,ativos,mortos,curados)
        return menssagem
    else:
        r_estado = requests.get('https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{}'.format(estado))
        if r_estado.status_code == 200:
            dict_estado = json.loads(r_estado.content)
            estado_nome = dict_estado['state']
            mortos = dict_estado['deaths']
            confirmados = dict_estado['cases']
            menssagem = '{}: \n ✅ Confirmados: {} | 💀 Mortos: {}'.format(estado_nome,confirmados,mortos)
        return menssagem

def topcorona():
    r_pais = requests.get('https://covid19-brazil-api.now.sh/api/report/v1/countries')
    if r_pais.status_code == 200:
        dict_pais = json.loads(r_pais.content)
        dict_pais = dict_pais['data']
        lista = list()
        lista = sorted(dict_pais, key=lambda k: k['confirmed'], reverse=True)[:5]
    return lista