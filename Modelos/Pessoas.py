import pypyodbc as pyodbc
import json
import datetime
from BD import BdConfig as db

class Pessoas:
    Id = 0
    NomeCompleto = ""
    Email = ""
    DataNasc = datetime.datetime.now()
    Ativo = True
    CriadoEm = datetime.datetime.now()
    AtualizadoEm = datetime.datetime.now()

    def __init__(self, pId=None):
        if pId:
            self.Id = pId
            self.GetById()
        

    def ListarTodos(self, pAtivo=None):
        """Lista as pessoas (todas ou por status)
        de acordo com parametro passado"""
        lista = list()
        config = db.BdConfig()
        conn = pyodbc.connect(config.Conexao)
        cursor = conn.cursor()
        
        if pAtivo is not None:
            cursor.execute('SELECT * FROM Pessoas WHERE Ativo = ?', [pAtivo])
        else:
            cursor.execute('SELECT * FROM Pessoas')

        for linha in cursor.fetchall():
            item = Pessoas()
            item.FillAttr(linha)
            lista.append(item)

        return lista

    def Salvar(self):
        """Salvar um novo registro ou
        atualizar um existente"""
        config = db.BdConfig()
        conn = pyodbc.connect(config.Conexao)
        cursor = conn.cursor()
        params = [self.Id, self.NomeCompleto, self.Email,
        self.DataNasc, self.Ativo]
        if(self.Id > 0):
            cursor.execute("UPDATE Pessoas SET NomeCompleto = ?, Email = ?, DataNasc = ?, Ativo = ? WHERE Id = ?", params)
        else:
            #params.remove(0)
            #params.remove(len(params)-1)
            cursor.execute("INSERT INTO Pessoas(NomeCompleto, Email, DataNasc) VALUES(?,?,?)", params)
        conn.commit()

    #Buscar um registro
    def GetById(self):
        config = db.BdConfig()
        conn = pyodbc.connect(config.Conexao)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Pessoas WHERE Id = ?", [self.Id])
        linha = cursor.fetchone()

        item = Pessoas()
        item.FillAttr(linha)

        return item

    def FillAttr(self, registro):
        self.Id = registro[0]
        self.NomeCompleto = registro[1]
        self.Email = registro[3]
        self.DataNasc = registro[2]
        self.Ativo = registro[4]
        self.CriadoEm = registro[5]
        self.AtualizadoEm = registro[6]