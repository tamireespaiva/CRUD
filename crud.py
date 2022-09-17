class MyCrud:

    def __init__(self, banco):
        import sqlite3
        self.conexao = sqlite3.connect(banco)
        self.cursor = self.conexao.cursor()

    def fecharDB(self):
        self.conexao.close()
    
    def criarTabela(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS pessoas(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL, 
                cpf CHAR(11) NOT NULL 
            );
        '''
        self.cursor.execute(sql) 
        print("A tabela pessoas foi criada...")

    def selecionar(self):
        sql = '''
            SELECT * FROM pessoas;
        '''
        resultados = self.cursor.execute(sql)
        for resultado in resultados.fetchall():
            print(resultado)

    def inserir(self, nome, cpf):
        sql = '''
            INSERT INTO pessoas(nome, cpf)
            VALUES(?, ?);
        '''
        self.cursor.execute(sql, (nome, cpf))
        self.conexao.commit()
        print("Os dados foram inseridos com sucesso...")

    def alterar(self, id, nome, cpf):
        sql = '''
            UPDATE pessoas
            SET nome = ?, cpf = ?
            WHERE id = ?
        '''
        self.cursor.execute(sql, (nome, cpf, id))
        self.conexao.commit()
        print("Os dados foram alterados com sucesso...")

    def deletar(self, id):
        sql = '''
            DELETE FROM pessoas
            WHERE id = ?;
        '''
        self.cursor.execute(sql, (id,))
        self.conexao.commit()
        print("Os dados foram deletados com sucesso...")
        
