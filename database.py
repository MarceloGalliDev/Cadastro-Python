import sqlite3

class Data_base:
    def __init__(self, name = "system.db") -> None:
        self.name = name
    
    def connect(self):
        self.connection = sqlite3.connect(self.name)
        
    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass
    
    def create_table_company(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Empresas(
                CNPJ TEXT,
                RAZAO_SOCIAL TEXT,
                LOGRADOURO TEXT,
                NUMERO TEXT,
                COMPLEMENTO TEXT,
                BAIRRO TEXT,
                MUNICIPIO TEXT,
                UF TEXT,
                CEP TEXT,
                TELEFONE TEXT,
                EMAIL TEXT,
                
                PRIMARY KEY (CNPJ)
            );
        """)
    
    def register_company(self, fullDataSet):
        campos_tabela = ('CNPJ', 'RAZAO_SOCIAL', 'LOGRADOURO','NUMERO', 'COMPLEMENTO', 'BAIRRO', 'MUNICIPIO', 'UF', 'CEP', 'TELEFONE', 'EMAIL')
        
        qntd = ("?,?,?,?,?,?,?,?,?,?,?")
        cursor = self.connection.cursor()
        
        try:
            cursor.execute(f"""INSERT INTO Empresas{campos_tabela} VALUES({qntd})""", fullDataSet)
            self.connection.commit()
            return("OK")
        except:
            return "Erro"
    
    def select_all_companies(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM EMPRESAS ORDER BY RAZAO_SOCIAL")
            empresas = cursor.fetchall()
            return empresas
        except:
            pass
    
    def delete_companies(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Empresas WHERE CNPJ = '{id}' ")
            self.connection.commit()
            return "Cadastro de empresa excluído com sucesso!"
        except:
            return "Erro ao excluir registro!"
    
    def update_company(self, fullDataSet):
        cursor = self.connection.cursor()
        cursor.execute(f""" UPDATE Empresas set
            CNPJ = '{fullDataSet[0]}',
            RAZAO_SOCIAL = '{fullDataSet[1]}',
            LOGRADOURO = '{fullDataSet[2]}',
            NUMERO = '{fullDataSet[3]}',
            COMPLEMENTO = '{fullDataSet[4]}',
            BAIRRO = '{fullDataSet[5]}',
            MUNICIPIO = '{fullDataSet[6]}',
            UF = '{fullDataSet[7]}',
            CEP = '{fullDataSet[8]}',
            TELEFONE = '{fullDataSet[9]}',
            EMAIL = '{fullDataSet[10]}'
            WHERE CNPJ = '{fullDataSet[0]}' """)
        
        self.connection.commit()