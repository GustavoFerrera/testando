# Imports
# Imports
import zeep
import petl
from zeep import Client
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep.transports import Transport
import pandas as pd
from IPython.display import HTML
from IPython.display import display
from petl import fromcsv




def tabelatb():

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




  
    import pandas as pd
    import plotly.express as px
    df = pd.read_csv('C:\\Users\\106127\\TESTES\\testando\\apresentacao\\base.csv')
    fig = px.bar(df,x = 'COLABORADOR', y = 'Contador', title='GRAF')
    fig.show()



if __name__=="__main__":
    tabelatb()