import json
import os.path

class BdConfig:
    Conexao = ""
    __Driver = ""
    __Server = ""
    __Database = ""
    __User = ""
    __Password = ""

    def __init__(self):
        scriptpath = os.path.dirname(__file__)
        filename = os.path.join(scriptpath, 'conexao.json')
        with open(filename) as arquivo:    
            dados = json.load(arquivo)
            __Driver = dados['driver']
            __Server = dados['server']
            __Database = dados['database']
            __User = dados['user']
            __Password = dados['password']
            self.Conexao = "Driver={};Server={};Database={};uid={};pwd={}".format(__Driver,__Server,__Database,__User,__Password)