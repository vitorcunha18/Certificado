import sqlite3

class Banco(object):
    def __init__(self, nome):
        self.banco = sqlite3.connect(f'{nome}')
        self.c = self.banco.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS evento (
            id_e INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            nome TEXT,
            data DATETIME
            ); ''')

        self.c.execute('''CREATE TABLE IF NOT EXISTS certificado(
            id_p INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            local TEXT,
            fk_evento integer not null,
            FOREIGN KEY (fk_evento) REFERENCES evento(id_e)
            ); ''')
        self.banco.commit()
        self.banco.close()

class SGBD(object):
    def __init__(self, conexao):
        self.conexao = sqlite3.connect(f'{conexao}')
        self.curso = self.conexao.cursor()

    def Insert_certificado(self, nome, email, local):
        self.curso.execute("INSERT INTO certificado (nome, email, local) VALUES ('{}', '{}', '{}');".format(nome, email, local))
        self.conexao.commit()


