import sqlite3 as sql

class TransactionObject():
    datab = "clientes.db"
    conn = None
    cur = None
    connected = False

    def connected(self):
        TransactionObject.conn = sql.connect(TransactionObject.datab)
        TransactionObject.cur = TransactionObject.conn.cursor()
        TransactionObject.connected = True

    def disconnect(self):
        TransactionObject.conn.close()
        TransactionObject.connected = False

    def execute(self, sql,parms = None):
        if TransactionObject.connected:
            if parms == None:
                TransactionObject.cur.execute(sql)
            else:
                TransactionObject.cur.execute(sql, parms)
            return True
        else:
            return False
        
    def fetchall(self):
        return TransactionObject.cur.fetchall()

    def persist(self):
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        else:
            return False
    
def initDB():
    trans = TransactionObject()
    trans.connected()

    trans.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")

    trans.persist()
    trans.disconnect()

def insert(nome, sobrenome, email, cpf):
    trans = TransactionObject()
    trans.connected()
    trans.execute("INSERT INT clientes VALUES (NULL, ?, ?, ?, ?)", nome, sobrenome, email, cpf)
    trans.persist()
    trans.disconnect()

def view():
    trans = TransactionObject()
    trans.connected()
    trans.execute("SELECT * FROM clientes")
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def search(nome='', sobrenome='', email='', cpf=''):
    trans = TransactionObject()
    trans.connected()

    trans.execute("SELECT * FROM clientes WHERE nome = ? or sobrenome = ? or email = ? or cpf = ?", nome, sobrenome, email, cpf)
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def delete(id):
    trans = TransactionObject()
    trans.connected()
    trans.execute("DELETE FROM clientes WHERE id = ?", id)
    trans.persist()
    trans.disconnect()

def update(id,nome,sobrenome,email,cpf):
    trans = TransactionObject()
    trans.connected()
    trans.execute("UPDATE clientes SET nome = ?, sobrenome = ?, email = ?, cpf = ? WHERE id = ?", nome, sobrenome, email, cpf, id)
    trans.persist()
    trans.disconnect()

initDB()