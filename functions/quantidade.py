# Imports
import zeep
from zeep import Client
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep.transports import Transport
import pandas as pd

def quantidadeapi():

    # Variáveis
    codSentenca = "WS.042" #A sentença SQL é criada dentro do RM 
    codColigada = 0 #Todas
    codAplicacao = "P" #Módulo do RM de onde vem os dados

    Usuario = "gia.integra"
    Senha = "Seq@@2023"

    wsdl = "https://sequoialogistica118964.rm.cloudtotvs.com.br:444/wsConsultaSQL.asmx?wsdl" #A documentação está disponível no mesmo link, mas sem o final "?wsdl"

    session = Session()
    session.auth = HTTPBasicAuth(Usuario, Senha)


    client = Client(wsdl, transport=Transport(session=session))
    with client.settings(xml_huge_tree = True ):
        resp = client.service.RealizarConsultaSQL(codSentenca,
                                                codColigada,
                                                codAplicacao,)




    df=pd.read_xml(resp)
    print(df)
    return len(df)


if __name__=="__main__":
    quantidadeapi()